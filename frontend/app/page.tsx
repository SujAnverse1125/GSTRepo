"use client";
import { useState, useEffect } from "react";
import Link from "next/link";
import LiquidityCalculator from "./components/LiquidityCalculator";
import { ArrowRight, BarChart3, Clock, Landmark, ShieldCheck, Zap, Check, X, Circle, Activity, CheckCircle2, FileWarning } from "lucide-react";

export default function LandingPage() {

  const alerts = [
    {
      type: "bad",
      title: "GST Deficit Predicted",
      desc: "A ₹2.5L shortfall is expected on Day 18 due to Buyer Delay.",
      icon: <FileWarning className="w-5 h-5" />,
      colors: "bg-rose-500/10 border-rose-500/20 text-rose-300",
      iconBg: "bg-rose-500/20"
    },
    {
      type: "good",
      title: "Inflow Cleared",
      desc: "L&T invoice #9042 settled. Cash buffer increased by ₹1.2L.",
      icon: <CheckCircle2 className="w-5 h-5" />,
      colors: "bg-emerald-500/10 border-emerald-500/20 text-emerald-300",
      iconBg: "bg-emerald-500/20"
    },
    {
      type: "warning",
      title: "Concentration Risk",
      desc: "Reliance Retail accounts for 68% of your current receivables.",
      icon: <Activity className="w-5 h-5" />,
      colors: "bg-amber-500/10 border-amber-500/20 text-amber-300",
      iconBg: "bg-amber-500/20"
    }
  ];
  const [alertIdx, setAlertIdx] = useState(0);
  useEffect(() => {
    const int = setInterval(() => {
      setAlertIdx((prev) => (prev + 1) % alerts.length);
    }, 4000);
    return () => clearInterval(int);
  }, []);

  return (
    <div className="min-h-screen bg-gradient-to-b from-[#F2EFE9] to-[#FCFDFD] text-[#1A1C20] font-sans selection:bg-[#D0B063]/30">

      <style dangerouslySetInnerHTML={{__html: `
        @keyframes equalize {
          0% { height: var(--base-height); }
          50% { height: calc(var(--base-height) + 10%); }
          100% { height: var(--base-height); }
        }
        .live-bar {
          animation: equalize 2.5s ease-in-out infinite;
        }
      `}} />

      
      {/* Navigation */}
      <nav className="fixed w-full top-0 z-50 flex items-center justify-between px-6 lg:px-12 py-5 bg-[#F2EFE9]/80 backdrop-blur-md border-b border-[#D0B063]/20">
        <div className="flex items-center gap-2">
          <div className="flex h-10 w-10 items-center justify-center rounded-full bg-[#1A1C20] text-[#D0B063] shadow-md">
            <Activity className="h-5 w-5" />
          </div>
          <span className="font-extrabold text-2xl tracking-tight text-[#1A1C20] font-serif">MSME Twin</span>
        </div>
        <div className="flex items-center gap-6">
          <div className="hidden md:flex gap-6 text-sm font-bold text-[#1A1C20]/60">
            <Link href="#problem" className="hover:text-[#1A1C20] transition-colors">The Problem</Link>
            <Link href="#features" className="hover:text-[#1A1C20] transition-colors">How it Works</Link>
          </div>
          <Link href="/login" className="px-6 py-3 text-sm font-bold text-white bg-[#1A1C20] rounded-full hover:bg-[#2D3139] transition-all shadow-lg hover:-translate-y-0.5 flex items-center gap-2">
            Launch Demo <ArrowRight className="w-4 h-4" />
          </Link>
        </div>
      </nav>

      {/* Hero Section */}
      <section className="pt-40 pb-20 px-6 lg:px-12 max-w-7xl mx-auto flex flex-col lg:flex-row items-center gap-16">
        <div className="flex-1 text-center lg:text-left animate-in fade-in slide-in-from-bottom-8 duration-1000 mt-10">
          <div className="flex flex-wrap items-center justify-center lg:justify-start gap-3 mb-8">
            
            <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-[#1A1C20]/5 border border-[#1A1C20]/10 text-[#1A1C20]/70 text-sm font-bold">
              <ShieldCheck className="w-4 h-4" /> Account Aggregator Sandbox
            </div>
          </div>
          
          <h1 className="text-5xl md:text-7xl font-black tracking-tight text-[#1A1C20] mb-6 leading-[1.1] font-serif">
            Survive the GST Trap with an <span className="text-[#D0B063]">AI Digital Twin.</span>
          </h1>
          <p className="text-xl text-[#1A1C20]/70 mb-10 max-w-xl mx-auto lg:mx-0 leading-relaxed font-medium">
            Connect your ERP or bank data. Our predictive engine maps your cash flow 90 days out, spots buyer delays, and bridges liquidity gaps before they destroy your MSME.
          </p>
          <div className="flex flex-col sm:flex-row items-center justify-center lg:justify-start gap-4">
            <Link href="/login" className="w-full sm:w-auto px-8 py-4 text-base font-bold text-white bg-[#1A1C20] rounded-full hover:bg-[#2D3139] transition-all shadow-2xl hover:-translate-y-1 flex items-center justify-center gap-3">
              Launch Command Center <Zap className="w-5 h-5 text-[#D0B063]" />
            </Link>
          </div>
        </div>
                <div className="flex-1 relative w-full max-w-lg lg:max-w-none mt-10">
          <div className="relative w-full h-[500px] flex items-center justify-center">
            
            {/* Background Blob */}
            <div className="absolute inset-0 bg-[#D0B063]/20 blur-3xl rounded-full opacity-50 mix-blend-multiply animate-pulse"></div>
            
            {/* Main Floating UI */}
            <div className="relative z-10 w-full max-w-md bg-[#1A1C20] rounded-[2rem] shadow-2xl border border-white/10 p-8 transform rotate-3 hover:rotate-0 transition-transform duration-500 overflow-hidden">
              
              {/* Header */}
              <div className="flex justify-between items-center mb-8 border-b border-white/10 pb-4">
                <div className="flex items-center gap-3">
                  <div className="w-10 h-10 bg-emerald-500/20 rounded-full flex items-center justify-center text-emerald-300">
                    <CheckCircle2 className="w-5 h-5" />
                  </div>
                  <div>
                    <p className="text-white font-bold text-sm">FIP Connected</p>
                    <p className="text-white/40 text-xs">Syncing AA Data...</p>
                  </div>
                </div>
                <div className="w-2 h-2 bg-emerald-500 rounded-full animate-ping"></div>
              </div>

              {/* Chart Mock */}
              <div className="space-y-4 mb-8">
                <p className="text-white/50 text-xs font-bold uppercase tracking-widest">90-Day Liquidity Map</p>
                <div className="flex items-end gap-2 h-32">
                  {[40, 50, 60, 45, 30, 15, 5, 20, 50, 70, 80, 90].map((h, i) => (
                    <div 
                      key={i} 
                      className={`flex-1 rounded-t-sm live-bar ${h < 20 ? 'bg-rose-500 shadow-[0_0_15px_rgba(244,63,94,0.6)]' : 'bg-[#D0B063]'}`} 
                      style={{ 
                        '--base-height': `${h}%`, 
                        height: `${h}%`,
                        animationDelay: `${i * 0.12}s` 
                      } as any}
                    ></div>
                  ))}
                </div>
              </div>

              {/* Dynamic Alert Card */}
              <div className={`transition-colors duration-500 border rounded-xl p-4 flex items-start gap-4 ${alerts[alertIdx].colors}`}>
                <div className={`p-2 rounded-lg mt-1 ${alerts[alertIdx].iconBg}`}>
                  {alerts[alertIdx].icon}
                </div>
                <div className="transition-opacity duration-500 animate-in fade-in" key={alertIdx}>
                  <p className="font-bold text-sm text-white">{alerts[alertIdx].title}</p>
                  <p className="text-white/80 text-xs mt-1">{alerts[alertIdx].desc}</p>
                </div>
              </div>

            </div>

            {/* Floating Element 2 */}
            <div className="absolute -bottom-8 -left-8 z-20 bg-white p-4 rounded-2xl shadow-xl border border-black/5 flex items-center gap-4 animate-bounce hover:animate-none" style={{ animationDuration: '3s' }}>
              <div className="bg-[#1A1C20] p-3 rounded-xl text-[#D0B063]">
                <Activity className="w-6 h-6" />
              </div>
              <div>
                <p className="text-[#1A1C20] font-black text-sm">AI CFO Action Matrix</p>
                <p className="text-[#1A1C20]/60 text-xs font-medium mt-0.5">3 Solutions Generated</p>
              </div>
            </div>

          </div>
        </div>
      </section>

      {/* The Tension Section (Steward Wise Inspired) */}
      <section className="py-32 px-6 bg-[#FCFDFD]">
        <div className="max-w-5xl mx-auto">
          <div className="mb-16">
            <h2 className="text-4xl md:text-5xl font-black text-[#1A1C20] mb-6 font-serif">
              If You've Ever Felt the Panic of a <span className="text-rose-700">GST Deadline...</span> You're Not Alone.
            </h2>
            <p className="text-xl text-[#1A1C20]/70 max-w-3xl leading-relaxed">
              So many MSMEs struggle silently with the GST Liquidity Paradox. You deliver the goods, you pay the taxes, but the buyer takes 90 days to pay you. That gap gets messy.
            </p>
          </div>

          <div className="space-y-12">
            <div className="flex gap-6 items-start">
              <div className="flex flex-col items-center mt-2">
                <div className="w-4 h-4 rounded-full bg-[#D0B063]"></div>
                <div className="w-0.5 h-24 bg-[#D0B063]/30 my-2"></div>
              </div>
              <div>
                <h3 className="text-2xl font-bold text-[#1A1C20] mb-2"><span className="text-[#D0B063]">Day 1:</span> The Illusion of Wealth</h3>
                <p className="text-lg text-[#1A1C20]/60">You raise an invoice for ₹1 Lakh. On paper, you are profitable. In reality, your bank account hasn't changed.</p>
              </div>
            </div>
            
            <div className="flex gap-6 items-start">
              <div className="flex flex-col items-center mt-2">
                <div className="w-4 h-4 rounded-full bg-rose-500"></div>
                <div className="w-0.5 h-24 bg-rose-500/30 my-2"></div>
              </div>
              <div>
                <h3 className="text-2xl font-bold text-[#1A1C20] mb-2"><span className="text-rose-500">Day 20:</span> The Tax Trap</h3>
                <p className="text-lg text-[#1A1C20]/60">The government demands 18% GST immediately. You are forced to pay ₹18,000 out of your own pocket.</p>
              </div>
            </div>

            <div className="flex gap-6 items-start">
              <div className="flex flex-col items-center mt-2">
                <div className="w-4 h-4 rounded-full bg-[#1A1C20]"></div>
              </div>
              <div>
                <h3 className="text-2xl font-bold text-[#1A1C20] mb-2">MSME Twin was born out of that tension.</h3>
                <p className="text-lg text-[#1A1C20]/60">We're not here to just show you charts—we're here to walk with you, predict the gaps, and bridge them before you default.</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Features Grid (A Breath of Fresh Air) */}
      <section className="py-32 px-6 bg-[#1A1C20] text-white">
        <div className="max-w-7xl mx-auto">
          <div className="mb-20 text-center">
            <h2 className="text-4xl md:text-6xl font-black mb-6 font-serif">
              A Financial Tool That Feels Like a <span className="text-[#D0B063]">Breath of Fresh Air.</span>
            </h2>
            <p className="text-xl text-white/60 max-w-2xl mx-auto">
              Here's how we blend Account Aggregator data with AI predictive power without the overwhelm.
            </p>
          </div>

          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
            <div className="p-10 rounded-[2rem] bg-white/5 border border-white/10 hover:bg-white/10 transition-colors">
              <Landmark className="w-12 h-12 text-[#D0B063] mb-8" />
              <h3 className="text-2xl font-bold mb-4">Account Aggregator</h3>
              <p className="text-white/60 text-lg leading-relaxed">Secure, consent-based sync with your banks and GSTN. No manual data entry ever again.</p>
            </div>
            
            <div className="p-10 rounded-[2rem] bg-[#D0B063] text-[#1A1C20] border border-[#D0B063] shadow-2xl shadow-[#D0B063]/20 hover:-translate-y-2 transition-transform">
              <Clock className="w-12 h-12 text-[#1A1C20] mb-8" />
              <h3 className="text-2xl font-black mb-4">AI Predictive Engine</h3>
              <p className="text-[#1A1C20]/80 text-lg leading-relaxed font-medium">Using standard deviation, we analyze buyer delay habits and map out exactly when cash will dry up.</p>
            </div>

            <div className="p-10 rounded-[2rem] bg-white/5 border border-white/10 hover:bg-white/10 transition-colors">
              <Zap className="w-12 h-12 text-[#D0B063] mb-8" />
              <h3 className="text-2xl font-bold mb-4">1-Click Auto-Finance</h3>
              <p className="text-white/60 text-lg leading-relaxed">When the AI spots a cash crater in your timeline, it triggers pre-approved invoice discounting automatically.</p>
            </div>
          </div>
        </div>
      </section>

      <LiquidityCalculator />

      {/* Comparison Table (Built Section) */}
      <section className="py-32 px-6 bg-[#FCFDFD]">
        <div className="max-w-5xl mx-auto">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-black text-[#1A1C20] mb-6 font-serif">Built With <span className="text-[#D0B063]">MSMEs</span> in Mind</h2>
            <p className="text-xl text-[#1A1C20]/70">We are designing MSME Twin to support your liquidity journey, unlike traditional banking.</p>
          </div>

          <div className="bg-white rounded-[2rem] border border-[#1A1C20]/10 shadow-xl overflow-hidden">
            <table className="w-full text-left border-collapse">
              <thead>
                <tr className="border-b border-[#1A1C20]/10 bg-[#F2EFE9]/50">
                  <th className="p-6 text-xl font-bold text-[#1A1C20]">Capability</th>
                  <th className="p-6 text-xl font-bold text-[#1A1C20]/50 text-center">Traditional Dashboard</th>
                  <th className="p-6 text-xl font-bold text-[#D0B063] text-center bg-[#D0B063]/5">MSME Digital Twin</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-[#1A1C20]/5">
                {[
                  ["Consent-Based Bank Sync", false, true],
                  ["Historical Cash Tracking", true, true],
                  ["GST Shortfall Prediction", false, true],
                  ["Buyer Delay Variance (AI)", false, true],
                  ["Automated Invoice Discounting", false, true],
                ].map((row, i) => (
                  <tr key={i} className="hover:bg-[#F2EFE9]/20 transition-colors">
                    <td className="p-6 text-lg font-medium text-[#1A1C20]/80">{row[0]}</td>
                    <td className="p-6 text-center">
                      {row[1] ? <Check className="w-6 h-6 mx-auto text-[#1A1C20]/30" /> : <X className="w-6 h-6 mx-auto text-rose-300" />}
                    </td>
                    <td className="p-6 text-center bg-[#D0B063]/5">
                      {row[2] ? <Check className="w-8 h-8 mx-auto text-[#D0B063] font-bold" /> : <X className="w-6 h-6 mx-auto text-rose-300" />}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </section>

      
      {/* How it Works (Under the Hood) */}
      <section className="py-32 px-6 bg-white border-y border-[#1A1C20]/10">
        <div className="max-w-6xl mx-auto">
          <div className="text-center mb-20">
            <h2 className="text-4xl md:text-5xl font-black text-[#1A1C20] mb-6 font-serif">
              Under the <span className="text-[#D0B063]">Hood.</span>
            </h2>
            <p className="text-xl text-[#1A1C20]/70 max-w-2xl mx-auto">
              A transparent look at how data flows securely from your bank to our AI engine.
            </p>
          </div>

          <div className="relative flex flex-col md:flex-row justify-between items-center gap-12 md:gap-4">
            {/* Connecting Line */}
            <div className="hidden md:block absolute top-1/2 left-0 w-full h-1 bg-gradient-to-r from-transparent via-[#D0B063]/30 to-transparent -translate-y-1/2 z-0"></div>

            {/* Step 1 */}
            <div className="relative z-10 flex flex-col items-center text-center max-w-xs">
              <div className="w-20 h-20 rounded-2xl bg-[#F2EFE9] border-2 border-[#D0B063] flex items-center justify-center mb-6 shadow-xl shadow-[#D0B063]/10">
                <ShieldCheck className="w-10 h-10 text-[#1A1C20]" />
              </div>
              <h3 className="text-2xl font-bold text-[#1A1C20] mb-3">1. Secure Consent</h3>
              <p className="text-[#1A1C20]/60">You grant read-only access via the RBI Account Aggregator framework. No passwords shared.</p>
            </div>

            {/* Step 2 */}
            <div className="relative z-10 flex flex-col items-center text-center max-w-xs">
              <div className="w-20 h-20 rounded-2xl bg-[#1A1C20] border-2 border-[#1A1C20] flex items-center justify-center mb-6 shadow-xl">
                <Activity className="w-10 h-10 text-[#D0B063]" />
              </div>
              <h3 className="text-2xl font-bold text-[#1A1C20] mb-3">2. AI Ingestion</h3>
              <p className="text-[#1A1C20]/60">Our Python engine parses 6 months of historical transactions and GST invoices to find patterns.</p>
            </div>

            {/* Step 3 */}
            <div className="relative z-10 flex flex-col items-center text-center max-w-xs">
              <div className="w-20 h-20 rounded-2xl bg-[#D0B063] border-2 border-[#D0B063] flex items-center justify-center mb-6 shadow-xl shadow-[#D0B063]/30">
                <BarChart3 className="w-10 h-10 text-[#1A1C20]" />
              </div>
              <h3 className="text-2xl font-bold text-[#1A1C20] mb-3">3. Actionable Twin</h3>
              <p className="text-[#1A1C20]/60">A 90-day predictive timeline is generated, highlighting exactly when you will face a cash crunch.</p>
            </div>
          </div>
        </div>
      </section>

      {/* Security & Trust Block */}
      <section className="py-24 px-6 bg-[#1A1C20] text-white overflow-hidden relative">
        <div className="absolute top-0 right-0 w-96 h-96 bg-[#D0B063]/10 rounded-full blur-[100px] pointer-events-none"></div>
        <div className="max-w-5xl mx-auto flex flex-col md:flex-row items-center gap-16">
          <div className="flex-1 space-y-8">
            <h2 className="text-4xl md:text-5xl font-black font-serif leading-tight">
              Bank-Grade Security. <br />
              <span className="text-[#D0B063]">Zero Data Retention.</span>
            </h2>
            <div className="space-y-6">
              <div className="flex items-start gap-4">
                <div className="w-10 h-10 rounded-full bg-emerald-500/10 flex items-center justify-center shrink-0">
                  <Check className="w-5 h-5 text-emerald-300" />
                </div>
                <div>
                  <h4 className="text-xl font-bold mb-1">RBI Compliant</h4>
                  <p className="text-white/60">Built strictly on the Sahamati Account Aggregator guidelines.</p>
                </div>
              </div>
              <div className="flex items-start gap-4">
                <div className="w-10 h-10 rounded-full bg-emerald-500/10 flex items-center justify-center shrink-0">
                  <Check className="w-5 h-5 text-emerald-300" />
                </div>
                <div>
                  <h4 className="text-xl font-bold mb-1">AES-256 Encryption</h4>
                  <p className="text-white/60">Your financial data is encrypted in transit and at rest.</p>
                </div>
              </div>
              <div className="flex items-start gap-4">
                <div className="w-10 h-10 rounded-full bg-emerald-500/10 flex items-center justify-center shrink-0">
                  <Check className="w-5 h-5 text-emerald-300" />
                </div>
                <div>
                  <h4 className="text-xl font-bold mb-1">We Predict, Then We Delete</h4>
                  <p className="text-white/60">You can revoke consent at any time. When you do, your data is wiped instantly.</p>
                </div>
              </div>
            </div>
          </div>
          <div className="flex-1 w-full relative">
            <div className="aspect-square max-w-sm mx-auto rounded-full border border-white/10 flex items-center justify-center relative">
               <div className="absolute inset-0 rounded-full border border-dashed border-white/20 animate-spin-slow"></div>
               <ShieldCheck className="w-32 h-32 text-[#D0B063]" />
            </div>
          </div>
        </div>
      </section>

      {/* FAQs */}
      <section className="py-32 px-6 bg-[#FCFDFD]">
        <div className="max-w-4xl mx-auto">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-black text-[#1A1C20] mb-4 font-serif">Common Questions</h2>
            <p className="text-xl text-[#1A1C20]/60">Everything you need to know about MSME Twin.</p>
          </div>
          <div className="space-y-6">
            {[
              {
                q: "Does this replace my accountant or CA?",
                a: "No. MSME Twin works alongside your CA. While your CA looks at the past to file taxes, MSME Twin looks at the future to ensure you have the cash to pay those taxes."
              },
              {
                q: "What if I have multiple bank accounts?",
                a: "Our Account Aggregator integration can sync with multiple FIPs (Financial Information Providers) simultaneously, merging all your cash flows into one holistic twin."
              },
              {
                q: "Do I have to upload invoices manually?",
                a: "Never. By connecting to the GSTN portal, we automatically pull your B2B invoices and match them against your bank inflows."
              }
            ].map((faq, i) => (
              <div key={i} className="p-8 rounded-2xl bg-white border border-[#1A1C20]/10 shadow-sm hover:shadow-md transition-shadow">
                <h3 className="text-2xl font-bold text-[#1A1C20] mb-3">{faq.q}</h3>
                <p className="text-lg text-[#1A1C20]/70 leading-relaxed">{faq.a}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-32 px-6 bg-[#1A1C20] text-center">
        <div className="max-w-3xl mx-auto">
          <h2 className="text-5xl md:text-6xl font-black text-white mb-8 font-serif">
            Ready to Budget with <span className="text-[#D0B063]">Purpose?</span>
          </h2>
          <p className="text-xl text-white/60 mb-12 leading-relaxed">
            Join the MSME Twin community and be the first to access the app, receive exclusive updates, and start your journey toward financial freedom.
          </p>
          <div className="flex justify-center">
             <Link href="/login" className="px-12 py-6 text-xl font-black text-[#1A1C20] bg-[#D0B063] rounded-full hover:bg-[#E3C376] transition-all shadow-2xl shadow-[#D0B063]/20 hover:-translate-y-1">
               Secure Login via Account Aggregator
             </Link>
          </div>
          
        </div>
      </section>

    </div>
  );
}
