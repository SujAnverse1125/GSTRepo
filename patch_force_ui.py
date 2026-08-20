import re
from pathlib import Path

file_path = Path("D:\\SIH2026\\frontend\\app\\dashboard\\page.tsx")
content = file_path.read_text(encoding="utf-8")

# 1. Inject Language Dropdown
dropdown_jsx = """
                  <select 
                    value={lang} 
                    onChange={(e) => setLang(e.target.value as any)}
                    className="bg-white border border-[#1A1C20]/10 text-[#1A1C20] px-3 py-2 rounded-xl font-bold text-sm outline-none cursor-pointer hover:border-[#D0B063] transition-colors"
                  >
                    <option value="en">English</option>
                    <option value="hi">हिंदी (Hindi)</option>
                    <option value="or">ଓଡ଼ିଆ (Odia)</option>
                  </select>"""

if "<select" not in dropdown_jsx or "value={lang}" not in content:
    content = re.sub(
        r'(<div className="flex gap-4">)',
        r'\1' + dropdown_jsx,
        content
    )

# 2. Upgrade Grid from 3 to 4
content = re.sub(
    r'<div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">',
    r'<div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">',
    content
)

# 3. Inject CCC Card
ccc_card = """
          <div className="bg-white rounded-2xl p-6 border-b-4 border-b-[#D0B063] border border-[#1A1C20]/5 shadow-sm relative overflow-hidden group">
            <p className="text-xs font-bold text-[#D0B063] uppercase tracking-widest mb-1">{t.ccc_title}</p>
            <h2 className="text-3xl font-black text-[#1A1C20]">{metrics ? metrics.buyer_delay_days + 15 : '...'} Days</h2>
            <p className="text-xs font-bold text-[#1A1C20]/40 mt-1">{t.ccc_desc}</p>
          </div>
"""

# Find the end of the 3rd card (Avg Buyer Delay)
# We look for "Avg Buyer Delay" followed by </h2> and then </div>
content = re.sub(
    r'(<p className="text-sm font-bold text-\[#1A1C20\]/40 uppercase tracking-widest mb-1">Avg Buyer Delay</p>.*?</h2>\s*</div>)',
    r'\1' + ccc_card,
    content,
    flags=re.DOTALL
)

# 4. Fix WhatsApp button action
content = re.sub(
    r'onClick=\{\(\) => alert\("WhatsApp Morning Briefs activated.*?"\)\}',
    r'onClick={() => alert("✅ Morning Brief sent to +91 98*** **432 on WhatsApp!")}',
    content
)

file_path.write_text(content, encoding="utf-8")
print("Targeted regex applied for CCC, Dropdown, and WhatsApp.")
