import csv
from datetime import date, timedelta
from random import randint

file_path = "D:\\SIH2026\\sample_bank_export.csv"

# Starting parameters
current_date = date(2026, 3, 1)
end_date = date(2026, 8, 19)
balance = 450000.00

rows = [["Date", "Description", "Reference_No", "Debit", "Credit", "Balance"]]

def add_row(tx_date, desc, ref, debit, credit):
    global balance
    if debit:
        balance -= debit
    if credit:
        balance += credit
    rows.append([
        tx_date.strftime("%Y-%m-%d"),
        desc,
        ref,
        f"{debit:.2f}" if debit else "",
        f"{credit:.2f}" if credit else "",
        f"{balance:.2f}"
    ])

# Generate months of data
while current_date <= end_date:
    year = current_date.year
    month = current_date.month
    
    # 1st: Rent
    add_row(date(year, month, 1), "OFFICE RENT - WFH PLAZA", f"IMPS{randint(1000,9999)}", 45000.00, None)
    
    # 5th: Salaries
    add_row(date(year, month, 5), "SALARY DISBURSEMENT", f"NEFT-SAL-{month:02d}", 125000.00, None)
    
    # 8th: Software / Cloud
    add_row(date(year, month, 8), "AWS CLOUD SERVICES", f"CC-AUTOPAY-{randint(100,999)}", 12500.00, None)
    
    # 12th: Major Inflow (Reliance) -> Creates Concentration Risk
    reliance_amt = randint(180000, 220000)
    add_row(date(year, month, 12), f"NEFT-RELIANCE RETAIL-INV{month}01", f"N{randint(100000,999999)}", None, reliance_amt)
    
    # 16th: Supplier Payment
    supplier_amt = randint(70000, 95000)
    add_row(date(year, month, 16), "RTGS-ABC POLYMERS LTD", f"R{randint(100000,999999)}", supplier_amt, None)
    
    # 20th: GST Payment
    gst_amt = randint(25000, 35000)
    add_row(date(year, month, 20), f"GST PAYMENT - {current_date.strftime('%b').upper()}", f"TAX{randint(10000,99999)}", gst_amt, None)
    
    # 24th: Secondary Inflow (Tata)
    tata_amt = randint(60000, 90000)
    add_row(date(year, month, 24), f"RTGS-TATA ELECTRONICS-INV{month}02", f"R{randint(100000,999999)}", None, tata_amt)
    
    # 27th: Minor Inflow (Other SME)
    sme_amt = randint(15000, 30000)
    add_row(date(year, month, 27), f"UPI-KUMAR ENTERPRISES", f"UPI{randint(100000,999999)}", None, sme_amt)
    
    # 29th: Utilities / Misc
    add_row(date(year, month, 29), "ELECTRICITY BOARD", f"BPAY{randint(1000,9999)}", 18500.00, None)

    # Move to next month
    if month == 12:
        current_date = date(year + 1, 1, 1)
    else:
        current_date = date(year, month + 1, 1)

# Write to file
with open(file_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

print(f"Generated {len(rows)-1} rows of rich financial data.")
