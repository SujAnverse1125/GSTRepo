import re

file_path = "D:\\\\SIH2026\\\\frontend\\\\app\\\\dashboard\\\\page.tsx"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Add the states
if "const [showTour, setShowTour] = useState(false);" not in content:
    content = content.replace("const [simulatedDelay, setSimulatedDelay] = useState(45);", 
                              "const [simulatedDelay, setSimulatedDelay] = useState(45);\n  const [showTour, setShowTour] = useState(false);\n  const [tourStep, setTourStep] = useState(1);")

# Trigger the tour
old_trigger = """    setTimeout(() => {
      setAppState('dashboard');
    }, 1000);"""
new_trigger = """    setTimeout(() => {
      setAppState('dashboard');
      setShowTour(true);
    }, 1000);"""
content = content.replace(old_trigger, new_trigger)

# Inject the Tour UI right after appState === 'dashboard' div opens
old_dashboard_open = """      {appState === 'dashboard' && (
        <div className="max-w-7xl mx-auto animate-in fade-in duration-1000">"""
        
tour_ui = """      {appState === 'dashboard' && (
        <div className="max-w-7xl mx-auto animate-in fade-in duration-1000">
          
          {/* Onboarding Tour Modal */}
          {showTour && (
            <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-[#1A1C20]/40 backdrop-blur-sm animate-in fade-in">
              <div className="bg-white rounded-[2rem] p-10 max-w-lg w-full shadow-2xl relative overflow-hidden">
                 <div className="absolute top-0 left-0 w-full h-2 bg-gradient-to-r from-[#1A1C20] to-[#D0B063]"></div>
                 
                 {tourStep === 1 && (
                   <div className="animate-in fade-in slide-in-from-right-4">
                     <div className="w-16 h-16 rounded-2xl bg-[#F2EFE9] flex items-center justify-center text-[#1A1C20] mb-6">
                       <BarChart3 className="w-8 h-8" />
                     </div>
                     <h3 className="text-2xl font-black font-serif mb-3 text-[#1A1C20]">Your Twin is Live.</h3>
                     <p className="text-[#1A1C20]/70 text-lg leading-relaxed mb-8">
                       We've successfully mapped your FIP Bank data against your GSTN invoices. The chart behind this is your exact cash flow projected 90 days into the future.
                     </p>
                     <button onClick={() => setTourStep(2)} className="w-full py-4 bg-[#1A1C20] text-white rounded-xl font-bold hover:bg-[#2D3139] transition-all">Next: How to use the Simulator</button>
                   </div>
                 )}

                 {tourStep === 2 && (
                   <div className="animate-in fade-in slide-in-from-right-4">
                     <div className="w-16 h-16 rounded-2xl bg-[#D0B063]/20 flex items-center justify-center text-[#D0B063] mb-6">
                       <Activity className="w-8 h-8" />
                     </div>
                     <h3 className="text-2xl font-black font-serif mb-3 text-[#1A1C20]">Simulate Reality</h3>
                     <p className="text-[#1A1C20]/70 text-lg leading-relaxed mb-8">
                       Scroll down to the <strong>Digital Twin Simulator</strong>. Drag the slider to test alternate realities—like "What if my buyer pays 30 days late?"—and watch the chart update in real-time.
                     </p>
                     <button onClick={() => setTourStep(3)} className="w-full py-4 bg-[#1A1C20] text-white rounded-xl font-bold hover:bg-[#2D3139] transition-all">Next: The Safety Net</button>
                   </div>
                 )}

                 {tourStep === 3 && (
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
                 )}
                 
                 {/* Pagination Dots */}
                 <div className="flex justify-center gap-3 mt-8">
                   {[1, 2, 3].map(step => (
                     <div key={step} className={`w-2.5 h-2.5 rounded-full transition-colors ${tourStep === step ? 'bg-[#1A1C20]' : 'bg-[#1A1C20]/10'}`}></div>
                   ))}
                 </div>
              </div>
            </div>
          )}
"""
content = content.replace(old_dashboard_open, tour_ui)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Onboarding tour added.")
