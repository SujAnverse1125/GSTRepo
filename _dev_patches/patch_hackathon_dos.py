import re
from pathlib import Path

file_path = Path("D:\\SIH2026\\frontend\\app\\dashboard\\page.tsx")
content = file_path.read_text(encoding="utf-8")

# 1. Add Language State & Translations
lang_state = """  // Language State
  const [lang, setLang] = useState<'en' | 'hi' | 'or'>('en');
  
  const translations = {
    en: {
      title: "Command Center",
      subtitle: "Your MSME Digital Twin is live.",
      ccc_title: "Cash Conversion Cycle",
      ccc_desc: "Days to convert inventory to cash"
    },
    hi: {
      title: "कमांड सेंटर",
      subtitle: "आपका MSME डिजिटल ट्विन लाइव है।",
      ccc_title: "नकद रूपांतरण चक्र (CCC)",
      ccc_desc: "इन्वेंट्री को नकदी में बदलने के दिन"
    },
    or: {
      title: "କମାଣ୍ଡ ସେଣ୍ଟର",
      subtitle: "ଆପଣଙ୍କର MSME ଡିଜିଟାଲ୍ ଟ୍ୱିନ୍ ଲାଇଭ୍ ଅଛି।",
      ccc_title: "ନଗଦ ରୂପାନ୍ତର ଚକ୍ର (CCC)",
      ccc_desc: "ସାମଗ୍ରୀକୁ ନଗଦରେ ପରିଣତ କରିବାର ଦିନ"
    }
  };
  const t = translations[lang];"""

content = re.sub(r'const \[showUploadModal, setShowUploadModal\] = useState\(false\);', lang_state + '\n  const [showUploadModal, setShowUploadModal] = useState(false);', content, count=1)

# 2. Update Header Title to use translation & Add Language Selector
old_header = """          <div>
            <h1 className="text-3xl font-black font-serif text-[#1A1C20] tracking-tight">Command Center</h1>
            <p className="text-[#1A1C20]/60 font-medium">Your MSME Digital Twin is live.</p>
          </div>
          
          <div className="flex items-center gap-4">
            <button className="flex items-center gap-2 bg-[#25D366]/10 text-[#25D366] px-4 py-2 rounded-full font-bold text-sm hover:bg-[#25D366]/20 transition-colors">
              <MessageSquare className="w-4 h-4" /> WhatsApp Briefs: ON
            </button>"""

new_header = """          <div>
            <h1 className="text-3xl font-black font-serif text-[#1A1C20] tracking-tight">{t.title}</h1>
            <p className="text-[#1A1C20]/60 font-medium">{t.subtitle}</p>
          </div>
          
          <div className="flex items-center gap-3">
            <select 
              value={lang} 
              onChange={(e) => setLang(e.target.value as any)}
              className="bg-white border border-[#1A1C20]/10 text-[#1A1C20] px-3 py-2 rounded-lg font-bold text-sm outline-none cursor-pointer"
            >
              <option value="en">English</option>
              <option value="hi">हिंदी (Hindi)</option>
              <option value="or">ଓଡ଼ିଆ (Odia)</option>
            </select>
          
            <button 
              onClick={() => alert("✅ Morning Brief sent to +91 98*** **432 on WhatsApp!")}
              className="flex items-center gap-2 bg-[#25D366]/10 text-[#25D366] px-4 py-2 rounded-full font-bold text-sm hover:bg-[#25D366]/20 transition-colors"
            >
              <MessageSquare className="w-4 h-4" /> WhatsApp Briefs: ON
            </button>"""

content = content.replace(old_header, new_header)

# 3. Add CCC to metrics grid (Change from grid-cols-3 to grid-cols-4)
old_metrics = """        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-10">
          <div className="bg-white rounded-2xl p-6 border border-[#1A1C20]/5 shadow-sm relative overflow-hidden group">
            <div className="absolute top-0 right-0 p-4 opacity-10 group-hover:opacity-20 transition-opacity">
              <Wallet className="w-16 h-16" />
            </div>
            <p className="text-sm font-bold text-[#1A1C20]/40 uppercase tracking-widest mb-1">Current Balance</p>
            <h2 className="text-4xl font-black text-[#1A1C20]">₹{metrics ? metrics.current_balance.toLocaleString('en-IN') : '...'}</h2>
          </div>

          <div className="bg-white rounded-2xl p-6 border border-[#1A1C20]/5 shadow-sm relative overflow-hidden group">
            <div className="absolute top-0 right-0 p-4 opacity-10 group-hover:opacity-20 transition-opacity">
              <AlertTriangle className="w-16 h-16" />
            </div>
            <p className="text-sm font-bold text-[#1A1C20]/40 uppercase tracking-widest mb-1">Shortfall Risk</p>
            <h2 className="text-4xl font-black text-rose-600">Critical</h2>
          </div>

          <div className="bg-white rounded-2xl p-6 border border-[#1A1C20]/5 shadow-sm relative overflow-hidden group">
            <div className="absolute top-0 right-0 p-4 opacity-10 group-hover:opacity-20 transition-opacity">
              <TrendingDown className="w-16 h-16" />
            </div>
            <p className="text-sm font-bold text-[#1A1C20]/40 uppercase tracking-widest mb-1">Avg Buyer Delay</p>
            <h2 className="text-4xl font-black text-[#1A1C20]">{metrics ? metrics.buyer_delay_days : '...'} Days</h2>
          </div>
        </div>"""

new_metrics = """        <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-10">
          <div className="bg-white rounded-2xl p-6 border border-[#1A1C20]/5 shadow-sm relative overflow-hidden group">
            <div className="absolute top-0 right-0 p-4 opacity-10 group-hover:opacity-20 transition-opacity">
              <Wallet className="w-16 h-16" />
            </div>
            <p className="text-sm font-bold text-[#1A1C20]/40 uppercase tracking-widest mb-1">Current Balance</p>
            <h2 className="text-4xl font-black text-[#1A1C20]">₹{metrics ? metrics.current_balance.toLocaleString('en-IN') : '...'}</h2>
          </div>

          <div className="bg-white rounded-2xl p-6 border border-[#1A1C20]/5 shadow-sm relative overflow-hidden group">
            <div className="absolute top-0 right-0 p-4 opacity-10 group-hover:opacity-20 transition-opacity">
              <AlertTriangle className="w-16 h-16" />
            </div>
            <p className="text-sm font-bold text-[#1A1C20]/40 uppercase tracking-widest mb-1">Shortfall Risk</p>
            <h2 className="text-4xl font-black text-rose-600">Critical</h2>
          </div>

          <div className="bg-white rounded-2xl p-6 border border-[#1A1C20]/5 shadow-sm relative overflow-hidden group">
            <div className="absolute top-0 right-0 p-4 opacity-10 group-hover:opacity-20 transition-opacity">
              <TrendingDown className="w-16 h-16" />
            </div>
            <p className="text-sm font-bold text-[#1A1C20]/40 uppercase tracking-widest mb-1">Avg Buyer Delay</p>
            <h2 className="text-3xl font-black text-[#1A1C20]">{metrics ? metrics.buyer_delay_days : '...'} Days</h2>
          </div>
          
          <div className="bg-white rounded-2xl p-6 border-b-4 border-b-[#D0B063] border border-[#1A1C20]/5 shadow-sm relative overflow-hidden group">
            <p className="text-xs font-bold text-[#D0B063] uppercase tracking-widest mb-1">{t.ccc_title}</p>
            <h2 className="text-3xl font-black text-[#1A1C20]">{metrics ? metrics.buyer_delay_days + 15 : '...'} Days</h2>
            <p className="text-xs font-bold text-[#1A1C20]/40 mt-1">{t.ccc_desc}</p>
          </div>
        </div>"""

content = content.replace(old_metrics, new_metrics)

file_path.write_text(content, encoding="utf-8")
print("CCC Metric, Multilingual Support, and WhatsApp Fallback added.")
