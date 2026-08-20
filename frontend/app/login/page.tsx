"use client";

import { useState } from 'react';
import { supabase } from '../../utils/supabase';
import { useRouter } from 'next/navigation';
import { ShieldCheck, Activity } from 'lucide-react';

export default function LoginPage() {
  const [phone, setPhone] = useState('');
  const [showOtp, setShowOtp] = useState(false);
  const [otp, setOtp] = useState('');
  const [loading, setLoading] = useState(false);
  const [step, setStep] = useState<"login" | "consent">("login");
  const [errorMsg, setErrorMsg] = useState('');
  const router = useRouter();

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
        // Auth successful, push to the consent dashboard flow
        setStep('consent');
        setTimeout(() => router.push('/dashboard'), 4000); // Wait 4 seconds then route
      }
    }
  };

  
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

          <style dangerouslySetInnerHTML={{__html: `
            @keyframes progress {
              0% { width: 0%; }
              50% { width: 60%; }
              100% { width: 100%; }
            }
          `}} />
        </div>
      </div>
    );
  }

  return (
    <div className="flex min-h-screen flex-col items-center justify-center bg-[#F2EFE9] p-4 text-[#1A1C20] selection:bg-[#D0B063]/30">
      <div className="w-full max-w-md rounded-[2rem] border border-[#1A1C20]/10 bg-white p-10 shadow-2xl text-center relative overflow-hidden">
        {/* Subtle decorative accent */}
        <div className="absolute top-0 left-0 w-full h-2 bg-gradient-to-r from-[#1A1C20] to-[#D0B063]"></div>

        <div className="mb-8 flex justify-center">
          <div className="flex h-20 w-20 items-center justify-center rounded-2xl bg-[#1A1C20] shadow-xl shadow-[#1A1C20]/20">
            <Activity className="h-10 w-10 text-[#D0B063]" />
          </div>
        </div>
        
        <h1 className="mb-2 text-3xl font-black tracking-tight text-[#1A1C20] font-serif">MSME Twin Login</h1>
        <p className="mb-8 text-sm text-[#1A1C20]/60 font-medium">Secure Account Aggregator Auth via Supabase.</p>
        
        {errorMsg && (
          <div className="mb-6 rounded-xl border border-rose-500/50 bg-rose-500/10 p-4 text-sm text-rose-600 font-medium">
            {errorMsg}
          </div>
        )}

        {!showOtp ? (
          <div className="space-y-5 animate-in fade-in">
            <div className="text-left">
              <label className="mb-2 block text-xs font-bold text-[#1A1C20]/70 uppercase tracking-wider">Mobile Number</label>
              <div className="flex shadow-sm rounded-xl overflow-hidden">
                <span className="inline-flex items-center border border-r-0 border-[#1A1C20]/10 bg-[#F2EFE9] px-4 text-sm font-bold text-[#1A1C20]/60">
                  +91
                </span>
                <input 
                  type="tel" 
                  maxLength={10}
                  value={phone}
                  onChange={(e) => setPhone(e.target.value.replace(/\D/g, ''))}
                  className="w-full border border-[#1A1C20]/10 bg-white px-5 py-4 text-[#1A1C20] font-bold focus:border-[#D0B063] focus:ring-1 focus:ring-[#D0B063] focus:outline-none transition-all"
                  placeholder="00000 00000"
                />
              </div>
            </div>
            <button 
              onClick={handleSendOtp}
              disabled={phone.length !== 10 || loading}
              className="w-full rounded-xl bg-[#1A1C20] px-4 py-4 font-bold text-white transition-all hover:bg-[#2D3139] disabled:opacity-50 hover:-translate-y-0.5 shadow-lg shadow-[#1A1C20]/20"
            >
              {loading ? 'Sending Request...' : 'Send Secure OTP'}
            </button>
          </div>
        ) : (
          <div className="space-y-5 animate-in fade-in slide-in-from-right-4">
            <div className="text-left">
              <label className="mb-2 flex justify-between text-xs font-bold text-[#1A1C20]/70 uppercase tracking-wider">
                <span>Enter OTP sent to +91 {phone}</span>
                <button onClick={() => {setShowOtp(false); setErrorMsg('');}} className="text-[#D0B063] hover:underline">Edit</button>
              </label>
              <input 
                type="password" 
                maxLength={6}
                value={otp}
                onChange={(e) => setOtp(e.target.value.replace(/\D/g, ''))}
                className="w-full rounded-xl border border-[#1A1C20]/10 bg-white px-5 py-4 text-center tracking-[0.75em] text-2xl font-black text-[#1A1C20] focus:border-[#D0B063] focus:ring-1 focus:ring-[#D0B063] focus:outline-none transition-all"
                placeholder="••••••"
              />
            </div>
            <button 
              onClick={handleVerifyOtp}
              disabled={otp.length !== 6 || loading}
              className="w-full rounded-xl bg-[#D0B063] px-4 py-4 font-bold text-[#1A1C20] transition-all hover:bg-[#E3C376] disabled:opacity-50 hover:-translate-y-0.5 shadow-lg shadow-[#D0B063]/30"
            >
              {loading ? 'Verifying...' : 'Verify & Enter Twin'}
            </button>
          </div>
        )}
      </div>

      <div className="mt-8 flex items-center gap-2 text-sm font-medium text-[#1A1C20]/50">
        <ShieldCheck className="w-4 h-4" /> RBI Account Aggregator Compliant
      </div>
    </div>
  );
}
