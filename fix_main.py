import os
import re

file_path = r'D:\SIH2026\backend\main.py'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Locate @app.post("/api/upload")
start_idx = text.find('@app.post("/api/upload")')
end_idx = text.find('class MLPredictionRequest', start_idx)

if start_idx != -1 and end_idx != -1:
    old_upload_block = text[start_idx:end_idx]
    
    new_upload_block = """@app.post("/api/upload")
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
        "dataSource": "ml_offline_csv"
    }


"""
    text = text[:start_idx] + new_upload_block + text[end_idx:]
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Fixed upload endpoint in main.py!")
else:
    print("Could not find upload block.")
