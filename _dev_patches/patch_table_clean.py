import re
from pathlib import Path

file_path = Path("D:\\SIH2026\\frontend\\app\\dashboard\\page.tsx")
content = file_path.read_text(encoding="utf-8")

# Let's completely wipe and replace the RecentTxns state to ensure it's clean
new_state = """  const [recentTxns, setRecentTxns] = useState<any[]>([
    { source: "GSTN Inv #1042", amount: "₹1,00,000", status: "Unpaid", ai: "Delayed", type: "warning" },
    { source: "SBI Bank Statement", amount: "-₹18,000", status: "Tax Due", ai: "Day 20", type: "danger" },
    { source: "GSTN Inv #1041", amount: "₹45,000", status: "Settled", ai: "On time", type: "success" }
  ]);"""

content = re.sub(r'const \[recentTxns, setRecentTxns\].*?\]\);', new_state, content, flags=re.DOTALL)

# Let's completely wipe and replace the table HTML
table_start = '<tbody className="divide-y divide-[#1A1C20]/5">'
table_end = '</tbody>'
new_table = """<tbody className="divide-y divide-[#1A1C20]/5">
                    {recentTxns.map((txn, i) => (
                      <tr key={i} className="hover:bg-[#F2EFE9]/30 transition-colors">
                        <td className="py-4 font-bold text-[#1A1C20]">{txn.source}</td>
                        <td className="py-4 text-[#1A1C20]/80">{txn.amount}</td>
                        <td className="py-4">
                          <span className={`px-2 py-1 text-xs font-bold rounded-full ${txn.type === 'success' ? 'bg-emerald-100 text-emerald-700' : txn.type === 'warning' ? 'bg-amber-100 text-amber-700' : 'bg-rose-100 text-rose-700'}`}>
                            {txn.status}
                          </span>
                        </td>
                        <td className="py-4 text-right text-[#1A1C20]/80 font-bold">{txn.ai}</td>
                      </tr>
                    ))}
                  </tbody>"""

content = re.sub(r'<tbody className="divide-y divide-\[#1A1C20\]/5">.*?</tbody>', new_table, content, flags=re.DOTALL)

file_path.write_text(content, encoding="utf-8")
print("Cleaned up recentTxns state and table rendering.")
