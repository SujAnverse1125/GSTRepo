import re

file_path = "D:\\\\SIH2026\\\\frontend\\\\app\\\\dashboard\\\\page.tsx"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add new state variables for the advanced simulator
old_state = "const [simulatedDelay, setSimulatedDelay] = useState(45);"
new_state = """const [simulatedDelay, setSimulatedDelay] = useState(45);
  const [revenueShock, setRevenueShock] = useState(0);
  const [costShock, setCostShock] = useState(0);"""
if "const [revenueShock" not in content:
    content = content.replace(old_state, new_state)

# 2. Update the dynamic Deficit Calculation inside the component body
# We'll calculate a local 'totalDeficit' variable inside the render so both the chart and the comparator can use it
calc_logic = """
  // Dynamic Deficit Calculation
  const delayPenalty = simulatedDelay > 20 ? (simulatedDelay - 20) * 1500 : 0;
  const revenuePenalty = revenueShock * 5000;
  const costPenalty = costShock * 3000;
  const totalDeficit = delayPenalty + revenuePenalty + costPenalty;
  const isSafe = totalDeficit === 0;
"""
if "// Dynamic Deficit Calculation" not in content:
    content = content.replace("const router = useRouter();", "const router = useRouter();\n" + calc_logic)

# 3. Update the Simulator UI
old_simulator = """<div className="space-y-6">
                   <div>
                     <label className="flex justify-between text-sm font-bold uppercase tracking-wider text-white/80 mb-4">
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
                   </button>
                 </div>"""

new_simulator = """<div className="space-y-6">
                   {/* Delay Slider */}
                   <div>
                     <label className="flex justify-between text-sm font-bold uppercase tracking-wider text-white/80 mb-2">
                       <span>Buyer Payment Delay</span>
                       <span className="text-[#D0B063]">{simulatedDelay} Days</span>
                     </label>
                     <input 
                       type="range" min="10" max="90" 
                       value={simulatedDelay} 
                       onChange={handleSimulationChange}
                       className="w-full h-2 bg-white/20 rounded-lg appearance-none cursor-pointer accent-[#D0B063]" 
                     />
                   </div>

                   {/* Revenue Drop Slider */}
                   <div>
                     <label className="flex justify-between text-sm font-bold uppercase tracking-wider text-white/80 mb-2">
                       <span>Revenue Drop Shock</span>
                       <span className="text-[#D0B063]">{revenueShock}%</span>
                     </label>
                     <input 
                       type="range" min="0" max="50" 
                       value={revenueShock} 
                       onChange={(e) => setRevenueShock(parseInt(e.target.value))}
                       className="w-full h-2 bg-white/20 rounded-lg appearance-none cursor-pointer accent-[#D0B063]" 
                     />
                   </div>

                   {/* Cost Spike Slider */}
                   <div>
                     <label className="flex justify-between text-sm font-bold uppercase tracking-wider text-white/80 mb-2">
                       <span>Material Cost Spike</span>
                       <span className="text-[#D0B063]">{costShock}%</span>
                     </label>
                     <input 
                       type="range" min="0" max="50" 
                       value={costShock} 
                       onChange={(e) => setCostShock(parseInt(e.target.value))}
                       className="w-full h-2 bg-white/20 rounded-lg appearance-none cursor-pointer accent-[#D0B063]" 
                     />
                   </div>

                   {/* Live Deficit Warning */}
                   <div className="p-4 rounded-xl bg-[#D0B063]/10 border border-[#D0B063]/20 mt-4">
                     {isSafe ? (
                       <p className="text-sm text-white/80"><strong className="text-emerald-400">Cash Flow Positive!</strong> You safely avoid the GST trap under these conditions.</p>
                     ) : (
                       <p className="text-sm text-white/80">Under these parameters, you face a <strong className="text-rose-400 text-lg">₹{totalDeficit.toLocaleString('en-IN')}</strong> cash deficit. AI solutions generated.</p>
                     )}
                   </div>
                 </div>"""

content = content.replace(old_simulator, new_simulator)

# 4. Replace the old Auto-Finance Panel with the new 4-Option Comparator
old_action_panel = """            {/* Auto-Finance Action Panel */}
            <div className="bg-white rounded-[2rem] border border-[#1A1C20]/10 shadow-sm p-8 flex flex-col justify-between">
              <div>
                <div className="inline-flex items-center gap-2 px-3 py-1 bg-rose-50 border border-rose-200 text-rose-700 text-xs font-bold rounded-full mb-6 uppercase tracking-wider">
                  <FileWarning className="w-4 h-4" /> GST Liability Tracker
                </div>
                <h3 className="text-2xl font-black font-serif mb-4">Liquidity Paradox Detected</h3>
                <p className="text-[#1A1C20]/70 mb-8 leading-relaxed">
                  The AI predicts your ₹{metrics?.gst_due?.toLocaleString('en-IN') || "18,000"} GST payment is due on Day 20, but buyer payment is delayed until Day {metrics?.buyer_delay_days || 45}. 
                  You will hit a cash deficit of <strong className="text-rose-600">₹{Math.abs(metrics?.lowest_projected_balance || -2000).toLocaleString('en-IN')}</strong>.
                </p>
              </div>

              <div className="space-y-4">
                <div className="p-5 rounded-2xl bg-[#F2EFE9] border border-[#1A1C20]/10">
                  <h4 className="font-bold mb-1">Pre-Approved Invoice Discounting</h4>
                  <p className="text-sm text-[#1A1C20]/60 mb-4">Bridge the gap instantly. 1.5% fee.</p>
                  <button className="w-full py-4 bg-[#D0B063] text-[#1A1C20] rounded-xl font-bold hover:bg-[#E3C376] transition-all shadow-md">
                    Discount Invoice for ₹1,00,000
                  </button>
                </div>
              </div>
            </div>"""

new_action_panel = """            {/* Debt vs Non-Debt Comparator Matrix */}
            <div className="bg-white rounded-[2rem] border border-[#1A1C20]/10 shadow-sm p-8 flex flex-col h-full">
              <div className="mb-6">
                <div className="inline-flex items-center gap-2 px-3 py-1 bg-[#1A1C20] text-white text-xs font-bold rounded-full mb-4 uppercase tracking-wider">
                  <ShieldCheck className="w-4 h-4 text-[#D0B063]" /> AI Action Matrix
                </div>
                <h3 className="text-2xl font-black font-serif mb-2 text-[#1A1C20]">Resolution Comparator</h3>
                <p className="text-[#1A1C20]/70 text-sm">
                  {isSafe ? "Your cash flow is stable. No financing required right now." : `We detected a ₹${totalDeficit.toLocaleString('en-IN')} deficit. Compare your options to bridge the gap:`}
                </p>
              </div>

              {!isSafe && (
                <div className="space-y-3 overflow-y-auto pr-2 custom-scrollbar flex-1">
                  
                  {/* Option 1: AI Recommended */}
                  <div className="p-4 rounded-xl border-2 border-[#D0B063] bg-[#D0B063]/5 relative">
                    <div className="absolute -top-3 right-4 bg-[#D0B063] text-[#1A1C20] text-[10px] font-black uppercase tracking-wider px-3 py-1 rounded-full shadow-sm">
                      ✨ AI Recommended (Non-Debt)
                    </div>
                    <div className="flex justify-between items-start mb-2 mt-2">
                      <h4 className="font-bold text-[#1A1C20]">Offer 2% Early Discount</h4>
                      <span className="text-sm font-bold text-rose-600">Cost: ₹{Math.round(totalDeficit * 0.02).toLocaleString('en-IN')}</span>
                    </div>
                    <p className="text-xs text-[#1A1C20]/60 mb-3">Instead of a loan, offer Tata Electronics a 2% discount to pay today. Fastest & cheapest.</p>
                    <button className="w-full py-2.5 bg-[#1A1C20] text-white text-sm rounded-lg font-bold hover:bg-[#2D3139] transition-all">Send Discount Offer</button>
                  </div>

                  {/* Option 2: Invoice Discounting */}
                  <div className="p-4 rounded-xl border border-[#1A1C20]/10 bg-white hover:border-[#D0B063]/50 transition-colors">
                    <div className="flex justify-between items-start mb-2">
                      <h4 className="font-bold text-[#1A1C20]">Invoice Discounting (Debt)</h4>
                      <span className="text-sm font-bold text-rose-600">Cost: ₹{Math.round(totalDeficit * 0.015).toLocaleString('en-IN')}</span>
                    </div>
                    <p className="text-xs text-[#1A1C20]/60 mb-3">Bank advances 80% of invoice today at 1.5% monthly fee.</p>
                    <button className="w-full py-2 border border-[#1A1C20]/20 text-[#1A1C20] text-sm rounded-lg font-bold hover:bg-[#F2EFE9] transition-all">Select</button>
                  </div>

                  {/* Option 3: Do Nothing */}
                  <div className="p-4 rounded-xl border border-rose-200 bg-rose-50/30">
                    <div className="flex justify-between items-start mb-2">
                      <h4 className="font-bold text-[#1A1C20]">Do Nothing (Miss Tax)</h4>
                      <span className="text-sm font-bold text-rose-600">Cost: ₹{Math.round(totalDeficit * 0.05).toLocaleString('en-IN')}</span>
                    </div>
                    <p className="text-xs text-[#1A1C20]/60 mb-3">Wait for buyer. Pay 18% GST interest + ₹50/day late penalty.</p>
                    <button className="w-full py-2 border border-rose-200 text-rose-600 text-sm rounded-lg font-bold hover:bg-rose-100 transition-all">Select</button>
                  </div>

                </div>
              )}
            </div>"""

content = content.replace(old_action_panel, new_action_panel)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Advanced simulator and Comparator patched.")
