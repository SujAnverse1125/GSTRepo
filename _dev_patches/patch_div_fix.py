import re
from pathlib import Path

file_path = Path("D:\\SIH2026\\frontend\\app\\dashboard\\page.tsx")
content = file_path.read_text(encoding="utf-8")

# Fix the extra div bug
content = content.replace("</tbody></table></div></div>", "</tbody></table></div>")

file_path.write_text(content, encoding="utf-8")
print("Removed extra closing div.")
