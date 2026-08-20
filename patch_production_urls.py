import os

dashboard_path = 'D:/SIH2026/frontend/app/dashboard/page.tsx'
ml_path = 'D:/SIH2026/frontend/app/lib/ml_service.ts'

with open(dashboard_path, 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('"http://localhost:8000/api/upload"', '(process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000") + "/api/upload"')
text = text.replace('"http://localhost:8000/api/simulate"', '(process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000") + "/api/simulate"')

with open(dashboard_path, 'w', encoding='utf-8') as f:
    f.write(text)
    
with open(ml_path, 'r', encoding='utf-8') as f:
    text2 = f.read()

text2 = text2.replace('"http://localhost:8000/api/ml/predict"', '(process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000") + "/api/ml/predict"')

with open(ml_path, 'w', encoding='utf-8') as f:
    f.write(text2)

print("Updated API URLs to support production deployments!")
