const fs = require('fs');
const path = require('path');

const file = path.join('D:', 'SIH2026', 'frontend', 'app', 'dashboard', 'page.tsx');
let text = fs.readFileSync(file, 'utf8');

// Add state for Treds Modal
if (!text.includes('showTredsModal')) {
  text = text.replace('const [loading, setLoading] = useState(true);', 'const [loading, setLoading] = useState(true);\n  const [showTredsModal, setShowTredsModal] = useState(false);\n  const [tredsStatus, setTredsStatus] = useState("loading");');
}

// Add the modal HTML before the final closing div
const tredsModalUI = `
      {/* TReDS Resolution Modal */}
      {showTredsModal && (
        <div className="fixed inset-0 z-[100] flex items-center justify-center p-4 bg-[#1A1C20]/40 backdrop-blur-sm">
          <div className="bg-white rounded-3xl p-8 max-w-sm w-full shadow-2xl border border-[#D0B063]/30 animate-in fade-in zoom-in-95 duration-300">
            {tredsStatus === 'loading' ? (
              <div className="flex flex-col items-center text-center">
                <div className="w-16 h-16 border-4 border-[#F2EFE9] border-t-[#D0B063] rounded-full animate-spin mb-6"></div>
                <h3 className="text-xl font-black text-[#1A1C20] mb-2 font-serif">Connecting to TReDS...</h3>
                <p className="text-sm text-[#1A1C20]/60">Validating GSTR-1 & securing invoice financing via SBI.</p>
              </div>
            ) : (
              <div className="flex flex-col items-center text-center">
                <div className="w-16 h-16 bg-emerald-500/10 text-emerald-500 rounded-full flex items-center justify-center mb-6">
                  <CheckCircle2 className="w-8 h-8" />
                </div>
                <h3 className="text-xl font-black text-[#1A1C20] mb-2 font-serif">Liquidity Secured</h3>
                <p className="text-sm text-[#1A1C20]/60 mb-6">₹{totalDeficit.toLocaleString('en-IN')} has been advanced by SBI and credited to your ICICI Account.</p>
                <button 
                  onClick={() => {
                    setShowTredsModal(false);
                    // Hackathon magic: Set a massive negative delay (meaning paid instantly) to visually turn the chart green
                    setSimulatedDelay(1);
                  }}
                  className="w-full py-3 bg-[#1A1C20] text-white font-bold rounded-xl hover:bg-[#2D3139] transition-all"
                >
                  View Updated Dashboard
                </button>
              </div>
            )}
          </div>
        </div>
      )}
`;

if (!text.includes('TReDS Resolution Modal')) {
  text = text.replace('</div>\n    </div>\n  );\n}', tredsModalUI + '</div>\n    </div>\n  );\n}');
}

// Update the Option 2 button to trigger the modal
text = text.replace(
  '<button className="w-full py-2 border border-[#1A1C20]/20 text-[#1A1C20] text-sm rounded-lg \nfont-bold hover:bg-[#F2EFE9] transition-all">Select</button>', 
  '<button onClick={() => { setShowTredsModal(true); setTredsStatus("loading"); setTimeout(() => setTredsStatus("success"), 2500); }} className="w-full py-2 border border-[#1A1C20]/20 text-[#1A1C20] text-sm rounded-lg font-bold hover:bg-[#F2EFE9] transition-all">Select TReDS Financing</button>'
);

// Fallback in case of powershell line-break replacement failure
text = text.replace(
  /<button[^>]*>Select<\/button>/g,
  '<button onClick={() => { setShowTredsModal(true); setTredsStatus("loading"); setTimeout(() => setTredsStatus("success"), 2500); }} className="w-full py-2 border border-[#1A1C20]/20 text-[#1A1C20] text-sm rounded-lg font-bold hover:bg-[#F2EFE9] transition-all">Select TReDS Financing</button>'
);

fs.writeFileSync(file, text, 'utf8');
console.log("TReDS Modal Flow injected.");
