const fs = require('fs');
const path = require('path');

const filePath = path.join('D:', 'SIH2026', 'frontend', 'app', 'dashboard', 'page.tsx');
let content = fs.readFileSync(filePath, 'utf8');

// 1. Fix the translation strings
const newTranslations = `  const translations = {
    en: {
      title: "Command Center",
      subtitle: "Your MSME Digital Twin is live.",
      ccc_title: "Cash Conversion Cycle",
      ccc_desc: "Days to convert inventory to cash"
    },
    hi: {
      title: "कमांड सेंटर",
      subtitle: "आपका MSME डिजिटल ट्विन लाइव है।",
      ccc_title: "नकद रूपांतरण चक्र (CCC)",
      ccc_desc: "इन्वेंट्री को नकदी में बदलने के दिन"
    },
    or: {
      title: "କମାଣ୍ଡ ସେଣ୍ଟର",
      subtitle: "ଆପଣଙ୍କର MSME ଡିଜିଟାଲ୍ ଟ୍ୱିନ୍ ଲାଇଭ୍ ଅଛି।",
      ccc_title: "ନଗଦ ରୂପାନ୍ତର ଚକ୍ର (CCC)",
      ccc_desc: "ସାମଗ୍ରୀକୁ ନଗଦରେ ପରିଣତ କରିବାର ଦିନ"
    }
  };`;

content = content.replace(/const translations = \{[\s\S]*?\}\n\s*\};\s/g, newTranslations + '\n\n');

// 2. Replace the Header explicitly
const oldHeaderRegex = /<h1 className="text-4xl font-black font-serif mb-2">Command Center<\/h1>\s*<p className="text-\[#1A1C20\]\/60 font-medium text-lg">Your MSME Digital Twin is live\.<\/p>/g;
const newHeader = `<h1 className="text-4xl font-black font-serif mb-2">{t.title}</h1>
                <p className="text-[#1A1C20]/60 font-medium text-lg">{t.subtitle}</p>`;
content = content.replace(oldHeaderRegex, newHeader);

// 3. Add Language Dropdown next to WhatsApp button
const oldWhatsApp = /<button onClick=\{\(\) => alert\("WhatsApp Morning Briefs activated.*?\<\/button>/g;
const newWhatsApp = `<select 
                    value={lang} 
                    onChange={(e) => setLang(e.target.value as any)}
                    className="bg-white border border-[#1A1C20]/10 text-[#1A1C20] px-3 py-2 rounded-xl font-bold text-sm outline-none cursor-pointer hover:border-[#D0B063] transition-colors"
                  >
                    <option value="en">English</option>
                    <option value="hi">हिंदी (Hindi)</option>
                    <option value="or">ଓଡ଼ିଆ (Odia)</option>
                  </select>
                  <button onClick={() => alert("✅ Morning Brief sent to +91 98*** **432 on WhatsApp!")} className="px-5 py-2.5 bg-emerald-50 border border-emerald-200 text-emerald-700 rounded-xl shadow-sm font-bold text-sm hover:bg-emerald-100 transition-colors hidden md:flex items-center gap-2">
                    <span>💬 WhatsApp Briefs: ON</span>
                  </button>`;
content = content.replace(oldWhatsApp, newWhatsApp);

fs.writeFileSync(filePath, content, 'utf8');
console.log("Node patch applied successfully.");
