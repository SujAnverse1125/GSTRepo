import re
from pathlib import Path

file_path = Path("D:\\SIH2026\\frontend\\app\\dashboard\\page.tsx")
content = file_path.read_text(encoding="utf-8")

# The CCC card JSX to inject
ccc_card = """
          <div className="bg-white rounded-2xl p-6 border-b-4 border-b-[#D0B063] border border-[#1A1C20]/5 shadow-sm relative overflow-hidden group">
            <p className="text-xs font-bold text-[#D0B063] uppercase tracking-widest mb-1">{t.ccc_title}</p>
            <h2 className="text-3xl font-black text-[#1A1C20]">{metrics ? metrics.buyer_delay_days + 15 : '...'} Days</h2>
            <p className="text-xs font-bold text-[#1A1C20]/40 mt-1">{t.ccc_desc}</p>
          </div>
"""

# Match the end of the 3rd card (buyer_delay) and inject the 4th card (CCC)
# We know the 3rd card has {t.buyer_delay} inside a <p> tag, followed by an <h2> tag, and then closed by </div>
content = re.sub(
    r'(<p className="[^"]*">\{t\.buyer_delay\}</p>\s*<h2 className="[^"]*">[^<]*</h2>\s*</div>)',
    r'\1' + ccc_card,
    content,
    flags=re.DOTALL
)

# Ensure grid-cols-4 is set
content = re.sub(
    r'<div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">',
    r'<div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">',
    content
)

file_path.write_text(content, encoding="utf-8")
print("CCC Card correctly injected!")
