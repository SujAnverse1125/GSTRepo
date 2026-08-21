const fs = require('fs');
let text = fs.readFileSync('D:/SIH2026/frontend/app/dashboard/page.tsx', 'utf8');

// 1. Add buyers state
const stateLine = `const [buyers, setBuyers] = useState<any[]>([]);`;
if (!text.includes(stateLine)) {
  text = text.replace('const [recentTxns, setRecentTxns]', stateLine + '\n  const [recentTxns, setRecentTxns]');
}

// 2. Set buyers on upload
const oldUpload = `setMetrics({
        current_balance: data.summary.cashOnHand,`;
const newUpload = `setBuyers(data.buyerBreakdown || []);\n      setMetrics({
        current_balance: data.summary.cashOnHand,`;
if (text.includes(oldUpload)) {
  text = text.replace(oldUpload, newUpload);
}

// 3. Replace the hardcoded JSX with dynamic mapping
const oldJsx = `<div>
                    <div className="flex justify-between text-sm font-bold mb-2">
                      <span className="text-[#1A1C20]">Reliance Retail Ltd.</span>
                      <span className="text-rose-600">68% of Receivables</span>
                    </div>
                    <div className="w-full h-3 bg-[#F2EFE9] rounded-full overflow-hidden">
                      <div className="h-full bg-rose-500 rounded-full" style={{ width: '68%' }}></div>
                    </div>
                  </div>
                  
                  <div>
                    <div className="flex justify-between text-sm font-bold mb-2">
                      <span className="text-[#1A1C20]">Tata Electronics</span>
                      <span className="text-[#D0B063]">22% of Receivables</span>
                    </div>
                    <div className="w-full h-3 bg-[#F2EFE9] rounded-full overflow-hidden">
                      <div className="h-full bg-[#D0B063] rounded-full" style={{ width: '22%' }}></div>
                    </div>
                  </div>
  
                  <div>
                    <div className="flex justify-between text-sm font-bold mb-2">
                      <span className="text-[#1A1C20]">Other SMEs</span>
                      <span className="text-emerald-500">10% of Receivables</span>
                    </div>
                    <div className="w-full h-3 bg-[#F2EFE9] rounded-full overflow-hidden">
                      <div className="h-full bg-emerald-500 rounded-full" style={{ width: '10%' }}></div>
                    </div>
                  </div>`;

const newJsx = `{buyers && buyers.length > 0 ? buyers.map((buyer, idx) => {
                    const colors = ['bg-rose-500', 'bg-[#D0B063]', 'bg-emerald-500'];
                    const textColors = ['text-rose-600', 'text-[#D0B063]', 'text-emerald-500'];
                    return (
                      <div key={idx}>
                        <div className="flex justify-between text-sm font-bold mb-2">
                          <span className="text-[#1A1C20]">{buyer.name.replace('Client Payment - ', '')}</span>
                          <span className={textColors[idx % 3]}>{Math.round(buyer.share)}% of Receivables</span>
                        </div>
                        <div className="w-full h-3 bg-[#F2EFE9] rounded-full overflow-hidden">
                          <div className={\`h-full rounded-full \${colors[idx % 3]}\`} style={{ width: \`\${buyer.share}%\` }}></div>
                        </div>
                      </div>
                    );
                  }) : (
                    <div className="text-sm font-bold text-[#1A1C20]/50 text-center py-4">No concentration data available</div>
                  )}`;

text = text.replace(oldJsx, newJsx);

fs.writeFileSync('D:/SIH2026/frontend/app/dashboard/page.tsx', text, 'utf8');
console.log('Fixed UI Concentration Risk to use dynamic state!');
