/**
 * ML Engine API Service
 * 
 * Your ML team can connect the React frontend to the Python FastAPI ML backend here.
 * When the user moves the slider in the simulator, call `fetchMLLiquidityForecast`
 * instead of running the hardcoded math in React.
 */

export interface MLPredictionRequest {
  current_balance: number;
  slider_delay_days: number;
  revenue_shock: number;
  cost_shock: number;
}

export interface MLPredictionResponse {
  predicted_base_delay: number;
  forecast_90_days: number[];
  recommended_action: {
    action: string;
    confidence: number;
    amount_needed: number;
  };
}

export async function fetchMLLiquidityForecast(data: MLPredictionRequest): Promise<MLPredictionResponse | null> {
  try {
    const response = await fetch("/api/ml/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });

    if (!response.ok) {
      throw new Error("Failed to fetch ML forecast");
    }

    return await response.json();
  } catch (error) {
    console.error("ML Engine Error:", error);
    return null;
  }
}
