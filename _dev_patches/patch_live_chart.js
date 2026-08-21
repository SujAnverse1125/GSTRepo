const fs = require('fs');
const path = require('path');

const file = path.join('D:', 'SIH2026', 'frontend', 'app', 'page.tsx');
let text = fs.readFileSync(file, 'utf8');

// 1. Inject the Style tag right after the opening main div
const styleTag = `
      <style dangerouslySetInnerHTML={{__html: \`
        @keyframes equalize {
          0% { height: var(--base-height); }
          50% { height: calc(var(--base-height) + 10%); }
          100% { height: var(--base-height); }
        }
        .live-bar {
          animation: equalize 2.5s ease-in-out infinite;
        }
      \`}} />
`;
text = text.replace(
  '<div className="min-h-screen bg-gradient-to-b from-[#F2EFE9] to-[#FCFDFD] text-[#1A1C20] font-sans selection:bg-[#D0B063]/30">', 
  '<div className="min-h-screen bg-gradient-to-b from-[#F2EFE9] to-[#FCFDFD] text-[#1A1C20] font-sans selection:bg-[#D0B063]/30">\n' + styleTag
);


// 2. Replace the static bar chart with the animated one
const staticBars = `{[40, 50, 60, 45, 30, 15, 5, 20, 50, 70, 80, 90].map((h, i) => (
                    <div key={i} className={\`flex-1 rounded-t-sm \${h < 20 ? 'bg-rose-500' : 'bg-[#D0B063]'}\`} style={{ height: \`\${h}%\` }}></div>
                  ))}`;

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

text = text.replace(staticBars, animatedBars);

fs.writeFileSync(file, text, 'utf8');
console.log("Chart brought to life!");
