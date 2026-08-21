import re
from pathlib import Path

file_path = Path("D:\\SIH2026\\frontend\\app\\page.tsx")
content = file_path.read_text(encoding="utf-8")

# 1. Update the Navbar
old_nav = """        <div className="flex items-center gap-6">
          <Link href="/login" className="hidden md:block text-sm font-semibold text-[#1A1C20]/70 hover:text-[#1A1C20] transition-colors">
            Our Mission
          </Link>
          <Link href="/login" className="px-6 py-3 text-sm font-bold text-white bg-[#1A1C20] rounded-full hover:bg-[#2D3139] transition-all shadow-lg hover:-translate-y-0.5">
            Join Waitlist
          </Link>
        </div>"""

new_nav = """        <div className="flex items-center gap-6">
          <div className="hidden md:flex gap-6 text-sm font-bold text-[#1A1C20]/60">
            <Link href="#problem" className="hover:text-[#1A1C20] transition-colors">The Problem</Link>
            <Link href="#features" className="hover:text-[#1A1C20] transition-colors">How it Works</Link>
          </div>
          <Link href="/login" className="px-6 py-3 text-sm font-bold text-white bg-[#1A1C20] rounded-full hover:bg-[#2D3139] transition-all shadow-lg hover:-translate-y-0.5 flex items-center gap-2">
            Launch Demo <ArrowRight className="w-4 h-4" />
          </Link>
        </div>"""

content = content.replace(old_nav, new_nav)

# 2. Update the Hero Left Side (Text/Buttons)
old_hero_left = """        <div className="flex-1 text-center lg:text-left animate-in fade-in slide-in-from-bottom-8 duration-1000">
          <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-[#D0B063]/10 border border-[#D0B063]/30 text-[#8C7335] text-sm font-bold mb-8">
            <ShieldCheck className="w-4 h-4" /> 
            Powered by India Stack
          </div>
          <h1 className="text-5xl md:text-7xl font-black tracking-tight text-[#1A1C20] mb-6 leading-[1.1] font-serif">
            Where Data Meets <br />
            <span className="text-[#D0B063]">Liquidity.</span>
          </h1>
          <p className="text-xl text-[#1A1C20]/70 mb-10 max-w-xl mx-auto lg:mx-0 leading-relaxed font-medium">
            India's first AI-powered Digital Twin for MSMEs. We predict your cash flow 90 days in advance so you never miss a GST payment or payroll again.
          </p>
          <div className="flex flex-col sm:flex-row items-center justify-center lg:justify-start gap-4">
            <Link href="/login" className="w-full sm:w-auto px-8 py-4 text-base font-bold text-white bg-[#1A1C20] rounded-full hover:bg-[#2D3139] transition-all shadow-xl hover:-translate-y-1">
              Start Simulating Now
            </Link>
            <Link href="/login" className="w-full sm:w-auto px-8 py-4 text-base font-bold text-[#1A1C20] bg-transparent border-2 border-[#1A1C20]/10 rounded-full hover:bg-[#1A1C20]/5 transition-all">
              Get the Free Guide
            </Link>
          </div>
        </div>"""

new_hero_left = """        <div className="flex-1 text-center lg:text-left animate-in fade-in slide-in-from-bottom-8 duration-1000 mt-10">
          <div className="flex flex-wrap items-center justify-center lg:justify-start gap-3 mb-8">
            <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-[#D0B063]/10 border border-[#D0B063]/30 text-[#8C7335] text-sm font-bold">
              🏆 Built for SIH 2026
            </div>
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
        </div>"""

content = content.replace(old_hero_left, new_hero_left)

# 3. Update the Hero Right Side (Abstract Image)
old_hero_right = """        <div className="flex-1 relative w-full max-w-lg lg:max-w-none">
          {/* Abstract Hero Image Replacement */}
          <div className="relative w-full aspect-square rounded-[3rem] bg-gradient-to-tr from-[#1A1C20] to-[#2D3139] shadow-2xl overflow-hidden p-8 flex flex-col justify-between transform rotate-2 hover:rotate-0 transition-transform duration-700">
             <div className="flex justify-between items-start">
               <div className="w-16 h-16 rounded-2xl bg-[#D0B063] flex items-center justify-center shadow-lg">
                 <BarChart3 className="w-8 h-8 text-[#1A1C20]" />
               </div>
               <div className="px-4 py-2 bg-white/10 backdrop-blur-md rounded-full text-white/90 text-sm font-semibold border border-white/10">
                 Live Twin Active
               </div>
             </div>
             <div className="space-y-4">
               <div className="h-2 w-1/3 bg-white/20 rounded-full"></div>
               <h3 className="text-4xl font-serif text-white">,11,84,000</h3>
               <div className="h-16 w-full bg-gradient-to-r from-rose-500/80 to-rose-400/20 rounded-xl border border-rose-500/30 flex items-center px-6">
                 <span className="text-white font-bold tracking-widest text-sm">SHORTFALL ALERT: DAY 20</span>
               </div>
             </div>
          </div>
        </div>"""

new_hero_right = """        <div className="flex-1 relative w-full max-w-lg lg:max-w-none mt-10">
          <div className="relative w-full h-[500px] flex items-center justify-center">
            
            {/* Background Blob */}
            <div className="absolute inset-0 bg-[#D0B063]/20 blur-3xl rounded-full opacity-50 mix-blend-multiply animate-pulse"></div>
            
            {/* Main Floating UI */}
            <div className="relative z-10 w-full max-w-md bg-[#1A1C20] rounded-[2rem] shadow-2xl border border-white/10 p-8 transform rotate-3 hover:rotate-0 transition-transform duration-500 overflow-hidden">
              
              {/* Header */}
              <div className="flex justify-between items-center mb-8 border-b border-white/10 pb-4">
                <div className="flex items-center gap-3">
                  <div className="w-10 h-10 bg-emerald-500/20 rounded-full flex items-center justify-center text-emerald-400">
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
                    <div key={i} className={`flex-1 rounded-t-sm ${h < 20 ? 'bg-rose-500' : 'bg-[#D0B063]'}`} style={{ height: `${h}%` }}></div>
                  ))}
                </div>
              </div>

              {/* Alert Card */}
              <div className="bg-rose-500/10 border border-rose-500/20 rounded-xl p-4 flex items-start gap-4">
                <div className="bg-rose-500/20 p-2 rounded-lg text-rose-400 mt-1">
                  <FileWarning className="w-5 h-5" />
                </div>
                <div>
                  <p className="text-rose-400 font-bold text-sm">GST Deficit Predicted</p>
                  <p className="text-rose-400/70 text-xs mt-1">A ₹2.5L shortfall is expected on Day 18 due to Buyer Delay.</p>
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
        </div>"""

# Safely replace, accounting for corrupted ₹ characters in old text if any
content = re.sub(r'<div className="flex-1 relative w-full max-w-lg lg:max-w-none">.*?</div>\s*</section>', new_hero_right + '\n      </section>', content, flags=re.DOTALL)

file_path.write_text(content, encoding="utf-8")
print("Landing page successfully revamped for the Hackathon!")
