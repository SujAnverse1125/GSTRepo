const fs = require('fs');
let text = fs.readFileSync('D:/SIH2026/frontend/app/dashboard/page.tsx', 'utf8');

const oldCode = `      setMetrics({
        current_balance: data.summary.cashOnHand,
        gst_due: data.summary.gstDue,
        lowest_projected_balance: data.summary.minProjectedBalance,
        buyer_delay_days: 45
      });`;

const newCode = `      setMetrics({
        current_balance: data.summary.cashOnHand,
        gst_due: data.summary.gstDue,
        lowest_projected_balance: data.summary.minProjectedBalance,
        buyer_delay_days: data.summary.buyer_delay_days || 45
      });
      
      // Update the Digital Twin Simulator to start at the dynamic AI baseline!
      if (data.summary.buyer_delay_days) {
          setSimulatedDelay(data.summary.buyer_delay_days);
      }`;

text = text.replace(oldCode, newCode);
fs.writeFileSync('D:/SIH2026/frontend/app/dashboard/page.tsx', text, 'utf8');
console.log("Dashboard successfully patched for dynamic ML baseline!");
