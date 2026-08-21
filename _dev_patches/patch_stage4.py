import re

file_path = "D:\\\\SIH2026\\\\frontend\\\\app\\\\dashboard\\\\page.tsx"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add Export/Import Buttons to the Data Table
old_table_header = """            <div className="bg-white rounded-[2rem] border border-[#1A1C20]/10 shadow-sm p-8">
              <h3 className="text-2xl font-black font-serif mb-6 text-[#1A1C20]">Account Aggregator Data</h3>"""

new_table_header = """            <div className="bg-white rounded-[2rem] border border-[#1A1C20]/10 shadow-sm p-8">
              <div className="flex flex-col md:flex-row md:items-center justify-between mb-6 gap-4">
                <h3 className="text-2xl font-black font-serif text-[#1A1C20]">Account Aggregator Data</h3>
                <div className="flex gap-2">
                  <button onClick={() => alert("Downloading bank_data.csv...")} className="px-4 py-2 text-sm font-bold bg-[#F2EFE9] border border-[#1A1C20]/10 text-[#1A1C20] rounded-lg hover:bg-[#e8e4dc] transition-colors shadow-sm">
                    📥 Export CSV
                  </button>
                  <button onClick={() => alert("Opening file picker... Once uploaded, the Twin Engine will recalculate.")} className="px-4 py-2 text-sm font-bold bg-[#1A1C20] text-white rounded-lg hover:bg-[#2D3139] transition-colors shadow-sm">
                    📤 Upload Corrected Sheet
                  </button>
                </div>
              </div>"""
content = content.replace(old_table_header, new_table_header)

# 2. Add WhatsApp Integration toggle to the Header
old_header = """              <div className="flex gap-4">
                <button onClick={handleRevokeConsent} className="px-5 py-2.5 bg-white border border-rose-200 text-rose-600 rounded-xl shadow-sm font-bold text-sm hover:bg-rose-50 transition-colors">
                  Revoke Consent & Wipe Data
                </button>
                <div className="px-5 py-2.5 bg-[#1A1C20] text-white rounded-xl shadow-sm flex items-center gap-3">
                  <div className="w-2 h-2 bg-emerald-400 rounded-full animate-pulse"></div>
                  <span className="font-bold text-sm">Live: SBI & GSTN</span>
                </div>
              </div>"""

new_header = """              <div className="flex gap-4">
                <button onClick={() => alert("WhatsApp Morning Briefs activated. You will receive an 8 AM daily cash summary.")} className="px-5 py-2.5 bg-emerald-50 border border-emerald-200 text-emerald-700 rounded-xl shadow-sm font-bold text-sm hover:bg-emerald-100 transition-colors hidden md:flex items-center gap-2">
                  <span>💬 WhatsApp Briefs: ON</span>
                </button>
                <button onClick={handleRevokeConsent} className="px-5 py-2.5 bg-white border border-rose-200 text-rose-600 rounded-xl shadow-sm font-bold text-sm hover:bg-rose-50 transition-colors">
                  Revoke Consent
                </button>
                <div className="px-5 py-2.5 bg-[#1A1C20] text-white rounded-xl shadow-sm flex items-center gap-3">
                  <div className="w-2 h-2 bg-emerald-400 rounded-full animate-pulse"></div>
                  <span className="font-bold text-sm hidden md:inline">Live: SBI & GSTN</span>
                </div>
              </div>"""
content = content.replace(old_header, new_header)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Stage 4 buttons added.")
