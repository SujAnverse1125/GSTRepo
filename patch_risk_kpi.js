const fs = require('fs');
let text = fs.readFileSync('D:/SIH2026/frontend/app/dashboard/page.tsx', 'utf8');

// Update Shortfall Risk to dynamically use isSafe
const oldRisk = `<h3 className="text-3xl font-black text-white font-serif">Critical</h3>`;
const newRisk = `<h3 className={\`text-3xl font-black font-serif \${isSafe ? 'text-emerald-400' : 'text-rose-400'}\`}>{isSafe ? 'Stable' : 'Critical'}</h3>`;

text = text.replace(oldRisk, newRisk);

fs.writeFileSync('D:/SIH2026/frontend/app/dashboard/page.tsx', text, 'utf8');
console.log("Shortfall Risk KPI card is now dynamic!");
