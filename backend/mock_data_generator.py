import json
import random
from datetime import datetime, timedelta

def generate_dates(start_date, end_date, num_dates):
    delta = end_date - start_date
    return [start_date + timedelta(days=random.randint(0, delta.days)) for _ in range(num_dates)]

def generate_mock_data():
    today = datetime.now()
    six_months_ago = today - timedelta(days=180)
    
    # 1. AA Bank Statement
    transactions = []
    categories = ['Operating', 'Financing', 'Tax']
    for i in range(100):
        tx_date = six_months_ago + timedelta(days=random.randint(0, 180))
        tx = {
            "tx_id": f"TXN{1000+i}",
            "date": tx_date.strftime("%Y-%m-%d"),
            "amount": round(random.uniform(-5000, 50000), 2),
            "category": random.choice(categories),
            "description": f"Mock transaction {i}"
        }
        transactions.append(tx)
        
    with open("aa_bank_statement.json", "w") as f:
        json.dump(transactions, f, indent=4)
        
    # 2. GSTN Invoices
    invoices = []
    buyers = ['Reliance', 'Tata', 'Wipro', 'Infosys']
    for i in range(50):
        # Make Reliance have a lot of invoices (concentration risk)
        buyer = 'Reliance' if random.random() < 0.6 else random.choice(buyers)
        
        issue_date = six_months_ago + timedelta(days=random.randint(0, 180))
        due_date = issue_date + timedelta(days=30)
        
        inv = {
            "invoice_id": f"INV{2000+i}",
            "buyer_name": buyer,
            "amount": round(random.uniform(1000, 100000), 2),
            "issue_date": issue_date.strftime("%Y-%m-%d"),
            "due_date": due_date.strftime("%Y-%m-%d")
        }
        invoices.append(inv)
        
    with open("gstn_invoices.json", "w") as f:
        json.dump(invoices, f, indent=4)
        
    print("Generated aa_bank_statement.json and gstn_invoices.json")

if __name__ == "__main__":
    generate_mock_data()
