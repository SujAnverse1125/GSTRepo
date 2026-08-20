file_path = "D:\\\\SIH2026\\\\frontend\\\\app\\\\page.tsx"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Insert the Supabase import at the top
if "import { supabase }" not in content:
    content = content.replace("import { useEffect, useState } from 'react';", "import { useEffect, useState } from 'react';\nimport { supabase } from '../utils/supabase';")

# The old mock LandingPage
old_landing = """function LandingPage({ onNext }: { onNext: () => void }) {
  const [phone, setPhone] = useState('');
  const [showOtp, setShowOtp] = useState(false);
  const [otp, setOtp] = useState('');

  const handleSendOtp = () => {
    if (phone.length >= 10) setShowOtp(true);
  };

  return (
    <div className="flex min-h-screen flex-col items-center justify-center bg-[#020817] p-4 text-slate-100">
      <div className="w-full max-w-md rounded-[24px] border border-slate-800 bg-slate-900/50 p-8 shadow-2xl text-center">
        <div className="mb-6 flex justify-center">
          <div className="flex h-16 w-16 items-center justify-center rounded-2xl bg-gradient-to-br from-cyan-500 to-blue-600 shadow-lg shadow-cyan-500/30">
            <svg className="h-8 w-8 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
            </svg>
          </div>
        </div>
        <h1 className="mb-2 text-3xl font-bold tracking-tight text-white">MSME Twin Login</h1>
        <p className="mb-8 text-sm text-slate-400">Secure access to your liquidity command center.</p>
        
        {!showOtp ? (
          <div className="space-y-4 animate-in fade-in">
            <div className="text-left">
              <label className="mb-1 block text-xs text-slate-400">Mobile Number</label>
              <div className="flex">
                <span className="inline-flex items-center rounded-l-lg border border-r-0 border-slate-700 bg-slate-800 px-3 text-sm text-slate-400">+91</span>
                <input 
                  type="tel" 
                  maxLength={10}
                  value={phone}
                  onChange={(e) => setPhone(e.target.value.replace(/\\D/g, ''))}
                  className="w-full rounded-r-lg border border-slate-700 bg-slate-800 px-4 py-2 text-white focus:border-cyan-500 focus:outline-none"
                  placeholder="98765 43210"
                />
              </div>
            </div>
            <button 
              onClick={handleSendOtp}
              disabled={phone.length !== 10}
              className="w-full rounded-lg bg-cyan-500 px-4 py-3 font-semibold text-slate-950 transition hover:bg-cyan-400 disabled:opacity-50"
            >
              Send Secure OTP
            </button>
          </div>
        ) : (
          <div className="space-y-4 animate-in fade-in slide-in-from-right-4">
            <div className="text-left">
              <label className="mb-1 flex justify-between text-xs text-slate-400">
                <span>Enter OTP sent to +91 {phone}</span>
                <button onClick={() => setShowOtp(false)} className="text-cyan-400 hover:underline">Edit</button>
              </label>
              <input 
                type="text" 
                maxLength={6}
                value={otp}
                onChange={(e) => setOtp(e.target.value.replace(/\\D/g, ''))}
                className="w-full rounded-lg border border-slate-700 bg-slate-800 px-4 py-3 text-center tracking-[0.5em] text-white focus:border-cyan-500 focus:outline-none"
                placeholder="••••••"
              />
            </div>
            <button 
              onClick={onNext}
              disabled={otp.length !== 6}
              className="w-full rounded-lg bg-cyan-500 px-4 py-3 font-semibold text-slate-950 transition hover:bg-cyan-400 disabled:opacity-50"
            >
              Verify & Login
            </button>
          </div>
        )}
      </div>
    </div>
  );
}"""

# The new real Supabase LandingPage
new_landing = """function LandingPage({ onNext }: { onNext: () => void }) {
  const [phone, setPhone] = useState('');
  const [showOtp, setShowOtp] = useState(false);
  const [otp, setOtp] = useState('');
  const [loading, setLoading] = useState(false);
  const [errorMsg, setErrorMsg] = useState('');

  const handleSendOtp = async () => {
    if (phone.length >= 10) {
      setLoading(true);
      setErrorMsg('');
      const { error } = await supabase.auth.signInWithOtp({
        phone: '+91' + phone,
      });
      setLoading(false);
      
      if (error) {
        setErrorMsg(error.message);
      } else {
        setShowOtp(true);
      }
    }
  };

  const handleVerifyOtp = async () => {
    if (otp.length === 6) {
      setLoading(true);
      setErrorMsg('');
      const { data, error } = await supabase.auth.verifyOtp({
        phone: '+91' + phone,
        token: otp,
        type: 'sms',
      });
      setLoading(false);

      if (error) {
        setErrorMsg(error.message);
      } else if (data.session) {
        onNext();
      }
    }
  };

  return (
    <div className="flex min-h-screen flex-col items-center justify-center bg-[#020817] p-4 text-slate-100">
      <div className="w-full max-w-md rounded-[24px] border border-slate-800 bg-slate-900/50 p-8 shadow-2xl text-center">
        <div className="mb-6 flex justify-center">
          <div className="flex h-16 w-16 items-center justify-center rounded-2xl bg-gradient-to-br from-cyan-500 to-blue-600 shadow-lg shadow-cyan-500/30">
            <svg className="h-8 w-8 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
            </svg>
          </div>
        </div>
        <h1 className="mb-2 text-3xl font-bold tracking-tight text-white">MSME Twin Login</h1>
        <p className="mb-6 text-sm text-slate-400">Secure access to your liquidity command center.</p>
        
        {errorMsg && (
          <div className="mb-4 rounded border border-rose-500/50 bg-rose-500/10 p-3 text-sm text-rose-400">
            {errorMsg}
          </div>
        )}

        {!showOtp ? (
          <div className="space-y-4 animate-in fade-in">
            <div className="text-left">
              <label className="mb-1 block text-xs text-slate-400">Mobile Number</label>
              <div className="flex">
                <span className="inline-flex items-center rounded-l-lg border border-r-0 border-slate-700 bg-slate-800 px-3 text-sm text-slate-400">+91</span>
                <input 
                  type="tel" 
                  maxLength={10}
                  value={phone}
                  onChange={(e) => setPhone(e.target.value.replace(/\\D/g, ''))}
                  className="w-full rounded-r-lg border border-slate-700 bg-slate-800 px-4 py-2 text-white focus:border-cyan-500 focus:outline-none"
                  placeholder="00000 00000"
                />
              </div>
            </div>
            <button 
              onClick={handleSendOtp}
              disabled={phone.length !== 10 || loading}
              className="w-full rounded-lg bg-cyan-500 px-4 py-3 font-semibold text-slate-950 transition hover:bg-cyan-400 disabled:opacity-50"
            >
              {loading ? 'Sending...' : 'Send Secure OTP'}
            </button>
          </div>
        ) : (
          <div className="space-y-4 animate-in fade-in slide-in-from-right-4">
            <div className="text-left">
              <label className="mb-1 flex justify-between text-xs text-slate-400">
                <span>Enter OTP sent to +91 {phone}</span>
                <button onClick={() => {setShowOtp(false); setErrorMsg('');}} className="text-cyan-400 hover:underline">Edit</button>
              </label>
              <input 
                type="text" 
                maxLength={6}
                value={otp}
                onChange={(e) => setOtp(e.target.value.replace(/\\D/g, ''))}
                className="w-full rounded-lg border border-slate-700 bg-slate-800 px-4 py-3 text-center tracking-[0.5em] text-white focus:border-cyan-500 focus:outline-none"
                placeholder="••••••"
              />
            </div>
            <button 
              onClick={handleVerifyOtp}
              disabled={otp.length !== 6 || loading}
              className="w-full rounded-lg bg-cyan-500 px-4 py-3 font-semibold text-slate-950 transition hover:bg-cyan-400 disabled:opacity-50"
            >
              {loading ? 'Verifying...' : 'Verify & Login'}
            </button>
          </div>
        )}
      </div>
    </div>
  );
}"""

content = content.replace(old_landing, new_landing)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Real Supabase Auth injected.")
