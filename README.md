# 🎯 MSME Digital Twin
**AI-Powered Cash Flow Predictor & GST Liquidity Savior**

![Digital Twin Concept](https://img.shields.io/badge/Status-Hackathon_Ready-emerald?style=for-the-badge)
![Tech Stack](https://img.shields.io/badge/Stack-Next.js_|_FastAPI_|_Python_ML-blue?style=for-the-badge)

## 🚨 The Problem: The GST Liquidity Paradox
Indian MSMEs are trapped in a lethal cycle. When an MSME raises an invoice for ₹1 Lakh, they are forced to pay 18% GST to the government almost immediately out of their own pocket. However, large corporate buyers often take **90 to 120 days** to actually settle the invoice. 

This creates a massive "liquidity crater" where profitable businesses go bankrupt simply because their cash is trapped in pending receivables. Traditional banking dashboards only show the past—they don't warn MSMEs about the upcoming crunch.

## 💡 Our Solution
**MSME Twin** is a forward-looking financial command center that acts as an AI CFO for small businesses. By securely connecting to banking data via the RBI **Account Aggregator** framework, it builds a 90-day predictive model of your cash flow.

### ✨ Key Features
- **🔮 90-Day Liquidity Map:** A live, dynamic chart predicting your exact cash balance every day for the next 3 months.
- **🤖 Buyer Variance AI:** Uses machine learning (Standard Deviation & Z-Scores) to learn exactly how late specific buyers usually pay, dynamically adjusting your cash flow projections.
- **⚠️ Concentration Risk Alerts:** Automatically scans your receivables and warns you if too much of your cash is tied up with a single risky buyer.
- **⚡ AI Action Matrix:** When a GST deficit is predicted, the AI instantly offers actionable solutions, such as 1-click invoice discounting (TReDS integration) to bridge the gap before you default.
- **🔒 Privacy First:** Strict Sahamati Account Aggregator compliance. We predict, and then we delete. Zero persistent data retention.

---

## 🛠️ Tech Stack
* **Frontend:** Next.js (React), Tailwind CSS, Lucide Icons, Recharts
* **Backend:** Python, FastAPI, Uvicorn
* **AI/ML Engine:** Scikit-Learn, Pandas, Joblib (Random Forest & Variance Modeling)
* **Auth:** Supabase (Sandbox/Mocked for Demo)

---

## 🚀 Running the Project Locally

Because this project uses both a React frontend and a Python Machine Learning backend, you need to run both servers simultaneously.

### 1. Start the ML Backend (FastAPI)
```bash
cd backend
# Create and activate your virtual environment (recommended)
python -m venv .venv
.venv\Scripts\activate  # (Windows)
# source .venv/bin/activate (Mac/Linux)

pip install -r requirements.txt
python -m uvicorn main:app --reload --port 8000
```
*The backend will now be running on `http://localhost:8000`*

### 2. Start the Frontend (Next.js)
Open a **new** terminal window:
```bash
cd frontend
npm install
npm run dev
```
*The frontend will now be running on `http://localhost:3000`*

### 3. Launch the Demo
Open your browser and navigate to `http://localhost:3000`. 
Click **"Launch Demo"**, enter any 10-digit number (e.g. `00000 00000`) and bypass the OTP to instantly enter the Twin Dashboard. Use the AI simulators on the right to dynamically stress-test your cash flow!

---
*Built for SIH 2026* 🚀
