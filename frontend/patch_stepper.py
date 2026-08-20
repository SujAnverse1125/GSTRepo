import re

file_path = "D:\\\\SIH2026\\\\frontend\\\\app\\\\dashboard\\\\page.tsx"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

old_processing = """      {appState === 'processing' && (
        <div className="max-w-2xl mx-auto mt-32 animate-in zoom-in-95">
          <div className="bg-[#1A1C20] rounded-[2rem] p-8 shadow-2xl border border-[#D0B063]/30 relative overflow-hidden">
             {/* Spinner */}
             <div className="absolute top-0 left-0 w-full h-1 bg-gradient-to-r from-transparent via-[#D0B063] to-transparent animate-pulse"></div>
             
             <div className="flex items-center gap-4 mb-8">
               <Server className="w-8 h-8 text-[#D0B063] animate-pulse" />
               <h2 className="text-2xl font-black text-white font-serif">Twin Engine Ingestion</h2>
             </div>

             <div className="space-y-3 font-mono text-sm">
               {logs.map((log, i) => (
                 <div key={i} className="flex gap-3 text-emerald-400 animate-in slide-in-from-left-4">
                   <span>&gt;</span>
                   <span>{log}</span>
                 </div>
               ))}
               <div className="flex gap-3 text-[#D0B063] animate-pulse">
                 <span>&gt;</span>
                 <span className="w-2 h-4 bg-[#D0B063]"></span>
               </div>
             </div>
          </div>
        </div>
      )}"""

new_processing = """      {appState === 'processing' && (
        <div className="max-w-3xl mx-auto mt-20 animate-in zoom-in-95">
          <div className="bg-white rounded-[2rem] p-10 border border-[#1A1C20]/10 shadow-2xl relative overflow-hidden">
             <div className="flex items-center gap-4 mb-10">
               <div className="w-16 h-16 rounded-full bg-[#F2EFE9] flex items-center justify-center">
                 <div className="w-8 h-8 border-4 border-[#D0B063]/30 border-t-[#D0B063] rounded-full animate-spin"></div>
               </div>
               <div>
                 <h2 className="text-3xl font-black text-[#1A1C20] font-serif">Building Your Twin</h2>
                 <p className="text-[#1A1C20]/60 font-medium">Please wait while we secure your data and run the simulations.</p>
               </div>
             </div>

             <div className="space-y-8">
               {[
                 { title: "Hello! Initializing Secure Connection", desc: "Establishing a bank-grade AES-256 encrypted tunnel." },
                 { title: "Fetching FIP Bank Statements", desc: "We are securely pulling your last 6 months of cash flow history." },
                 { title: "Parsing GSTN Invoices", desc: "Matching outward invoices to predict your upcoming tax liabilities." },
                 { title: "AI Deviation Analysis", desc: "Calculating exactly how many days your buyers typically delay payments." },
                 { title: "You're in safe hands", desc: "Finalizing your MSME Digital Twin. We predict, then we delete." }
               ].map((step, i) => {
                 const isCompleted = i < Math.floor(logs.length / 1.2);
                 const isCurrent = i === Math.floor(logs.length / 1.2);
                 return (
                   <div key={i} className={`flex gap-6 transition-all duration-500 ${isCompleted || isCurrent ? 'opacity-100 translate-x-0' : 'opacity-30 translate-x-4'}`}>
                     <div className="flex flex-col items-center">
                       {isCompleted ? (
                         <div className="w-8 h-8 rounded-full bg-emerald-100 flex items-center justify-center">
                           <CheckCircle2 className="w-5 h-5 text-emerald-600" />
                         </div>
                       ) : isCurrent ? (
                         <div className="w-8 h-8 rounded-full bg-[#F2EFE9] flex items-center justify-center border-2 border-[#D0B063]">
                           <div className="w-3 h-3 bg-[#D0B063] rounded-full animate-pulse"></div>
                         </div>
                       ) : (
                         <div className="w-8 h-8 rounded-full bg-[#F2EFE9] border border-[#1A1C20]/10"></div>
                       )}
                       {i < 4 && <div className={`w-0.5 h-12 mt-2 ${isCompleted ? 'bg-emerald-200' : 'bg-[#1A1C20]/5'}`}></div>}
                     </div>
                     <div className={isCurrent ? 'animate-pulse' : ''}>
                       <h3 className={`text-lg font-bold ${isCompleted ? 'text-[#1A1C20]' : 'text-[#1A1C20]/60'}`}>{step.title}</h3>
                       <p className="text-[#1A1C20]/50 text-sm mt-1">{step.desc}</p>
                     </div>
                   </div>
                 );
               })}
             </div>
          </div>
        </div>
      )}"""

# We need to make sure startIngestion function triggers enough state changes to drive the stepper
old_ingestion = """    const steps = [
      "Authenticating with Account Aggregator...",
      "FIP Consent Granted. Fetching 6-month bank statements...",
      "Parsing GSTN invoices via API...",
      "Running standard deviation analysis on buyer delays...",
      "Calculating GST Liquidity Paradox...",
      "Generating Digital Twin..."
    ];

    for (let i = 0; i < steps.length; i++) {
      await new Promise(r => setTimeout(r, 1000));
      setLogs(prev => [...prev, steps[i]]);
    }

    // Fetch actual data from python backend"""

new_ingestion = """    const steps = [
      "Authenticating with Account Aggregator...",
      "FIP Consent Granted. Fetching 6-month bank statements...",
      "Parsing GSTN invoices via API...",
      "Running standard deviation analysis on buyer delays...",
      "Calculating GST Liquidity Paradox...",
      "Generating Digital Twin...",
      "Finishing up..."
    ];

    for (let i = 0; i < steps.length; i++) {
      await new Promise(r => setTimeout(r, 800));
      setLogs(prev => [...prev, steps[i]]);
    }

    // Fetch actual data from python backend"""

content = content.replace(old_processing, new_processing)
content = content.replace(old_ingestion, new_ingestion)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Premium stepper applied successfully.")
