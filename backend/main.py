from pydantic import BaseModel
from ml_model import ml_engine
import json
import io
import csv
from collections import defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any

from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

APP_ROOT = Path(__file__).resolve().parent
BANK_PATH = APP_ROOT / "aa_bank_statement.json"
INVOICES_PATH = APP_ROOT / "gstn_invoices.json"

app = FastAPI(title="Consent-Based MSME Cash-Flow Digital Twin API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def _read_json(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8") as fp:
        return json.load(fp)


def _safe_date(raw: str) -> date:
    return datetime.strptime(raw, "%Y-%m-%d").date()


def _gst_due_date(issue_dt: date) -> date:
    due_year = issue_dt.year + (1 if issue_dt.month == 12 else 0)
    due_month = 1 if issue_dt.month == 12 else issue_dt.month + 1
    return date(due_year, due_month, 20)


def _historical_delay_proxy(buyer_name: str, invoices: list[dict[str, Any]], start_day: date) -> int:
    delays = []
    for inv in invoices:
        if str(inv.get("buyer_name", "")).lower() == buyer_name.lower():
            due_dt = _safe_date(inv["due_date"]) if inv.get("due_date") else None
            if due_dt and due_dt < start_day:
                delays.append(max(0, (start_day - due_dt).days))
    if delays:
        return int(sum(delays) / len(delays))
    
    profiles = {"reliance": 18, "tata": 10, "infosys": 7, "wipro": 12}
    return profiles.get(buyer_name.lower(), 9)

def _buyer_delay_slope(buyer_name: str, invoices: list[dict[str, Any]], start_day: date) -> float:
    buyer_invoices = sorted(
        [inv for inv in invoices if str(inv.get("buyer_name", "")).lower() == buyer_name.lower() and inv.get("issue_date")],
        key=lambda x: _safe_date(x["issue_date"])
    )
    recent = buyer_invoices[-6:]
    if len(recent) < 2:
        return 0.0
    
    delays = [max(0, (start_day - _safe_date(inv["due_date"])).days) for inv in recent]
    x = list(range(len(delays)))
    y = delays
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xx = sum(i*i for i in x)
    denominator = (n * sum_xx - sum_x ** 2)
    if denominator == 0:
        return 0.0
    return (n * sum(i*j for i, j in zip(x, y)) - sum_x * sum_y) / denominator


def _estimate_daily_operating_runrate(bank_txns: list[dict[str, Any]]) -> tuple[float, float, float]:
    if not bank_txns:
        return 5000.0, 4200.0, 160000.0

    operating_amounts = [
        float(item.get("amount", 0.0))
        for item in bank_txns
        if str(item.get("category", "")).lower() == "operating"
    ]
    all_amounts = [float(item.get("amount", 0.0)) for item in bank_txns]

    observed_dates = [_safe_date(item["date"]) for item in bank_txns if item.get("date")]
    span_days = 180
    if observed_dates:
        span_days = max(30, (max(observed_dates) - min(observed_dates)).days + 1)

    operating_inflow = sum(value for value in operating_amounts if value > 0)
    operating_outflow = abs(sum(value for value in operating_amounts if value < 0))

    daily_inflow = max(2500.0, operating_inflow / span_days)
    daily_outflow = max(2800.0, operating_outflow / span_days)

    net_cash = sum(all_amounts)
    start_balance = max(90000.0, 130000.0 + (net_cash * 0.08))

    return daily_outflow, daily_inflow, start_balance


class ShockConfig(BaseModel):
    buyerDelayDays: int = Field(default=0, ge=0, le=45)
    revenueDropPct: float = Field(default=0.0, ge=0.0, le=60.0)
    costRisePct: float = Field(default=0.0, ge=0.0, le=60.0)


def _build_simulation(
    invoices: list[dict[str, Any]],
    bank_txns: list[dict[str, Any]],
    shock: ShockConfig,
) -> tuple[list[dict[str, Any]], dict[str, Any], list[dict[str, Any]]]:
    daily_outflow, daily_inflow, current_balance = _estimate_daily_operating_runrate(bank_txns)
    horizon_days = 90
    start_day = datetime.utcnow().date()

    invoice_receipts_by_day: dict[date, float] = defaultdict(float)
    gst_by_day: dict[date, float] = defaultdict(float)
    buyer_totals: dict[str, float] = defaultdict(float)
    payment_delays: list[int] = []

    for invoice in invoices:
        amount = float(invoice.get("amount", 0.0))
        buyer = str(invoice.get("buyer_name", "Unknown"))
        if amount <= 0:
            continue

        buyer_totals[buyer] += amount

        issue_dt = _safe_date(invoice["issue_date"]) if invoice.get("issue_date") else start_day
        due_dt = _safe_date(invoice["due_date"]) if invoice.get("due_date") else (issue_dt + timedelta(days=30))
        buyer_delay = _historical_delay_proxy(buyer, invoices, start_day) + shock.buyerDelayDays
        payment_delays.append(buyer_delay)

        expected_receipt = due_dt + timedelta(days=buyer_delay)
        adjusted_receipt = amount * (1.0 - shock.revenueDropPct / 100.0)
        invoice_receipts_by_day[expected_receipt] += adjusted_receipt

        gst_due_dt = _gst_due_date(issue_dt)
        gst_by_day[gst_due_dt] += amount * 0.18

    total_receivables = sum(buyer_totals.values())
    top_buyer = max(buyer_totals.items(), key=lambda item: item[1])[0] if buyer_totals else "Unknown"
    concentration_slope = _buyer_delay_slope(top_buyer, invoices, start_day)
    concentration = (max(buyer_totals.values()) / total_receivables * 100.0) if buyer_totals else 0.0

    adjusted_daily_inflow = daily_inflow * (1.0 - shock.revenueDropPct / 100.0)
    adjusted_daily_outflow = daily_outflow * (1.0 + shock.costRisePct / 100.0)

    mean_delay = sum(payment_delays) / len(payment_delays) if payment_delays else 0.0
    variance = (
        sum((delay - mean_delay) ** 2 for delay in payment_delays) / len(payment_delays)
        if payment_delays
        else 0.0
    )
    std_dev = variance ** 0.5

    projected: list[dict[str, Any]] = []
    gst_timeline: list[dict[str, Any]] = []
    min_balance = current_balance
    negative_days = 0

    for day in range(1, horizon_days + 1):
        cursor = start_day + timedelta(days=day - 1)
        receipt_inflow = invoice_receipts_by_day.get(cursor, 0.0)
        gst_outflow = gst_by_day.get(cursor, 0.0)

        inflow = adjusted_daily_inflow + receipt_inflow
        outflow = adjusted_daily_outflow + gst_outflow
        current_balance = current_balance + inflow - outflow

        min_balance = min(min_balance, current_balance)
        if current_balance < 0:
            negative_days += 1

        
        avg_daily_receipts = total_receivables / 90.0 if total_receivables else 0.0
        margin_of_error = 1.96 * std_dev * avg_daily_receipts

        projected.append(
            {
                "day": day,
                "label": f"D{day}",
                "date": cursor.isoformat(),
                "balance": round(current_balance, 2),
                "forecastLow": round(current_balance - margin_of_error, 2),
                "forecastHigh": round(current_balance + margin_of_error, 2),
                "inflow": round(inflow, 2),
                "outflow": round(outflow, 2),
                "gstOutflow": round(gst_outflow, 2),
            }
        )

        if gst_outflow > 0:
            inflow_window = sum(
                invoice_receipts_by_day.get(cursor - timedelta(days=offset), 0.0)
                for offset in range(0, 15)
            )
            gst_timeline.append(
                {
                    "dueDate": cursor.isoformat(),
                    "gstAmount": round(gst_outflow, 2),
                    "expectedInflowsBeforeDue": round(inflow_window, 2),
                    "shortfall": round(max(0.0, gst_outflow - inflow_window), 2),
                }
            )

    total_gst_due = sum(item["gstAmount"] for item in gst_timeline)
    risk_level = "Stable"
    if concentration > 40.0 or negative_days >= 8:
        risk_level = "Critical"
    elif concentration > 25.0 or negative_days > 0:
        risk_level = "Moderate"

    health_score = max(20, min(95, int(95 - concentration * 0.8 - negative_days * 1.4)))

    summary = {
        "cashOnHand": round(projected[-1]["balance"] if projected else current_balance, 2),
        "gstDue": round(total_gst_due, 2),
        "receivables": round(total_receivables, 2),
        "burnRate": round(adjusted_daily_outflow * 30, 2),
        "healthScore": health_score,
        "buyerConcentration": round(concentration, 2),
        "concentrationTrendSlope": round(concentration_slope, 4),
        "riskLevel": risk_level,
        "minProjectedBalance": round(min_balance, 2),
        "negativeCashDays": negative_days,
    }

    buyer_breakdown = [
        {
            "name": name,
            "value": round(total, 2),
            "share": round((total / total_receivables) * 100.0, 2) if total_receivables else 0.0,
        }
        for name, total in sorted(buyer_totals.items(), key=lambda item: item[1], reverse=True)
    ]

    return projected, summary, buyer_breakdown, gst_timeline


def _build_alerts(summary: dict[str, Any], gst_timeline: list[dict[str, Any]]) -> list[dict[str, Any]]:
    alerts = []

    if summary["buyerConcentration"] > 40:
        slope_msg = ""
        if summary.get("concentrationTrendSlope", 0.0) > 0:
            slope_msg = f" Worsening trend detected (slope: {summary['concentrationTrendSlope']})."
        alerts.append(
            {
                "type": "Concentration risk",
                "message": f"A single buyer accounts for more than 40% of MSME receivables. Exposure is elevated.{slope_msg}",
                "severity": "high",
            }
        )

    shortfall_periods = [item for item in gst_timeline if item.get("shortfall", 0.0) > 0]
    if shortfall_periods:
        total_shortfall = sum(item["shortfall"] for item in shortfall_periods)
        alerts.append(
            {
                "type": "GST shortfall",
                "message": f"GST liability exceeds projected inflows before due date. Next-cycle shortfall of {round(total_shortfall, 2)}.",
                "severity": "high",
            }
        )

    if not alerts:
        alerts.append(
            {
                "type": "Healthy outlook",
                "message": "Cashflow remains inside a manageable range with moderate volatility.",
                "severity": "low",
            }
        )

    return alerts


def _build_recommendations(summary: dict[str, Any]) -> list[dict[str, Any]]:
    if summary["riskLevel"] == "Critical":
        return [
            {"title": "Invoice discounting", "detail": "Discount Reliance receivables to unlock cash within 72 hours.", "cost": "Low to medium"},
            {"title": "Working capital line", "detail": "Use a short tenor loan to bridge GST payables before buyer cash arrives.", "cost": "Medium"},
        ]

    return [
        {"title": "Wait and chase", "detail": "Follow up on slow-paying buyers while preserving liquidity buffer.", "cost": "Low"},
        {"title": "Invoice discounting", "detail": "Use invoice discounting selectively for high-value delayed invoices.", "cost": "Low to medium"},
    ]


@app.get("/health")
async def health_check() -> dict[str, Any]:
    return {"status": "ok", "timestamp": datetime.utcnow().isoformat()}


@app.get("/api/simulate")
async def simulate_cashflow(
    buyerDelayDays: int = 0,
    revenueDropPct: float = 0.0,
    costRisePct: float = 0.0,
) -> dict[str, Any]:
    invoices = _read_json(INVOICES_PATH)
    bank_txns = _read_json(BANK_PATH)

    shock = ShockConfig(
        buyerDelayDays=buyerDelayDays,
        revenueDropPct=revenueDropPct,
        costRisePct=costRisePct,
    )

    projection, summary, buyer_breakdown, gst_timeline = _build_simulation(
        invoices=invoices,
        bank_txns=bank_txns,
        shock=shock,
    )
    alerts = _build_alerts(summary, gst_timeline)
    recommendations = _build_recommendations(summary)

    return {
        "meta": {
            "timelineDays": 90,
            "generatedAt": datetime.utcnow().isoformat(),
            "source": "mock-aa-gstn",
            "shockConfig": shock.model_dump(),
        },
        "summary": summary,
        "projectedCashflow": projection,
        "alerts": alerts,
        "recommendations": recommendations,
        "buyerBreakdown": buyer_breakdown,
        "gstTimeline": gst_timeline,
    }


@app.post("/api/upload")
async def upload_offline_data(file: UploadFile = File(...)):
    content = await file.read()
    try:
        text = content.decode("utf-8")
        reader = csv.DictReader(io.StringIO(text))
        rows = list(reader)
        
        recent_txns = []
        for r in reversed(rows[-5:]):
            is_credit = bool(r.get("Credit", "").strip())
            amt = r.get("Credit") if is_credit else r.get("Debit", "0")
            desc = r.get("Description", "Unknown Transaction")
            
            recent_txns.append({
                "source": desc[:25] + "..." if len(desc) > 25 else desc,
                "amount": f"{amt}",
                "status": "Settled" if is_credit else "Paid",
                "ai": "Synced from CSV",
                "type": "success" if is_credit else "warning"
            })
            
        real_balance = float(rows[-1].get("Balance", 0))
    except Exception as e:
        print(f"CSV Parse Error: {e}")
        rows = []
        recent_txns = []
        real_balance = 500000

    # 1. EXTRACT ML FEATURES FROM CSV
    
    # Extract buyer breakdown
    buyer_totals = {}
    for r in rows:
        is_credit = bool(r.get("Credit", "").strip())
        desc = r.get("Description", "Unknown Transaction")
        amt_str = r.get("Credit", "0") if is_credit else "0"
        if not str(amt_str).strip(): amt_str = "0"
        try:
            amt = float(amt_str)
        except:
            amt = 0.0
            
        if is_credit and "Opening" not in desc:
            buyer_totals[desc] = buyer_totals.get(desc, 0.0) + amt
            
    total_receivables = sum(buyer_totals.values())
    buyer_breakdown = [
        {
            "name": name,
            "value": round(total, 2),
            "share": round((total / total_receivables) * 100.0, 2) if total_receivables else 0.0
        }
        for name, total in sorted(buyer_totals.items(), key=lambda item: item[1], reverse=True)
    ]
    
    features = ml_engine.extract_features(rows)

    
    # 2. PREDICT BASELINE DELAY using the trained Kaggle Random Forest
    base_delay = ml_engine.predict_buyer_delay(**features)
    
    # 3. CALCULATE CASH FLOW CURVE using dynamic base delay
    cashflow_array = ml_engine.generate_90_day_forecast(current_balance=real_balance, base_delay=base_delay)
    
    projectedCashflow = []
    min_balance = real_balance
    for i, bal in enumerate(cashflow_array):
        denormalized_bal = bal * 20000
        min_balance = min(min_balance, denormalized_bal)
        projectedCashflow.append({
            "day": i + 1,
            "balance": denormalized_bal,
            "forecastLow": denormalized_bal * 0.9,
            "forecastHigh": denormalized_bal * 1.1,
            "gstOutflow": 180000 if (i+1) in [20, 50, 80] else 0
        })

    # Prepare summary with the AI predicted delay
    summary = {
        "cashOnHand": real_balance,
        "gstDue": 540000,
        "minProjectedBalance": min_balance,
        "buyer_delay_days": base_delay
    }
    
    return {
        "projectedCashflow": projectedCashflow,
        "summary": summary,
        "recentTxns": recent_txns,
        "dataSource": "ml_offline_csv",
        "buyerBreakdown": buyer_breakdown
    }


class MLPredictionRequest(BaseModel):
    current_balance: float
    slider_delay_days: int
    revenue_shock: float = 0.0
    cost_shock: float = 0.0

@app.post("/api/ml/predict")
async def predict_liquidity(req: MLPredictionRequest):
    # 1. ML Model predicts the baseline delay from historical data
    # (Here we mock feature extraction)
    predicted_base_delay = ml_engine.predict_buyer_delay(None)
    
    # 2. ML Time-Series engine generates the 90 day curve based on the slider override
    forecast = ml_engine.generate_90_day_forecast(
        current_balance=req.current_balance,
        base_delay=predicted_base_delay,
        shock_scenario_delay=req.slider_delay_days,
        revenue_shock=req.revenue_shock,
        cost_shock=req.cost_shock
    )
    
    # 3. ML Action Matrix recommends an action
    action = ml_engine.recommend_action(forecast)
    
    return {
        "predicted_base_delay": predicted_base_delay,
        "forecast_90_days": forecast,
        "recommended_action": action
    }
