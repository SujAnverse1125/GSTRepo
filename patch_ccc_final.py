import re
from pathlib import Path

file_path = Path("D:\\SIH2026\\frontend\\app\\dashboard\\page.tsx")
content = file_path.read_text(encoding="utf-8")

# The CCC card JSX to inject
ccc_card = """
              <div className="bg-white rounded-[2rem] p-8 border-b-4 border-b-[#D0B063] border border-[#1A1C20]/10 shadow-sm flex items-center gap-6">
                <div className="w-16 h-16 rounded-2xl bg-[#D0B063]/10 flex items-center justify-center text-[#D0B063]">
                   <TrendingDown className="w-8 h-8" />
                </div>
                <div>
                  <p className="text-sm font-bold text-[#D0B063] uppercase tracking-wider mb-1">{t.ccc_title}</p>
                  <h3 className="text-3xl font-black font-serif">{metrics?.buyer_delay_days ? metrics.buyer_delay_days + 15 : 60} Days</h3>
                </div>
              </div>
"""

# Match the end of the 3rd card and inject the 4th card (CCC)
content = re.sub(
    r'(<p className="text-sm font-bold text-\[#1A1C20\]/50 uppercase tracking-wider mb-1">\{t\.buyer_delay\}</p>\s*<h3 className="text-3xl font-black font-serif">\{metrics\?\.buyer_delay_days \|\| 45\} Days</h3>\s*</div>\s*</div>)',
    r'\1\n' + ccc_card,
    content,
    flags=re.DOTALL
)

file_path.write_text(content, encoding="utf-8")
print("CCC Card forcefully appended to the grid!")
