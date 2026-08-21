import re

with open('backend/main.py', 'r', encoding='utf-8') as f:
    text = f.read()

buyer_logic = """
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
"""

text = text.replace('features = ml_engine.extract_features(rows)', buyer_logic)
text = text.replace('"dataSource": "ml_offline_csv"', '"dataSource": "ml_offline_csv",\n        "buyerBreakdown": buyer_breakdown')

with open('backend/main.py', 'w', encoding='utf-8') as f:
    f.write(text)
print("Updated backend to parse buyer breakdown")
