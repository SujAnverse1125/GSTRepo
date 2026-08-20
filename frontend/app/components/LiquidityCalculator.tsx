"use client";

import { useState } from 'react';
import { Calculator, CheckCircle2 } from 'lucide-react';

export default function LiquidityCalculator() {
  const [turnoverLakhs, setTurnoverLakhs] = useState(50);
  const [delayDays, setDelayDays] = useState(65);

  const formatTurnover = (val: number) => {
    return val >= 100 ? `₹${(val / 100).toFixed(2)} Crore` : `₹${val} Lakhs`;
  };

  const monthlyGst = (turnoverLakhs * 100000) * 0.18;
  const protectedCap = monthlyGst * (delayDays / 30);
  const penaltyAvoided = monthlyGst * 0.18 * 0.4; // Simplified penalty calculation

  return (
    <section className="py-24 px-6 lg:px-12 bg-white relative border-y border-[#1A1C20]/5">
      <div className="max-w-6xl mx-auto">
        <div className="text-center max-w-3xl mx-auto mb-16">
          <span className="text-xs font-bold text-[#D0B063] uppercase tracking-widest px-3 py-1 rounded-full bg-[#D0B063]/10 border border-[#D0B063]/20">
            Live ROI Calculator
          </span>
          <h2 className="text-3xl sm:text-5xl font-black text-[#1A1C20] mt-4 tracking-tight font-serif">
            How Much Liquidity Can <span className="text-[#D0B063]">MSME Twin</span> Protect?
          </h2>
          <p className="text-[#1A1C20]/60 text-lg mt-4 max-w-2xl mx-auto">
            Adjust the sliders below to calculate your estimated GST cash trap exposure based on your buyer payment delays.
          </p>
        </div>

        <div className="grid lg:grid-cols-12 gap-8 bg-[#F2EFE9] p-8 sm:p-12 rounded-[3rem] border border-[#1A1C20]/10 shadow-xl">
          
          {/* Controls Column */}
          <div className="lg:col-span-7 flex flex-col justify-between gap-10">
            
            {/* Slider 1: Turnover */}
            <div>
              <div className="flex justify-between items-center mb-4">
                <label className="text-base font-bold text-[#1A1C20]">Monthly Business Turnover</label>
                <span className="text-xl font-black font-serif text-[#D0B063]">{formatTurnover(turnoverLakhs)}</span>
              </div>
              <input 
                type="range" 
                min="10" max="500" step="5" 
                value={turnoverLakhs} 
                onChange={(e) => setTurnoverLakhs(Number(e.target.value))}
                className="w-full h-3 bg-white rounded-full appearance-none cursor-pointer border border-[#1A1C20]/10 shadow-inner accent-[#D0B063]"
              />
              <div className="flex justify-between text-xs font-bold text-[#1A1C20]/40 mt-3 uppercase tracking-wider">
                <span>₹10 Lakhs</span>
                <span>₹2.5 Crore</span>
                <span>₹5.0 Crore</span>
              </div>
            </div>

            {/* Slider 2: Buyer Delay */}
            <div>
              <div className="flex justify-between items-center mb-4">
                <label className="text-base font-bold text-[#1A1C20]">Average Buyer Payment Delay</label>
                <span className="text-xl font-black font-serif text-rose-500">{delayDays} Days</span>
              </div>
              <input 
                type="range" 
                min="15" max="120" step="1" 
                value={delayDays} 
                onChange={(e) => setDelayDays(Number(e.target.value))}
                className="w-full h-3 bg-white rounded-full appearance-none cursor-pointer border border-[#1A1C20]/10 shadow-inner accent-rose-500"
              />
              <div className="flex justify-between text-xs font-bold text-[#1A1C20]/40 mt-3 uppercase tracking-wider">
                <span>15 Days</span>
                <span>60 Days</span>
                <span>120 Days</span>
              </div>
            </div>

            <div className="p-5 rounded-2xl bg-white border border-[#1A1C20]/10 text-sm font-medium text-[#1A1C20]/60 flex items-start gap-3 shadow-sm">
              <Calculator className="w-6 h-6 text-[#D0B063] shrink-0" />
              <p>Calculation assumes standard 18% GST slab and 45-day statutory credit cycle under Section 43B(h) of the Income Tax Act.</p>
            </div>
          </div>

          {/* Calculated Output Column */}
          <div className="lg:col-span-5 rounded-[2rem] bg-[#1A1C20] p-8 flex flex-col justify-between border border-[#D0B063]/30 shadow-2xl relative overflow-hidden">
            {/* Background Glow */}
            <div className="absolute top-0 right-0 w-48 h-48 bg-[#D0B063]/20 rounded-full blur-3xl -translate-y-1/2 translate-x-1/4"></div>

            <div className="relative z-10">
              <span className="text-xs font-bold text-white/50 uppercase tracking-widest block mb-2">Quarterly Protected Capital</span>
              <div className="text-4xl sm:text-5xl font-black text-white font-serif">₹{Math.round(protectedCap).toLocaleString('en-IN')}</div>
              <div className="text-sm text-emerald-400 mt-2 font-bold flex items-center gap-2 bg-emerald-400/10 w-fit px-3 py-1 rounded-full border border-emerald-400/20">
                <CheckCircle2 className="w-4 h-4" />
                Protected from working capital freeze
              </div>
            </div>

            <div className="my-8 pt-8 border-t border-white/10 space-y-4 text-sm relative z-10">
              <div className="flex justify-between items-center text-white/70 font-medium">
                <span>Avg GST Locked per Month:</span>
                <span className="text-white font-bold text-base">₹{Math.round(monthlyGst).toLocaleString('en-IN')}</span>
              </div>
              <div className="flex justify-between items-center text-white/70 font-medium">
                <span>Risk Penalty Avoided:</span>
                <span className="text-emerald-400 font-bold text-base">₹{Math.round(penaltyAvoided).toLocaleString('en-IN')}/yr</span>
              </div>
            </div>

            <a href="/login" className="relative z-10 w-full py-4 rounded-xl bg-gradient-to-r from-[#D0B063] to-[#B8984C] text-[#1A1C20] font-black text-base tracking-tight transition-transform hover:-translate-y-1 shadow-lg text-center flex items-center justify-center">
              Sync My Account Aggregator
            </a>
          </div>

        </div>
      </div>
    </section>
  );
}
