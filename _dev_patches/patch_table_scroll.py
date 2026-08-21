import re
from pathlib import Path

file_path = Path("D:\\SIH2026\\frontend\\app\\dashboard\\page.tsx")
content = file_path.read_text(encoding="utf-8")

old_table_start = """              <table className="w-full text-left">
                <thead className="text-xs text-[#1A1C20]/40 uppercase tracking-widest border-b border-[#1A1C20]/10">"""

new_table_start = """              <div className="overflow-x-auto overflow-y-auto max-h-[400px] pr-2 custom-scrollbar">
                <table className="w-full text-left">
                  <thead className="text-xs text-[#1A1C20]/40 uppercase tracking-widest border-b border-[#1A1C20]/10 sticky top-0 bg-white shadow-sm z-10">"""

old_table_end = """                  </tbody>
              </table>
            </div>"""

new_table_end = """                  </tbody>
                </table>
              </div>
            </div>"""

# Safely replace
if "max-h-[400px]" not in content:
    content = content.replace(old_table_start, new_table_start)
    # The end replacement can be tricky because of div closing tags.
    # Let's use regex for the end replacement to be safe.
    content = re.sub(r'</tbody>\s*</table>\s*</div>', r'</tbody></table></div></div>', content)
    file_path.write_text(content, encoding="utf-8")
    print("Frontend table wrapper added.")
else:
    print("Frontend already patched.")
