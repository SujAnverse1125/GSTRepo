const fs = require('fs');
const path = require('path');

const file = path.join('D:', 'SIH2026', 'frontend', 'app', 'page.tsx');
let text = fs.readFileSync(file, 'utf8');

// Match the exact static map function regardless of whitespace
const regex = /\{\[40, 50, 60, 45, 30, 15, 5, 20, 50, 70, 80, 90\]\.map\(\(h, i\) => \(\s*<div key=\{i\} className=\{`flex-1 rounded-t-sm \$\{h < 20 \? 'bg-rose-500' : 'bg-\\[#D0B063\\]'\}`\} style=\{\{ height: `\$\{h\}%` \}\}>\s*<\/div>\s*\)\)\}/g;

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

text = text.replace(regex, animatedBars);

fs.writeFileSync(file, text, 'utf8');
console.log("Chart brought to life properly!");
