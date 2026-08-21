import re

file_path = "D:\\SIH2026\\frontend\\app\\lib\\ml_service.ts"

with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

# Replace the exposed API call with a secure relative call
text = text.replace(
    'const response = await fetch((process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000") + "/api/ml/predict"',
    'const response = await fetch("/api/ml/predict"'
)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Updated ml_service to use secure proxy")
