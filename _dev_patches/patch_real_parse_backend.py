import re
from pathlib import Path

file_path = Path("D:\\SIH2026\\backend\\main.py")
content = file_path.read_text(encoding="utf-8")

# 1. Add io and csv imports
if "import io" not in content:
    content = content.replace("import json", "import json\nimport io\nimport csv")

# 2. Rewrite the upload endpoint to ACTUALLY read the CSV file
old_endpoint = """@app.post("/api/upload")
async def upload_offline_data(file: UploadFile = File(...)):
    \"\"\"
    Mock endpoint to handle CSV/Excel file uploads.
    In a real app, this would parse the CSV using pandas.
    For the hackathon demo, we read the filename, pretend to parse it, 
    and return an aggressively 'improved' cashflow to prove the UI updates.
    \"\"\"
    # Read a chunk just to prove we received it
    contents = await file.read(1024) 
    
    # Generate the base simulation
    base_data = await simulate_cashflow()
    
    # Artificially boost the cashflow to simulate "New Invoices Found in Tally CSV"
    for pt in base_data["projectedCashflow"]:
        pt["balance"] += 85000  # Added 85k to balance
        pt["forecastLow"] += 85000
        pt["forecastHigh"] += 85000
        
    base_data["summary"]["cashOnHand"] += 85000
    base_data["summary"]["minProjectedBalance"] += 85000
    
    return base_data"""

new_endpoint = """@app.post("/api/upload")
async def upload_offline_data(file: UploadFile = File(...)):
    content = await file.read()
    try:
        text = content.decode("utf-8")
        reader = csv.DictReader(io.StringIO(text))
        rows = list(reader)
        
        # Parse the last 3 rows to send back to the frontend table
        recent_txns = []
        for r in reversed(rows[-3:]):
            is_credit = bool(r.get("Credit", "").strip())
            amt = r.get("Credit") if is_credit else r.get("Debit", "0")
            desc = r.get("Description", "Unknown Transaction")
            
            recent_txns.append({
                "source": desc[:25] + "..." if len(desc) > 25 else desc,
                "amount": f"₹{amt}",
                "status": "Settled" if is_credit else "Paid",
                "ai": "Synced from CSV",
                "type": "success" if is_credit else "warning"
            })
            
        # Get actual final balance from CSV
        real_balance = float(rows[-1].get("Balance", 0))
    except Exception as e:
        print(f"CSV Parse Error: {e}")
        recent_txns = []
        real_balance = 500000

    # Generate base simulation
    base_data = await simulate_cashflow()
    
    # Shift chart to match the real balance from the CSV
    diff = real_balance - base_data["summary"]["cashOnHand"]
    
    for pt in base_data["projectedCashflow"]:
        pt["balance"] += diff
        pt["forecastLow"] += diff
        pt["forecastHigh"] += diff
        
    base_data["summary"]["cashOnHand"] = real_balance
    base_data["summary"]["minProjectedBalance"] += diff
    
    return {
        "projectedCashflow": base_data["projectedCashflow"],
        "summary": base_data["summary"],
        "recentTxns": recent_txns
    }"""

content = content.replace(old_endpoint, new_endpoint)

file_path.write_text(content, encoding="utf-8")
print("Backend file parsing updated.")
