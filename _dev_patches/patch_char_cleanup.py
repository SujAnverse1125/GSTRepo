import re
from pathlib import Path

file_path = Path("D:\\SIH2026\\frontend\\app\\dashboard\\page.tsx")
content = file_path.read_text(encoding="utf-8")

# Fix corrupted Rupee symbols and weird chars
content = re.sub(r',1\{totalDeficit', r'₹{totalDeficit', content)
content = re.sub(r'o </button>', r'✕</button>', content)
content = re.sub(r'dY" Export CSV', r'📥 Export CSV', content)
content = re.sub(r'dY"\s*Upload Corrected Sheet', r'📤 Upload Corrected Sheet', content)

# I should also fix the table default state just in case it got corrupted
content = re.sub(r',11,00,000', r'₹1,00,000', content)
content = re.sub(r',118,000', r'-₹18,000', content)
content = re.sub(r',145,000', r'₹45,000', content)

file_path.write_text(content, encoding="utf-8")
print("Cleaned up corrupted characters.")
