import re
from pathlib import Path

file_path = Path("D:\\SIH2026\\frontend\\app\\dashboard\\page.tsx")
content = file_path.read_text(encoding="utf-8")

# 1. Add state for recentTxns
old_state = "const [chartData, setChartData] = useState<any[]>([]);"
new_state = """const [chartData, setChartData] = useState<any[]>([]);
  const [recentTxns, setRecentTxns] = useState<any[]>([
    { source: "GSTN Inv #1042", amount: "₹1,00,000", status: "Unpaid", ai: "Delayed (Day 45)", type: "warning" },
    { source: "SBI Bank Statement", amount: "₹18,000", status: "Tax Due", ai: "Day 20", type: "danger" },
    { source: "GSTN Inv #1041", amount: "₹45,000", status: "Settled", ai: "Paid on time", type: "success" }
  ]);"""
if "const [recentTxns" not in content:
    content = content.replace(old_state, new_state)

# 2. Update handleFileUpload to save recentTxns
old_metrics = """        setMetrics({
          current_balance: data.summary.cashOnHand,
          gst_due: data.summary.gstDue,
          lowest_projected_balance: data.summary.minProjectedBalance,
          buyer_delay_days: 45
        });"""

new_metrics = """        setMetrics({
          current_balance: data.summary.cashOnHand,
          gst_due: data.summary.gstDue,
          lowest_projected_balance: data.summary.minProjectedBalance,
          buyer_delay_days: 45
        });
        if (data.recentTxns && data.recentTxns.length > 0) {
          setRecentTxns(data.recentTxns);
        }"""
content = content.replace(old_metrics, new_metrics)

# 3. Update the HTML table to map over recentTxns
old_table = """                  <tbody className="divide-y divide-[#1A1C20]/5">
                    <tr className="hover:bg-[#F2EFE9]/30 transition-colors">
                      <td className="py-4 font-bold text-[#1A1C20]">GSTN Inv #1042</td>
                      <td className="py-4 text-[#1A1C20]/80">₹1,00,000</td>
                      <td className="py-4"><span className="px-2 py-1 bg-amber-100 text-amber-700 text-xs font-bold rounded-full">Unpaid</span></td>
                      <td className="py-4 text-right text-rose-600 font-bold">Delayed (Day 45)</td>
                    </tr>
                    <tr className="hover:bg-[#F2EFE9]/30 transition-colors">
                      <td className="py-4 font-bold text-[#1A1C20]">SBI Bank Statement</td>
                      <td className="py-4 text-[#1A1C20]/80">-₹18,000</td>
                      <td className="py-4"><span className="px-2 py-1 bg-rose-100 text-rose-700 text-xs font-bold rounded-full">Tax Due</span></td>
                      <td className="py-4 text-right text-[#1A1C20]/80 font-bold">Day 20</td>
                    </tr>
                    <tr className="hover:bg-[#F2EFE9]/30 transition-colors">
                      <td className="py-4 font-bold text-[#1A1C20]">GSTN Inv #1041</td>
                      <td className="py-4 text-[#1A1C20]/80">₹45,000</td>
                      <td className="py-4"><span className="px-2 py-1 bg-emerald-100 text-emerald-700 text-xs font-bold rounded-full">Settled</span></td>
                      <td className="py-4 text-right text-emerald-600 font-bold">Paid on time</td>
                    </tr>
                  </tbody>"""

new_table = """                  <tbody className="divide-y divide-[#1A1C20]/5">
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
content = content.replace(old_table, new_table)

file_path.write_text(content, encoding="utf-8")
print("Frontend updated to display dynamic table data.")
