import os

file_path = r'D:\SIH2026\backend\main.py'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

cors_code = """
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
"""

if 'CORSMiddleware' not in text:
    # Insert right after app = FastAPI()
    text = text.replace('app = FastAPI()', 'app = FastAPI()\n' + cors_code)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print("CORS successfully added to FastAPI.")
else:
    print("CORS already configured.")
