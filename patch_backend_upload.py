import re
from pathlib import Path

file_path = Path("D:\\SIH2026\\backend\\main.py")
content = file_path.read_text(encoding="utf-8")

# Add imports for file upload
if "from fastapi import FastAPI, File, UploadFile" not in content:
    content = content.replace("from fastapi import FastAPI", "from fastapi import FastAPI, File, UploadFile")

# The upload endpoint logic
upload_endpoint = """
@app.post("/api/upload")
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
    base_data = _generate_digital_twin_forecast(days=90)
    
    # Artificially boost the cashflow to simulate "New Invoices Found in Tally CSV"
    for pt in base_data["projectedCashflow"]:
        pt["balance"] += 85000  # Added 85k to balance
        pt["forecastLow"] += 85000
        pt["forecastHigh"] += 85000
        
    base_data["summary"]["cashOnHand"] += 85000
    base_data["summary"]["minProjectedBalance"] += 85000
    
    return base_data
"""

if "@app.post(\"/api/upload\")" not in content:
    content = content + "\n" + upload_endpoint

file_path.write_text(content, encoding="utf-8")
print("Backend patched for file upload.")
