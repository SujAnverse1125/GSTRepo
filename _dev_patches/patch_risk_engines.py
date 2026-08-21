import re

file_path = "D:\\\\SIH2026\\\\frontend\\\\app\\\\dashboard\\\\page.tsx"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update the Tour to mention the Liability Tracker & Risk Engines
old_tour_3 = """                 {tourStep === 3 && (
                   <div className="animate-in fade-in slide-in-from-right-4">
                     <div className="w-16 h-16 rounded-2xl bg-emerald-100 flex items-center justify-center text-emerald-600 mb-6">
                       <Zap className="w-8 h-8" />
                     </div>
                     <h3 className="text-2xl font-black font-serif mb-3 text-[#1A1C20]">1-Click Auto-Finance</h3>
                     <p className="text-[#1A1C20]/70 text-lg leading-relaxed mb-8">
                       If the AI predicts you will run out of cash before a GST deadline, it automatically surfaces pre-approved invoice discounting options. You're protected.
                     </p>
                     <button onClick={() => setShowTour(false)} className="w-full py-4 bg-[#D0B063] text-[#1A1C20] rounded-xl font-bold hover:bg-[#E3C376] transition-all">Enter Command Center</button>
                   </div>
                 )}"""

new_tour_3 = """                 {tourStep === 3 && (
                   <div className="animate-in fade-in slide-in-from-right-4">
                     <div className="w-16 h-16 rounded-2xl bg-[#D0B063]/20 flex items-center justify-center text-[#D0B063] mb-6">
                       <ShieldCheck className="w-8 h-8" />
                     </div>
                     <h3 className="text-2xl font-black font-serif mb-3 text-[#1A1C20]">Risk & Liability Engines</h3>
                     <p className="text-[#1A1C20]/70 text-lg leading-relaxed mb-8">
                       Your dashboard includes a dedicated <strong>GST Liability Tracker</strong>, a <strong>Concentration Risk</strong> analyzer, and a <strong>Seasonal Pattern Detector</strong> to guard against hidden cash traps.
                     </p>
                     <button onClick={() => setShowTour(false)} className="w-full py-4 bg-[#1A1C20] text-white rounded-xl font-bold hover:bg-[#2D3139] transition-all">Enter Command Center</button>
                   </div>
                 )}"""
content = content.replace(old_tour_3, new_tour_3)

# 2. Rename the Paradox panel to be explicitly the GST Liability Tracker
old_action_panel = """                <div className="inline-flex items-center gap-2 px-3 py-1 bg-rose-50 border border-rose-200 text-rose-700 text-xs font-bold rounded-full mb-6 uppercase tracking-wider">
                  <Activity className="w-4 h-4" /> Action Required
                </div>
                <h3 className="text-2xl font-black font-serif mb-4">GST Liquidity Paradox Detected</h3>"""

new_action_panel = """                <div className="inline-flex items-center gap-2 px-3 py-1 bg-rose-50 border border-rose-200 text-rose-700 text-xs font-bold rounded-full mb-6 uppercase tracking-wider">
                  <FileWarning className="w-4 h-4" /> GST Liability Tracker
                </div>
                <h3 className="text-2xl font-black font-serif mb-4">Liquidity Paradox Detected</h3>"""
content = content.replace(old_action_panel, new_action_panel)

# 3. Inject Concentration Risk & Seasonal Detectors
target_end_of_grid = """          {/* Interactive Tools & Tables */}"""

new_risk_engines = """          {/* AI Risk Engines */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-8 mb-8">
            {/* Concentration Risk */}
            <div className="bg-white rounded-[2rem] border border-[#1A1C20]/10 shadow-sm p-8">
              <div className="flex items-center justify-between mb-6">
                <h3 className="text-xl font-black font-serif text-[#1A1C20]">Concentration Risk Engine</h3>
                <span className="px-3 py-1 bg-rose-100 text-rose-700 text-xs font-bold rounded-full">High Risk</span>
              </div>
              <p className="text-[#1A1C20]/60 text-sm mb-6">AI analysis of your Account Aggregator data shows dangerous reliance on a single buyer.</p>
              
              <div className="space-y-5">
                <div>
                  <div className="flex justify-between text-sm font-bold mb-2">
                    <span className="text-[#1A1C20]">Reliance Retail Ltd.</span>
                    <span className="text-rose-600">68% of Receivables</span>
                  </div>
                  <div className="w-full h-3 bg-[#F2EFE9] rounded-full overflow-hidden">
                    <div className="h-full bg-rose-500 rounded-full" style={{ width: '68%' }}></div>
                  </div>
                </div>
                
                <div>
                  <div className="flex justify-between text-sm font-bold mb-2">
                    <span className="text-[#1A1C20]">Tata Electronics</span>
                    <span className="text-[#D0B063]">22% of Receivables</span>
                  </div>
                  <div className="w-full h-3 bg-[#F2EFE9] rounded-full overflow-hidden">
                    <div className="h-full bg-[#D0B063] rounded-full" style={{ width: '22%' }}></div>
                  </div>
                </div>

                <div>
                  <div className="flex justify-between text-sm font-bold mb-2">
                    <span className="text-[#1A1C20]">Other SMEs</span>
                    <span className="text-emerald-500">10% of Receivables</span>
                  </div>
                  <div className="w-full h-3 bg-[#F2EFE9] rounded-full overflow-hidden">
                    <div className="h-full bg-emerald-500 rounded-full" style={{ width: '10%' }}></div>
                  </div>
                </div>
              </div>
            </div>

            {/* Seasonal Pattern Detector */}
            <div className="bg-white rounded-[2rem] border border-[#1A1C20]/10 shadow-sm p-8 flex flex-col justify-center">
              <div className="flex items-center justify-between mb-6">
                <h3 className="text-xl font-black font-serif text-[#1A1C20]">Seasonal Pattern Detector</h3>
                <Activity className="w-6 h-6 text-[#D0B063]" />
              </div>
              <div className="p-5 rounded-2xl bg-[#D0B063]/10 border border-[#D0B063]/20 mb-6">
                <h4 className="font-bold text-[#1A1C20] mb-2 flex items-center gap-2">
                  <Database className="w-4 h-4 text-[#D0B063]" /> Historical Dip Detected
                </h4>
                <p className="text-[#1A1C20]/70 text-sm leading-relaxed">
                  Fast Fourier Transform (FFT) analysis of your past 3 years reveals a recurring <strong>15% revenue drop every September</strong> (Post-Monsoon slump).
                </p>
              </div>
              <p className="text-sm font-bold text-[#1A1C20]/60">
                ✓ The 90-Day Twin Engine has automatically factored this seasonal variance into your cash flow projection above.
              </p>
            </div>
          </div>

          {/* Interactive Tools & Tables */}"""

content = content.replace(target_end_of_grid, new_risk_engines)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Risk Engines added.")
