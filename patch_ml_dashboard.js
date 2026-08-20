const fs = require('fs');
const path = require('path');

const file = path.join('D:', 'SIH2026', 'frontend', 'app', 'dashboard', 'page.tsx');
let text = fs.readFileSync(file, 'utf8');

// Add import
if (!text.includes('fetchMLLiquidityForecast')) {
  text = text.replace('import Link from "next/link";', 'import Link from "next/link";\nimport { fetchMLLiquidityForecast } from "../lib/ml_service";');
}

// Replace handleSimulationChange
const oldHandler = `  const handleSimulationChange = (e: any) => {
    const newDelay = parseInt(e.target.value);
    setSimulatedDelay(newDelay);

    if (baseChartData.length > 0) {
      const morphedData = baseChartData.map((point: any) => {
        // Simple visual simulation: Drop balance between GST Day (20) and the new delay day
        if (point.day >= 20 && point.day < newDelay) {
          const drop = (newDelay - 20) * 15000; // Fake penalty calculation for visual effect
          return { ...point, balance: point.balance - drop, forecastLow: point.forecastLow - drop };
        }
        return point;
      });
      setChartData(morphedData);
    }
  };`;

const newHandler = `  const handleSimulationChange = async (e: any) => {
    const newDelay = parseInt(e.target.value);
    setSimulatedDelay(newDelay);

    // AI ML Engine Integration
    try {
      const mlData = await fetchMLLiquidityForecast({
        current_balance: metrics?.current_balance || 1500000,
        slider_delay_days: newDelay
      });

      if (mlData && mlData.forecast_90_days) {
        // We map the raw ML 90-day integer array back into the chart's object format
        const morphedData = mlData.forecast_90_days.map((val: number, idx: number) => ({
          day: idx + 1,
          balance: val * 20000, // Denormalize the ML array for display scale
          forecastLow: val * 18000
        }));
        
        // If Action Matrix detects a critical change, update the UI (Wait, just charting for now)
        setChartData(morphedData);
      }
    } catch (err) {
      console.error("ML Integration Error:", err);
    }
  };`;

text = text.replace(oldHandler, newHandler);

fs.writeFileSync(file, text, 'utf8');
console.log("ML Hook injected into Dashboard");
