import kagglehub
import os
import shutil

print("Downloading dataset...")
path = kagglehub.dataset_download("tharishreddy22/global-b2b-invoice-and-payments-dataset")
print("Downloaded to:", path)

# The dataset contains train_invoices.csv (we'll use this)
train_csv_path = os.path.join(path, "train_invoices.csv")

# Destination path in our backend
target_dir = r"D:\SIH2026\backend\data"
if not os.path.exists(target_dir):
    os.makedirs(target_dir)

target_csv_path = os.path.join(target_dir, "payment_history.csv")

if os.path.exists(train_csv_path):
    print(f"Moving {train_csv_path} to {target_csv_path}...")
    shutil.copy2(train_csv_path, target_csv_path)
    print("Dataset successfully installed in the backend!")
else:
    print("Could not find train_invoices.csv in the downloaded dataset.")
