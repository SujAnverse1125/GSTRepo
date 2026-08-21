const fs = require('fs');
const file = 'D:\\SIH2026\\frontend\\app\\page.tsx';
let text = fs.readFileSync(file, 'utf8');

// Regex to catch the div with the corrupted trophy emoji
text = text.replace(/<div className="inline-flex[^>]*>[^<]*Built for SIH 2026[^<]*<\/div>/g, '');

// Also remove the footer line just in case
text = text.replace(/<p className="mt-8 text-sm text-white\/40">Powered by SIH 2026 Innovation Team\.<\/p>/g, '');

fs.writeFileSync(file, text, 'utf8');
console.log("SIH references removed");
