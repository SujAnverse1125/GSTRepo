const fs = require('fs');
let text = fs.readFileSync('D:/SIH2026/frontend/app/dashboard/page.tsx', 'utf8');

// Replace the * 20000 scaling which ruins raw balances
const oldMap = `const morphedData = mlData.forecast_90_days.map((val: number, idx: number) => ({
            day: idx + 1,
            balance: val * 20000,
            forecastLow: val * 18000
          }));`;

const newMap = `const morphedData = mlData.forecast_90_days.map((val: number, idx: number) => ({
            day: idx + 1,
            balance: val,
            forecastLow: val * 0.9
          }));`;

text = text.replace(oldMap, newMap);

fs.writeFileSync('D:/SIH2026/frontend/app/dashboard/page.tsx', text, 'utf8');
console.log("Fixed dashboard graph scaling");
