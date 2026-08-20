const fs = require('fs');
let text = fs.readFileSync('D:/SIH2026/frontend/app/dashboard/page.tsx', 'utf8');

// Update the AVG BUYER DELAY KPI card to bind to the live slider state instead of the static baseline metric
text = text.replace(
  '<h3 className="text-3xl font-black font-serif">{metrics?.buyer_delay_days || 45} Days</h3>',
  '<h3 className="text-3xl font-black font-serif">{simulatedDelay} Days</h3>'
);

// Update the CASH CONVERSION CYCLE KPI card to also bind to the live slider state
text = text.replace(
  '<h3 className="text-3xl font-black font-serif">{metrics?.buyer_delay_days ? metrics.buyer_delay_days + 15 : 60} Days</h3>',
  '<h3 className="text-3xl font-black font-serif">{simulatedDelay + 15} Days</h3>'
);

fs.writeFileSync('D:/SIH2026/frontend/app/dashboard/page.tsx', text, 'utf8');
console.log("Bound KPI cards to the live simulatedDelay state");
