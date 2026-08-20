const fs = require('fs');
const path = require('path');

const file = path.join('D:', 'SIH2026', 'frontend', 'app', 'page.tsx');
let text = fs.readFileSync(file, 'utf8');

// Fix the corrupted JSX comments
text = text.replace(/\\{\\\/\\\* Comparison Table \\\(Built Section\\\) \\\*\\\/\\}/g, '{/* Comparison Table (Built Section) */}');

// Insert import
if (!text.includes('import LiquidityCalculator')) {
    text = text.replace('import Link from "next/link";', 'import Link from "next/link";\nimport LiquidityCalculator from "./components/LiquidityCalculator";');
}

fs.writeFileSync(file, text, 'utf8');
console.log("Fixed JSX syntax errors.");
