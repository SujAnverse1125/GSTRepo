const fs = require('fs');
let text = fs.readFileSync('D:/SIH2026/frontend/app/dashboard/page.tsx', 'utf8');

const effectBlock = `  useEffect(() => {
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

// 1. Remove the old effect
text = text.replace(effectBlock, '');
// Clean up any double empty lines that might have been left
text = text.replace(/\n\s*\n\s*\n/g, '\n\n');

// 2. Add it back after costShock
const costShockLine = `const [costShock, setCostShock] = useState(0);`;
text = text.replace(costShockLine, costShockLine + '\n\n' + effectBlock);

fs.writeFileSync('D:/SIH2026/frontend/app/dashboard/page.tsx', text, 'utf8');
console.log("Moved useEffect to prevent TDZ ReferenceError!");
