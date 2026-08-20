import re

file_path = "D:\\\\SIH2026\\\\frontend\\\\app\\\\dashboard\\\\page.tsx"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# I will add a new section below the Chart area for the Invoice List and the Scenario Simulator.
# Let's locate the closing div of the grid containing the chart and the Auto-Finance action panel.

target = """          <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
            {/* Chart Area */}
            <div className="lg:col-span-2">
              <CashFlowChart data={chartData} />
            </div>

            {/* Auto-Finance Action Panel */}
            <div className="bg-white rounded-[2rem] border border-[#1A1C20]/10 shadow-sm p-8 flex flex-col justify-between">"""

new_interactive_section = """
          {/* Interactive Tools & Tables */}
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 mt-8">
            {/* Live Invoice Sync Table */}
            <div className="bg-white rounded-[2rem] border border-[#1A1C20]/10 shadow-sm p-8">
              <h3 className="text-2xl font-black font-serif mb-6 text-[#1A1C20]">Account Aggregator Data</h3>
              <div className="overflow-x-auto">
                <table className="w-full text-left border-collapse">
                  <thead>
                    <tr className="border-b border-[#1A1C20]/10">
                      <th className="py-3 text-sm font-bold text-[#1A1C20]/50 uppercase tracking-wider">Source</th>
                      <th className="py-3 text-sm font-bold text-[#1A1C20]/50 uppercase tracking-wider">Amount</th>
                      <th className="py-3 text-sm font-bold text-[#1A1C20]/50 uppercase tracking-wider">Status</th>
                      <th className="py-3 text-sm font-bold text-[#1A1C20]/50 uppercase tracking-wider text-right">AI Prediction</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-[#1A1C20]/5">
                    <tr className="hover:bg-[#F2EFE9]/30 transition-colors">
                      <td className="py-4 font-bold text-[#1A1C20]">GSTN Inv #1042</td>
                      <td className="py-4 text-[#1A1C20]/80">₹1,00,000</td>
                      <td className="py-4"><span className="px-2 py-1 bg-amber-100 text-amber-700 text-xs font-bold rounded-full">Unpaid</span></td>
                      <td className="py-4 text-right text-rose-600 font-bold">Delayed (Day 45)</td>
                    </tr>
                    <tr className="hover:bg-[#F2EFE9]/30 transition-colors">
                      <td className="py-4 font-bold text-[#1A1C20]">SBI Bank Statement</td>
                      <td className="py-4 text-[#1A1C20]/80">-₹18,000</td>
                      <td className="py-4"><span className="px-2 py-1 bg-rose-100 text-rose-700 text-xs font-bold rounded-full">Tax Due</span></td>
                      <td className="py-4 text-right text-[#1A1C20]/80 font-bold">Day 20</td>
                    </tr>
                    <tr className="hover:bg-[#F2EFE9]/30 transition-colors">
                      <td className="py-4 font-bold text-[#1A1C20]">GSTN Inv #1041</td>
                      <td className="py-4 text-[#1A1C20]/80">₹45,000</td>
                      <td className="py-4"><span className="px-2 py-1 bg-emerald-100 text-emerald-700 text-xs font-bold rounded-full">Settled</span></td>
                      <td className="py-4 text-right text-emerald-600 font-bold">Paid on time</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>

            {/* Scenario Simulator */}
            <div className="bg-[#1A1C20] rounded-[2rem] shadow-xl p-8 text-white relative overflow-hidden">
               <div className="absolute top-0 right-0 w-64 h-64 bg-[#D0B063]/10 rounded-full blur-3xl pointer-events-none"></div>
               <div className="relative z-10">
                 <h3 className="text-2xl font-black font-serif mb-2 text-[#D0B063]">Digital Twin Simulator</h3>
                 <p className="text-white/60 mb-8">Move the slider to simulate alternate realities and see how it impacts your liquidity.</p>
                 
                 <div className="space-y-6">
                   <div>
                     <label className="flex justify-between text-sm font-bold uppercase tracking-wider text-white/80 mb-4">
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
                   </button>
                 </div>
               </div>
            </div>
          </div>
"""

content = content.replace('          </div>\n        </div>\n      )}\n    </div>', '          </div>\n' + new_interactive_section + '        </div>\n      )}\n    </div>')

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Added interactive sections successfully.")
