import re
from pathlib import Path

file_path = Path("D:\\SIH2026\\frontend\\app\\page.tsx")
content = file_path.read_text(encoding="utf-8")

# Add missing lucide imports
content = content.replace("from \"lucide-react\";", ", CheckCircle2, FileWarning } from \"lucide-react\";")
content = content.replace("Activity, CheckCircle2", "Activity")

file_path.write_text(content, encoding="utf-8")
print("Imports fixed.")
