import os
import joblib
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

print(" Loading Kaggle Dataset (Sampling 150,000 rows for fast laptop training)...")
# We sample to prevent blowing up laptop RAM. You can remove nrows later!
df = pd.read_csv("data/payment_history.csv", nrows=150000)

print(" Engineering Features...")
# 1. Filter only Paid invoices to calculate delay
df = df[df["payment_status"] == "Paid"].copy()

# 2. Convert dates
df["due_date"] = pd.to_datetime(df["due_date"])
df["payment_date"] = pd.to_datetime(df["payment_date"])
df["invoice_date"] = pd.to_datetime(df["invoice_date"])

# 3. Calculate TARGET: payment_delay_days (Negative means paid early, positive means late)
df["payment_delay_days"] = (df["payment_date"] - df["due_date"]).dt.days

# 4. Map to the exact features the frontend/backend expects
df["invoice_amount"] = df["total_amount"]
df["days_until_due"] = (df["due_date"] - df["invoice_date"]).dt.days

# 5. Group by customer to calculate their history (The 'AI' aspect of predicting buyer variance!)
customer_stats = df.groupby("customer_id").agg(
    previous_avg_delay=("payment_delay_days", "mean"),
    customer_invoice_count=("invoice_id", "count")
).reset_index()

# Calculate late payments count per customer
late_payments = df[df["payment_delay_days"] > 0].groupby("customer_id").size().reset_index(name="previous_late_payments")
customer_stats = customer_stats.merge(late_payments, on="customer_id", how="left").fillna(0)

# Merge back into main dataframe
df = df.merge(customer_stats, on="customer_id", how="left")

# Drop any NaNs
df = df.dropna(subset=["invoice_amount", "days_until_due", "previous_avg_delay", "previous_late_payments", "customer_invoice_count", "payment_delay_days"])

FEATURES = [
    "invoice_amount",
    "days_until_due",
    "previous_avg_delay",
    "previous_late_payments",
    "customer_invoice_count"
]
X = df[FEATURES]
y = df["payment_delay_days"]

print(f" Training on {len(X)} records...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(" Training Random Forest Regressor (Using all CPU Cores)...")
model = RandomForestRegressor(n_estimators=100, max_depth=10, random_state=42, n_jobs=-1)
model.fit(X_train, y_train)

# Test accuracy
predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)
print(f" Model Accuracy: Predictions are off by an average of {mae:.2f} days.")

# Save model
os.makedirs("models", exist_ok=True)
model_path = os.path.join("models", "payment_delay_model.joblib")
joblib.dump(model, model_path)

print(f" SUCCESS! Model saved to {model_path}.")
print("The API is now fully operational and running on real data!")
