const fs = require('fs');
const path = require('path');

const file = path.join('D:', 'SIH2026', 'frontend', 'app', 'page.tsx');
let text = fs.readFileSync(file, 'utf8');

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

// Insert the state logic right after "export default function LandingPage() {"
text = text.replace(/export default function LandingPage\(\) \{\s*return \(/, 'export default function LandingPage() {\n' + stateLogic + '\n  return (');

fs.writeFileSync(file, text, 'utf8');
console.log("State logic injected!");
