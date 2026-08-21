import re

file_path = "D:\\SIH2026\\frontend\\app\\login\\page.tsx"

with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

text = text.replace("import { supabase } from '../../utils/supabase';", "")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(text)

# Also let's safeguard utils/supabase.ts just in case it's imported elsewhere
supabase_path = "D:\\SIH2026\\frontend\\utils\\supabase.ts"
with open(supabase_path, "r", encoding="utf-8") as f:
    sup_text = f.read()

sup_text = sup_text.replace("const supabaseUrl = process.env.NEXT_PUBLIC_SUPABASE_URL || '';", "const supabaseUrl = process.env.NEXT_PUBLIC_SUPABASE_URL || 'https://dummy.supabase.co';")
sup_text = sup_text.replace("const supabaseAnonKey = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY || '';", "const supabaseAnonKey = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY || 'dummy';")

with open(supabase_path, "w", encoding="utf-8") as f:
    f.write(sup_text)

print("Removed supabase import and safeguarded initialization")
