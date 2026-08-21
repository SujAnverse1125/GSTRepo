const fs = require('fs');
let text = fs.readFileSync('D:/SIH2026/frontend/app/dashboard/page.tsx', 'utf8');

// Inside fetchML, update the metrics state with the lowest projected balance!
const oldSetChartData = `setChartData(morphedData);`;
const newSetChartData = `setChartData(morphedData);\n          setMetrics(prev => ({ ...prev, current_balance: Math.min(...mlData.forecast_90_days) }));`;

text = text.replace(oldSetChartData, newSetChartData);

// Let's also change the translation dictionary so it makes more sense why it's changing
text = text.replace('current_balance: "Current Balance"', 'current_balance: "Projected Low"');

fs.writeFileSync('D:/SIH2026/frontend/app/dashboard/page.tsx', text, 'utf8');
console.log("Current Balance card is now dynamic Projected Low!");
