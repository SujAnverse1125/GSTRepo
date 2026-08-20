import re

file_path = "D:\\\\SIH2026\\\\frontend\\\\app\\\\page.tsx"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add new state types and components above the Home function
new_components = """
type AppState = 'landing' | 'consent' | 'processing' | 'dashboard';

function LandingPage({ onNext }: { onNext: () => void }) {
  return (
    <div className="flex min-h-screen flex-col items-center justify-center bg-[#020817] p-4 text-slate-100">
      <div className="max-w-md text-center">
        <div className="mb-6 flex justify-center">
          <div className="flex h-16 w-16 items-center justify-center rounded-2xl bg-gradient-to-br from-cyan-500 to-blue-600 shadow-lg shadow-cyan-500/30">
            <svg className="h-8 w-8 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 10V3L4 14h7v7l9-11h-7z" />
            </svg>
          </div>
        </div>
        <h1 className="mb-4 text-4xl font-bold tracking-tight text-white">NoodleNova Twin</h1>
        <p className="mb-8 text-slate-400">Consent-based cash flow prediction and GST paradox prevention for Indian MSMEs.</p>
        <button 
          onClick={onNext}
          className="w-full rounded-full bg-cyan-500 px-6 py-3 font-semibold text-slate-950 transition hover:bg-cyan-400 focus:outline-none focus:ring-2 focus:ring-cyan-500 focus:ring-offset-2 focus:ring-offset-[#020817]"
        >
          Secure Login
        </button>
      </div>
    </div>
  );
}

function ConsentPage({ onNext }: { onNext: () => void }) {
  const [otp, setOtp] = useState('');
  const [step, setStep] = useState(1);

  return (
    <div className="flex min-h-screen flex-col items-center justify-center bg-[#020817] p-4 text-slate-100">
      <div className="w-full max-w-md rounded-[24px] border border-slate-800 bg-slate-900/50 p-8 shadow-2xl">
        <h2 className="mb-2 text-2xl font-bold text-white">Data Consent</h2>
        <p className="mb-6 text-sm text-slate-400">Connect your financial data via the Account Aggregator network.</p>
        
        <div className="mb-6 space-y-3">
          <div className="flex items-center justify-between rounded-lg border border-emerald-500/20 bg-emerald-500/5 p-3">
            <span className="text-sm font-medium text-slate-300">HDFC Bank (FIP)</span>
            <span className="text-xs text-emerald-400">Ready to link</span>
          </div>
          <div className="flex items-center justify-between rounded-lg border border-emerald-500/20 bg-emerald-500/5 p-3">
            <span className="text-sm font-medium text-slate-300">GSTN Portal</span>
            <span className="text-xs text-emerald-400">Ready to link</span>
          </div>
        </div>

        {step === 1 ? (
          <button 
            onClick={() => setStep(2)}
            className="w-full rounded-lg bg-white px-4 py-2 font-medium text-slate-900 transition hover:bg-slate-200"
          >
            Generate AA Request
          </button>
        ) : (
          <div className="space-y-4 animate-in fade-in slide-in-from-bottom-4">
            <div>
              <label className="mb-1 block text-xs text-slate-400">Enter 6-digit OTP sent to mobile</label>
              <input 
                type="text" 
                maxLength={6}
                value={otp}
                onChange={(e) => setOtp(e.target.value)}
                className="w-full rounded-lg border border-slate-700 bg-slate-800 px-4 py-2 text-center tracking-[0.5em] text-white focus:border-cyan-500 focus:outline-none"
                placeholder="••••••"
              />
            </div>
            <button 
              onClick={onNext}
              disabled={otp.length !== 6}
              className="w-full rounded-lg bg-cyan-500 px-4 py-2 font-medium text-slate-950 transition hover:bg-cyan-400 disabled:opacity-50"
            >
              Verify & Import Data
            </button>
          </div>
        )}
      </div>
    </div>
  );
}

function ProcessingPage({ onNext }: { onNext: () => void }) {
  const [logIdx, setLogIdx] = useState(0);
  const logs = [
    "Establishing secure FIU tunnel...",
    "Decrypting HDFC Bank statements...",
    "Pulling unpaid GSTN invoices...",
    "Calculating historical buyer delays...",
    "Running standard deviation variance...",
    "Generating 90-day Twin simulation..."
  ];

  useEffect(() => {
    const timer = setInterval(() => {
      setLogIdx((prev) => {
        if (prev >= logs.length - 1) {
          clearInterval(timer);
          setTimeout(onNext, 1000);
          return prev;
        }
        return prev + 1;
      });
    }, 800);
    return () => clearInterval(timer);
  }, [logs.length, onNext]);

  return (
    <div className="flex min-h-screen flex-col items-center justify-center bg-[#020817] p-4 text-slate-100">
      <div className="w-full max-w-md space-y-8 text-center">
        <div className="mx-auto flex h-16 w-16 items-center justify-center rounded-full bg-slate-800">
          <svg className="h-8 w-8 animate-spin text-cyan-500" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
            <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
            <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
          </svg>
        </div>
        <div className="space-y-2 font-mono text-sm text-slate-400">
          {logs.slice(0, logIdx + 1).map((log, i) => (
            <p key={i} className={i === logIdx ? "text-cyan-400 animate-pulse" : "opacity-50"}>
              > {log}
            </p>
          ))}
        </div>
      </div>
    </div>
  );
}

export default function Home() {
"""

# Replace `export default function Home() {`
content = content.replace("export default function Home() {\n", new_components)

# 2. Add state inside Home
state_injection = """
  const [appState, setAppState] = useState<AppState>('landing');
"""
# Insert right after the new `export default function Home() {` line which was injected above.
content = content.replace("export default function Home() {", "export default function Home() {\n" + state_injection)

# 3. Add conditional rendering before the main return statement
conditional_return = """
  if (appState === 'landing') return <LandingPage onNext={() => setAppState('consent')} />;
  if (appState === 'consent') return <ConsentPage onNext={() => setAppState('processing')} />;
  if (appState === 'processing') return <ProcessingPage onNext={() => setAppState('dashboard')} />;

  return (
    <main className="min-h-screen bg-[#020817] text-slate-100">
"""

content = content.replace('  return (\n    <main className="min-h-screen bg-[#020817] text-slate-100">', conditional_return)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("UI state machine injected perfectly.")
