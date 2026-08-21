import re

file_path = "D:\\SIH2026\\frontend\\app\\page.tsx"

with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

# Make alert icons brighter
text = text.replace("text-rose-400", "text-rose-300")
text = text.replace("text-emerald-400", "text-emerald-300")
text = text.replace("text-amber-400", "text-amber-300")

# Fix text colors for titles and descriptions inside the dark card
text = text.replace('<p className="font-bold text-sm">{alerts[alertIdx].title}</p>', '<p className="font-bold text-sm text-white">{alerts[alertIdx].title}</p>')
text = text.replace('<p className="opacity-70 text-xs mt-1">{alerts[alertIdx].desc}</p>', '<p className="text-white/80 text-xs mt-1">{alerts[alertIdx].desc}</p>')

with open(file_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Fixed landing page alert colors")
