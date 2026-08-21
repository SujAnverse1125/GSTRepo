import os
import re

file_path = r'D:\SIH2026\backend\main.py'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update MLPredictionRequest model
old_model = """class MLPredictionRequest(BaseModel):
    current_balance: float
    slider_delay_days: int"""

new_model = """class MLPredictionRequest(BaseModel):
    current_balance: float
    slider_delay_days: int
    revenue_shock: float = 0.0
    cost_shock: float = 0.0"""

text = text.replace(old_model, new_model)

# 2. Update predict_liquidity endpoint
old_endpoint = """    forecast = ml_engine.generate_90_day_forecast(
        current_balance=req.current_balance,
        base_delay=predicted_base_delay,
        shock_scenario_delay=req.slider_delay_days
    )"""

new_endpoint = """    forecast = ml_engine.generate_90_day_forecast(
        current_balance=req.current_balance,
        base_delay=predicted_base_delay,
        shock_scenario_delay=req.slider_delay_days,
        revenue_shock=req.revenue_shock,
        cost_shock=req.cost_shock
    )"""

text = text.replace(old_endpoint, new_endpoint)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)
print("main.py updated to handle all 3 sliders!")
