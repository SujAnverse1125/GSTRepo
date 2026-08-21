const fs = require('fs');
const path = require('path');

const filePath = path.join('D:', 'SIH2026', 'frontend', 'app', 'page.tsx');
let content = fs.readFileSync(filePath, 'utf8');

// Use simple resilient replace
content = content.replace(/import \{.*\} , CheckCircle2, FileWarning \} from "lucide-react";/g, 'import { ArrowRight, BarChart3, Clock, Landmark, ShieldCheck, Zap, Check, X, Circle, Activity, CheckCircle2, FileWarning } from "lucide-react";');
// Or if it didn't match the wildcard exactly due to multiline
content = content.replace('} , CheckCircle2, FileWarning } from "lucide-react";', ', CheckCircle2, FileWarning } from "lucide-react";');


fs.writeFileSync(filePath, content, 'utf8');
console.log("Imports fixed via Node.js");
