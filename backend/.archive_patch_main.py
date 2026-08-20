import re
from typing import Any

with open("D:\\SIH2026\\backend\\main.py", "r", encoding="utf-8") as f:
    code = f.read()

# 1. Replace _buyer_base_delay with historical logic
old_delay_func = """def _buyer_base_delay(buyer_name: str) -> int:
    profiles = {
        "reliance": 18,
        "tata": 10,
        "infosys": 7,
        "wipro": 12,
    }
    return profiles.get(buyer_name.lower(), 9)"""

new_delay_func = """def _historical_delay_proxy(buyer_name: str, invoices: list[dict[str, Any]], start_day: date) -> int:
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
    return (n * sum(i*j for i, j in zip(x, y)) - sum_x * sum_y) / denominator"""

code = code.replace(old_delay_func, new_delay_func)

# 2. Call historical delay proxy in _build_simulation
code = code.replace("buyer_delay = _buyer_base_delay(buyer) + shock.buyerDelayDays", 
                    "buyer_delay = _historical_delay_proxy(buyer, invoices, start_day) + shock.buyerDelayDays")

# 3. Add concentrationTrendSlope to summary
old_total_rec = "total_receivables = sum(buyer_totals.values())"
new_total_rec = """total_receivables = sum(buyer_totals.values())
    top_buyer = max(buyer_totals.items(), key=lambda item: item[1])[0] if buyer_totals else "Unknown"
    concentration_slope = _buyer_delay_slope(top_buyer, invoices, start_day)"""
code = code.replace(old_total_rec, new_total_rec)

old_summary_conc = '"buyerConcentration": round(concentration, 2),'
new_summary_conc = '"buyerConcentration": round(concentration, 2),\n        "concentrationTrendSlope": round(concentration_slope, 4),'
code = code.replace(old_summary_conc, new_summary_conc)

# 4. Better variance calculation in _build_simulation loop
old_uncertainty = "uncertainty = max(0.06, min(0.2, (std_dev / 100.0)))"
new_uncertainty = """
        avg_daily_receipts = total_receivables / 90.0 if total_receivables else 0.0
        margin_of_error = 1.96 * std_dev * avg_daily_receipts
"""
code = code.replace(old_uncertainty, new_uncertainty)

old_forecast_low = '"forecastLow": round(current_balance * (1 - uncertainty), 2),'
new_forecast_low = '"forecastLow": round(current_balance - margin_of_error, 2),'
old_forecast_high = '"forecastHigh": round(current_balance * (1 + uncertainty), 2),'
new_forecast_high = '"forecastHigh": round(current_balance + margin_of_error, 2),'
code = code.replace(old_forecast_low, new_forecast_low)
code = code.replace(old_forecast_high, new_forecast_high)

# 5. Fix GST Shortfall Alert in _build_alerts
# Update signature of _build_alerts everywhere
code = code.replace("def _build_alerts(summary: dict[str, Any]) -> list[dict[str, Any]]:", 
                    "def _build_alerts(summary: dict[str, Any], gst_timeline: list[dict[str, Any]]) -> list[dict[str, Any]]:")
code = code.replace("alerts = _build_alerts(summary)", "alerts = _build_alerts(summary, gst_timeline)")

# Fix alert logic
old_alerts = """    if summary["buyerConcentration"] > 40:
        alerts.append(
            {
                "type": "Concentration risk",
                "message": "Reliance accounts for more than 40% of MSME receivables. Exposure is elevated.",
                "severity": "high",
            }
        )

    if summary["gstDue"] > summary["cashOnHand"]:
        alerts.append(
            {
                "type": "GST shortfall",
                "message": "GST liability exceeds current inflow coverage. Working-capital stress is likely.",
                "severity": "high",
            }
        )"""

new_alerts = """    if summary["buyerConcentration"] > 40:
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
        )"""

code = code.replace(old_alerts, new_alerts)

with open("D:\\SIH2026\\backend\\main.py", "w", encoding="utf-8") as f:
    f.write(code)

print("Patching complete.")
