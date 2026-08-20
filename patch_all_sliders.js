const fs = require('fs');
let text = fs.readFileSync('D:/SIH2026/frontend/app/dashboard/page.tsx', 'utf8');

// 1. We need to add a useEffect to automatically trigger ML fetch when any of the 3 sliders change
const useEffectHook = `  useEffect(() => {
    if (appState !== 'dashboard') return;
    const fetchML = async () => {
      try {
        const mlData = await fetchMLLiquidityForecast({
          current_balance: metrics?.current_balance || 1500000,
          slider_delay_days: simulatedDelay,
          revenue_shock: revenueShock,
          cost_shock: costShock
        });

        if (mlData && mlData.forecast_90_days) {
          const morphedData = mlData.forecast_90_days.map((val: number, idx: number) => ({
            day: idx + 1,
            balance: val * 20000,
            forecastLow: val * 18000
          }));
          setChartData(morphedData);
        }
      } catch (err) {
        console.error("ML Integration Error:", err);
      }
    };
    fetchML();
  }, [simulatedDelay, revenueShock, costShock, appState]);`;

if (!text.includes('const fetchML = async () => {')) {
    text = text.replace('const [tredsStatus, setTredsStatus] = useState("loading");', 'const [tredsStatus, setTredsStatus] = useState("loading");\n\n' + useEffectHook);
}

// 2. Remove the old handleSimulationChange call from the slider onChange
text = text.replace('onChange={handleSimulationChange}', 'onChange={(e) => setSimulatedDelay(parseInt(e.target.value))}');

fs.writeFileSync('D:/SIH2026/frontend/app/dashboard/page.tsx', text, 'utf8');
console.log("dashboard updated to react to all 3 sliders!");
