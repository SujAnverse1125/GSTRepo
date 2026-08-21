import re
from pathlib import Path

file_path = Path("D:\\SIH2026\\backend\\main.py")
content = file_path.read_text(encoding="utf-8")

old_code = "for r in reversed(rows[-3:]):"
new_code = "for r in reversed(rows[-50:]):"

content = content.replace(old_code, new_code)
file_path.write_text(content, encoding="utf-8")
print("Backend updated to parse 50 rows instead of 3.")
