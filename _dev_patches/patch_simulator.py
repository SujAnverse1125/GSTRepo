import re

file_path = "D:\\\\SIH2026\\\\frontend\\\\app\\\\dashboard\\\\page.tsx"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Add states
if "const [simulatedDelay, setSimulatedDelay] = useState(45);" not in content:
    content = content.replace("const [chartData, setChartData] = useState([]);", 
                              "const [baseChartData, setBaseChartData] = useState<any[]>([]);\n  const [chartData, setChartData] = useState<any[]>([]);\n  const [simulatedDelay, setSimulatedDelay] = useState(45);")

# Update fetch block
old_fetch = """      setChartData(data.projectedCashflow);"""
new_fetch = """      setBaseChartData(data.projectedCashflow);
      setChartData(data.projectedCashflow);"""
content = content.replace(old_fetch, new_fetch)

# Add handler function
handler_func = """
  const handleSimulationChange = (e: any) => {
    const newDelay = parseInt(e.target.value);
    setSimulatedDelay(newDelay);

    if (baseChartData.length > 0) {
      const morphedData = baseChartData.map((point: any) => {
        // Simple visual simulation: Drop balance between GST Day (20) and the new delay day
        if (point.day >= 20 && point.day < newDelay) {
          const drop = (newDelay - 20) * 15000; // Fake penalty calculation for visual effect
          return { ...point, balance: point.balance - drop, forecastLow: point.forecastLow - drop };
        }
        return point;
      });
      setChartData(morphedData);
    }
  };
"""
if "handleSimulationChange" not in content:
    content = content.replace("const startIngestion = async () => {", handler_func + "\n  const startIngestion = async () => {")

# Replace simulator HTML
old_sim = """<label className="flex justify-between text-sm font-bold uppercase tracking-wider text-white/80 mb-4">
                       <span>Simulate Buyer Payment Delay</span>
                       <span className="text-[#D0B063]">45 Days</span>
                     </label>
                     <input type="range" min="10" max="90" defaultValue="45" className="w-full h-2 bg-white/20 rounded-lg appearance-none cursor-pointer accent-[#D0B063]" />
                     <div className="flex justify-between text-xs text-white/40 mt-2">
                       <span>10 Days</span>
                       <span>90 Days</span>
                     </div>
                   </div>

                   <div className="p-4 rounded-xl bg-[#D0B063]/10 border border-[#D0B063]/20">
                     <p className="text-sm text-white/80">If buyer pays in 45 days, you face a <strong className="text-rose-400">₹2,000 cash deficit</strong> on Day 20.</p>
                   </div>
                   
                   <button className="w-full py-3 border border-[#D0B063] text-[#D0B063] rounded-xl font-bold hover:bg-[#D0B063]/10 transition-colors">
                     Run Simulation
                   </button>"""

new_sim = """<label className="flex justify-between text-sm font-bold uppercase tracking-wider text-white/80 mb-4">
                       <span>Simulate Buyer Payment Delay</span>
                       <span className="text-[#D0B063]">{simulatedDelay} Days</span>
                     </label>
                     <input 
                       type="range" min="10" max="90" 
                       value={simulatedDelay} 
                       onChange={handleSimulationChange}
                       className="w-full h-2 bg-white/20 rounded-lg appearance-none cursor-pointer accent-[#D0B063]" 
                     />
                     <div className="flex justify-between text-xs text-white/40 mt-2">
                       <span>10 Days</span>
                       <span>90 Days</span>
                     </div>
                   </div>

                   <div className="p-4 rounded-xl bg-[#D0B063]/10 border border-[#D0B063]/20 mt-4">
                     {simulatedDelay <= 20 ? (
                       <p className="text-sm text-white/80">If buyer pays in {simulatedDelay} days, <strong className="text-emerald-400">you avoid the GST liquidity trap!</strong> No financing needed.</p>
                     ) : (
                       <p className="text-sm text-white/80">If buyer pays in {simulatedDelay} days, you face a <strong className="text-rose-400">₹{((simulatedDelay - 20) * 15000).toLocaleString('en-IN')} cash deficit</strong>. Action required.</p>
                     )}
                   </div>
                   
                   <button onClick={() => alert("Simulation saved. AI Auto-finance adjusted.")} className="w-full py-3 border border-[#D0B063] text-[#D0B063] rounded-xl font-bold hover:bg-[#D0B063]/10 transition-colors mt-6">
                     Apply Simulation to Twin
                   </button>"""

content = content.replace(old_sim, new_sim)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Simulator logic injected.")
