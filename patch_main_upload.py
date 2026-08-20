import os
import re

file_path = r'D:\SIH2026\backend\main.py'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# We want to replace the hardcoded "projectedCashflow" logic in /api/upload
old_logic_pattern = r"recent_txns\.append\(\{.*?\}\).*?# Fake projected cashflow.*?\]"

new_logic = """recent_txns.append({
                "source": desc[:25] + "..." if len(desc) > 25 else desc,
                "amount": f"₹{amt}",
                "status": "Settled",
                "ai": "Analyzed",
                "type": "success" if is_credit else "warning"
            })
            
        # 1. EXTRACT ML FEATURES FROM CSV
        features = ml_engine.extract_features(rows)
        
        # 2. PREDICT BASELINE DELAY using the trained Kaggle Random Forest
        base_delay = ml_engine.predict_buyer_delay(**features)
        
        # 3. CALCULATE CASH FLOW CURVE
        initial_balance = 1500000
        cashflow_array = ml_engine.generate_90_day_forecast(current_balance=initial_balance, base_delay=base_delay)
        
        projectedCashflow = []
        for i, bal in enumerate(cashflow_array):
            projectedCashflow.append({
                "day": i + 1,
                "balance": bal * 20000,  # Denormalize scale
                "forecastLow": bal * 18000
            })"""

# Perform replacement
text = re.sub(r"recent_txns\.append\(\{.*?\}\).*?# Fake projected cashflow.*?\]", new_logic, text, flags=re.DOTALL)

# Update the summary dictionary to return the dynamic delay
text = re.sub(r'"buyer_delay_days": 45', '"buyer_delay_days": base_delay', text)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)
print("Updated main.py successfully.")
