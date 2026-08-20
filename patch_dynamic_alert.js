const fs = require('fs');
const path = require('path');

const file = path.join('D:', 'SIH2026', 'frontend', 'app', 'page.tsx');
let text = fs.readFileSync(file, 'utf8');

// 1. Add "use client" and imports
if (!text.includes('"use client"')) {
  text = '"use client";\nimport { useState, useEffect } from "react";\n' + text;
}

// 2. Insert state into LandingPage function
const stateLogic = `
  const alerts = [
    {
      type: "bad",
      title: "GST Deficit Predicted",
      desc: "A ₹2.5L shortfall is expected on Day 18 due to Buyer Delay.",
      icon: <FileWarning className="w-5 h-5" />,
      colors: "bg-rose-500/10 border-rose-500/20 text-rose-400",
      iconBg: "bg-rose-500/20"
    },
    {
      type: "good",
      title: "Inflow Cleared",
      desc: "L&T invoice #9042 settled. Cash buffer increased by ₹1.2L.",
      icon: <CheckCircle2 className="w-5 h-5" />,
      colors: "bg-emerald-500/10 border-emerald-500/20 text-emerald-400",
      iconBg: "bg-emerald-500/20"
    },
    {
      type: "warning",
      title: "Concentration Risk",
      desc: "Reliance Retail accounts for 68% of your current receivables.",
      icon: <Activity className="w-5 h-5" />,
      colors: "bg-amber-500/10 border-amber-500/20 text-amber-400",
      iconBg: "bg-amber-500/20"
    }
  ];
  const [alertIdx, setAlertIdx] = useState(0);
  useEffect(() => {
    const int = setInterval(() => {
      setAlertIdx((prev) => (prev + 1) % alerts.length);
    }, 4000);
    return () => clearInterval(int);
  }, []);
`;

if (!text.includes('const [alertIdx, setAlertIdx]')) {
  text = text.replace('export default function LandingPage() {\n  return (', 'export default function LandingPage() {' + stateLogic + '\n  return (');
}

// 3. Replace the static alert card
const staticAlertStart = text.indexOf('{/* Alert Card */}');
const staticAlertEnd = text.indexOf('</div>', text.indexOf('</div>', text.indexOf('</div>', staticAlertStart) + 1) + 1) + 6;

const dynamicAlert = `{/* Dynamic Alert Card */}
              <div className={\`transition-colors duration-500 border rounded-xl p-4 flex items-start gap-4 \${alerts[alertIdx].colors}\`}>
                <div className={\`p-2 rounded-lg mt-1 \${alerts[alertIdx].iconBg}\`}>
                  {alerts[alertIdx].icon}
                </div>
                <div className="transition-opacity duration-500 animate-in fade-in" key={alertIdx}>
                  <p className="font-bold text-sm">{alerts[alertIdx].title}</p>
                  <p className="opacity-70 text-xs mt-1">{alerts[alertIdx].desc}</p>
                </div>
              </div>`;

if (staticAlertStart !== -1 && staticAlertEnd !== -1 && !text.includes('{/* Dynamic Alert Card */}')) {
  text = text.substring(0, staticAlertStart) + dynamicAlert + text.substring(staticAlertEnd);
}

fs.writeFileSync(file, text, 'utf8');
console.log("Dynamic alerts injected!");
