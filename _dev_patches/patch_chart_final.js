const fs = require('fs');
const file = 'D:\\SIH2026\\frontend\\app\\page.tsx';
let text = fs.readFileSync(file, 'utf8');

const startIdx = text.indexOf('{[40, 50, 60, 45');
const endIdx = text.indexOf('))}', startIdx) + 3;

if (startIdx !== -1 && endIdx !== -1) {
  const animatedBars = `{[40, 50, 60, 45, 30, 15, 5, 20, 50, 70, 80, 90].map((h, i) => (
                    <div 
                      key={i} 
                      className={\`flex-1 rounded-t-sm live-bar \${h < 20 ? 'bg-rose-500 shadow-[0_0_15px_rgba(244,63,94,0.6)]' : 'bg-[#D0B063]'}\`} 
                      style={{ 
                        '--base-height': \`\${h}%\`, 
                        height: \`\${h}%\`,
                        animationDelay: \`\${i * 0.12}s\` 
                      } as any}
                    ></div>
                  ))}`;

  text = text.substring(0, startIdx) + animatedBars + text.substring(endIdx);
  fs.writeFileSync(file, text, 'utf8');
  console.log("Success!");
} else {
  console.log("Could not find boundaries.");
}
