import csv
from datetime import date
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

# Generate months of highly profitable data
while current_date <= end_date:
    year = current_date.year
    month = current_date.month
    
    # Tiny Rent
    add_row(date(year, month, 1), "OFFICE RENT - WFH PLAZA", f"IMPS{randint(1000,9999)}", 15000.00, None)
    
    # Tiny Salaries
    add_row(date(year, month, 5), "SALARY DISBURSEMENT", f"NEFT-SAL-{month:02d}", 45000.00, None)
    
    # Massive Inflow (Reliance) -> Creates Concentration Risk but massive profitability
    reliance_amt = randint(580000, 620000)
    add_row(date(year, month, 12), f"NEFT-RELIANCE RETAIL-INV{month}01", f"N{randint(100000,999999)}", None, reliance_amt)
    
    # Tiny Supplier
    add_row(date(year, month, 16), "RTGS-ABC POLYMERS LTD", f"R{randint(100000,999999)}", 20000.00, None)
    
    # Secondary Inflow (Tata)
    tata_amt = randint(160000, 190000)
    add_row(date(year, month, 24), f"RTGS-TATA ELECTRONICS-INV{month}02", f"R{randint(100000,999999)}", None, tata_amt)
    
    if month == 12:
        current_date = date(year + 1, 1, 1)
    else:
        current_date = date(year, month + 1, 1)

with open(file_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

print("Generated highly profitable CSV.")
