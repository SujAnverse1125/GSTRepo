import re

file_path = "D:\\\\SIH2026\\\\frontend\\\\app\\\\dashboard\\\\page.tsx"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Add BarChart3 to the lucide-react import
old_import = "import { ShieldCheck, Database, Zap, FileWarning, ArrowRight, Server, Activity, CheckCircle2 } from 'lucide-react';"
new_import = "import { ShieldCheck, Database, Zap, FileWarning, ArrowRight, Server, Activity, CheckCircle2, BarChart3 } from 'lucide-react';"

content = content.replace(old_import, new_import)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Import fixed.")
