const fs = require('fs');
let text = fs.readFileSync('D:/SIH2026/frontend/app/dashboard/page.tsx', 'utf8');

// 1. Fix the missing import!
if (!text.includes('import { fetchMLLiquidityForecast }')) {
  text = text.replace('import CashFlowChart from \'../components/CashFlowChart\';', 'import CashFlowChart from \'../components/CashFlowChart\';\nimport { fetchMLLiquidityForecast } from \'../lib/ml_service\';');
}

// 2. Fix the label rendering so the X-Axis shows up
const oldMap = `const morphedData = mlData.forecast_90_days.map((val: number, idx: number) => ({
            day: idx + 1,
            balance: val,
            forecastLow: val * 0.9
          }));`;

const newMap = `const morphedData = mlData.forecast_90_days.map((val: number, idx: number) => ({
            day: idx + 1,
            label: 'D' + (idx + 1),
            balance: val,
            forecastLow: val * 0.9,
            forecastHigh: val * 1.1
          }));`;

text = text.replace(oldMap, newMap);

fs.writeFileSync('D:/SIH2026/frontend/app/dashboard/page.tsx', text, 'utf8');
console.log("Fixed import and labels!");
