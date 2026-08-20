import os

file_path = r'D:\SIH2026\backend\main.py'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Add imports for ml endpoint
if 'from ml_model import ml_engine' not in text:
    text = 'from pydantic import BaseModel\nfrom ml_model import ml_engine\n' + text

endpoint_code = """
class MLPredictionRequest(BaseModel):
    current_balance: float
    slider_delay_days: int

@app.post("/api/ml/predict")
async def predict_liquidity(req: MLPredictionRequest):
    # 1. ML Model predicts the baseline delay from historical data
    # (Here we mock feature extraction)
    predicted_base_delay = ml_engine.predict_buyer_delay(None)
    
    # 2. ML Time-Series engine generates the 90 day curve based on the slider override
    forecast = ml_engine.generate_90_day_forecast(
        current_balance=req.current_balance,
        base_delay=predicted_base_delay,
        shock_scenario_delay=req.slider_delay_days
    )
    
    # 3. ML Action Matrix recommends an action
    action = ml_engine.recommend_action(forecast)
    
    return {
        "predicted_base_delay": predicted_base_delay,
        "forecast_90_days": forecast,
        "recommended_action": action
    }
"""

if '/api/ml/predict' not in text:
    text += '\n' + endpoint_code
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print('ML Endpoint added to FastAPI!')
else:
    print('Endpoint already exists.')
