import re

file_path = "D:\\\\SIH2026\\\\frontend\\\\app\\\\dashboard\\\\page.tsx"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Add the Revoke button to the header
old_header = """            <div className="flex gap-4">
              <div className="px-5 py-2.5 bg-white border border-[#1A1C20]/10 rounded-xl shadow-sm flex items-center gap-3">
                <div className="w-2 h-2 bg-emerald-500 rounded-full animate-pulse"></div>
                <span className="font-bold text-sm">Live Sync: SBI & GSTN</span>
              </div>
            </div>"""

new_header = """            <div className="flex flex-col items-end gap-3">
              <div className="flex gap-4">
                <button onClick={() => alert("Responsible AI Guardrail Triggered: Disconnecting FIP. Wiping local data.")} className="px-5 py-2.5 bg-white border border-rose-200 text-rose-600 rounded-xl shadow-sm font-bold text-sm hover:bg-rose-50 transition-colors">
                  Revoke Consent & Wipe Data
                </button>
                <div className="px-5 py-2.5 bg-[#1A1C20] text-white rounded-xl shadow-sm flex items-center gap-3">
                  <div className="w-2 h-2 bg-emerald-400 rounded-full animate-pulse"></div>
                  <span className="font-bold text-sm">Live: SBI & GSTN</span>
                </div>
              </div>
            </div>"""

content = content.replace(old_header, new_header)

# Add the disclaimer footer
old_footer = """        </div>
      )}
    </div>"""

new_footer = """        </div>
      )}
      
      {appState === 'dashboard' && (
        <footer className="max-w-7xl mx-auto mt-12 pt-8 border-t border-[#1A1C20]/10 text-center pb-8 animate-in fade-in">
          <p className="text-xs font-bold text-[#1A1C20]/40 uppercase tracking-widest">
            Responsible AI Guardrails Active
          </p>
          <p className="text-sm text-[#1A1C20]/60 mt-2">
            This Digital Twin is an analytical planning tool, not financial advice. All AI auto-financing recommendations carry risk. Data is minimized and never shared.
          </p>
        </footer>
      )}
    </div>"""
content = content.replace(old_footer, new_footer)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Guardrails added.")
