const fs = require('fs');

let text = fs.readFileSync('D:/SIH2026/frontend/app/lib/ml_service.ts', 'utf8');

const oldInterface = `interface MLPredictionRequest {
  current_balance: number;
  slider_delay_days: number;
}`;

const newInterface = `interface MLPredictionRequest {
  current_balance: number;
  slider_delay_days: number;
  revenue_shock: number;
  cost_shock: number;
}`;

text = text.replace(oldInterface, newInterface);
fs.writeFileSync('D:/SIH2026/frontend/app/lib/ml_service.ts', text, 'utf8');
console.log("ml_service.ts updated!");
