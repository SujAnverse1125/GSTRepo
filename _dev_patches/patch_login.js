const fs = require('fs');
const path = require('path');

const file = path.join('D:', 'SIH2026', 'frontend', 'app', 'login', 'page.tsx');
let text = fs.readFileSync(file, 'utf8');

// 1. Add step state
if (!text.includes('const [step, setStep]')) {
  text = text.replace('const [loading, setLoading] = useState(false);', 'const [loading, setLoading] = useState(false);\n  const [step, setStep] = useState<"login" | "consent">("login");');
}

// 2. Change routing to AA step
text = text.replace("router.push('/dashboard');", "setStep('consent');\n        setTimeout(() => router.push('/dashboard'), 4000); // Wait 4 seconds then route");

// 3. Inject the Consent UI
const newReturn = `
  if (step === 'consent') {
    return (
      <div className="min-h-screen bg-[#F2EFE9] flex items-center justify-center p-6 selection:bg-[#D0B063]/30">
        <div className="w-full max-w-md bg-white rounded-3xl p-10 shadow-2xl border border-[#1A1C20]/10 flex flex-col items-center text-center animate-in fade-in zoom-in duration-500">
          <div className="relative">
            <div className="w-20 h-20 rounded-2xl bg-emerald-500/10 flex items-center justify-center mb-6 border border-emerald-500/20">
              <ShieldCheck className="w-10 h-10 text-emerald-500" />
            </div>
            <div className="absolute -bottom-2 -right-2 w-8 h-8 bg-blue-600 rounded-full flex items-center justify-center shadow-lg animate-pulse">
              <Activity className="w-4 h-4 text-white" />
            </div>
          </div>
          
          <h1 className="text-2xl font-black text-[#1A1C20] mb-2 font-serif">Sahamati Account Aggregator</h1>
          <p className="text-[#1A1C20]/60 font-medium mb-8">Securely fetching your GSTR-1, GSTR-3B, and Current Account ledgers from ICICI Bank...</p>
          
          <div className="w-full h-2 bg-[#F2EFE9] rounded-full overflow-hidden mb-4">
            <div className="h-full bg-emerald-500 rounded-full animate-[progress_4s_ease-in-out_forwards]" style={{ width: '100%' }}></div>
          </div>
          <p className="text-xs font-bold text-emerald-500 tracking-widest uppercase">Establishing Secure Data Link</p>

          <style dangerouslySetInnerHTML={{__html: \`
            @keyframes progress {
              0% { width: 0%; }
              50% { width: 60%; }
              100% { width: 100%; }
            }
          \`}} />
        </div>
      </div>
    );
  }

  return (`;

text = text.replace('return (', newReturn);

fs.writeFileSync(file, text, 'utf8');
console.log("Mock AA Consent Flow injected.");
