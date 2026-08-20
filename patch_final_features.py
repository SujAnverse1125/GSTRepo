import re
from pathlib import Path

file_path = Path("D:\\SIH2026\\frontend\\app\\dashboard\\page.tsx")
content = file_path.read_text(encoding="utf-8")

# 1. Add Print Styles
print_styles = """      <style dangerouslySetInnerHTML={{__html: `
        @media print {
          @page { size: landscape; margin: 1cm; }
          body { background: white !important; -webkit-print-color-adjust: exact; }
          button, select, input { display: none !important; }
          .shadow-2xl, .shadow-sm, .shadow-xl { box-shadow: none !important; border: 1px solid #e5e7eb !important; }
          .bg-\\[\\#F2EFE9\\] { background: white !important; }
          .min-h-screen { min-height: auto !important; }
        }
      `}} />"""

if "<style dangerouslySetInnerHTML" not in content:
    content = content.replace(
        '<div className="min-h-screen bg-[#F2EFE9] text-[#1A1C20] font-sans selection:bg-[#D0B063]/30 p-4 md:p-8">',
        '<div className="min-h-screen bg-[#F2EFE9] text-[#1A1C20] font-sans selection:bg-[#D0B063]/30 p-4 md:p-8">\n' + print_styles
    )

# 2. Add PDF Button to Header
pdf_button = """                  <button onClick={() => {
                    const originalTitle = document.title;
                    document.title = "MSME_Digital_Twin_Report";
                    window.print();
                    document.title = originalTitle;
                  }} className="px-5 py-2.5 bg-white border border-[#1A1C20]/10 text-[#1A1C20] rounded-xl shadow-sm font-bold text-sm hover:border-[#D0B063] transition-colors hidden md:flex items-center gap-2">
                    <span className="text-lg">📄</span> {t.export_csv || "Download Report"}
                  </button>\n                  <select """

content = content.replace('                  <select ', pdf_button)

# 3. Add Reset Demo Button to Footer
reset_button = """          <p className="text-sm text-[#1A1C20]/60 mt-2">
            This Digital Twin is an analytical planning tool, not financial advice. All AI auto-financing recommendations carry risk. Data is minimized and never shared.
          </p>
          <button 
            onClick={() => { localStorage.clear(); window.location.href = '/'; }} 
            className="mt-6 text-xs font-bold text-rose-500/50 hover:text-rose-600 transition-colors uppercase tracking-widest"
          >
            [ Hard Reset Demo ]
          </button>"""

content = re.sub(
    r'<p className="text-sm text-\[#1A1C20\]/60 mt-2">\s*This Digital Twin is an analytical planning tool, not financial advice.*?<\/p>',
    reset_button,
    content,
    flags=re.DOTALL
)

file_path.write_text(content, encoding="utf-8")
print("PDF Print and Reset features added.")
