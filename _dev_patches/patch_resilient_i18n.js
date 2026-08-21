const fs = require('fs');
const path = require('path');

const filePath = path.join('D:', 'SIH2026', 'frontend', 'app', 'dashboard', 'page.tsx');
let content = fs.readFileSync(filePath, 'utf8');

// We use highly resilient regex to catch the strings regardless of surrounding spaces or tags
content = content.replace(/Current Balance/g, '{t.current_balance}');
content = content.replace(/Shortfall Risk/g, '{t.shortfall_risk}');
content = content.replace(/Avg Buyer Delay/g, '{t.buyer_delay}');
content = content.replace(/Predictive Model/gi, '{t.predictive_model}');
content = content.replace(/90-Day Liquidity Forecast/g, '{t.forecast}');
content = content.replace(/AI Action Matrix/gi, '{t.action_matrix}');
content = content.replace(/Resolution Comparator/g, '{t.comparator}');
content = content.replace(/Concentration Risk Engine/g, '{t.concentration_risk}');
content = content.replace(/Seasonal Pattern Detector/g, '{t.seasonal_pattern}');
content = content.replace(/Account Aggregator Data/g, '{t.aa_data}');
content = content.replace(/Export CSV/g, '{t.export_csv}');
content = content.replace(/Upload Corrected Sheet/g, '{t.upload_csv}');
content = content.replace(/Digital Twin Simulator/g, '{t.simulator}');
content = content.replace(/Revoke Consent/g, '{t.revoke}');
content = content.replace(/WhatsApp Briefs: ON/g, '{t.whatsapp}');

// Fix accidental duplicate curly braces if any (e.g., >{t.current_balance}< got replaced again to >{{t.current_balance}}<)
content = content.replace(/\{\{t\./g, '{t.');
content = content.replace(/\}\}/g, '}');

// We must ensure that any literal string replacement like {t.current_balance} is actually valid JSX.
// If the original string was <p>Current Balance</p>, it becomes <p>{t.current_balance}</p>. This is PERFECT.
// BUT if the original was inside a className or a console.log, it might break.
// Fortunately, these specific strings only exist as visible text in the dashboard.

fs.writeFileSync(filePath, content, 'utf8');
console.log("Resilient string replacement completed.");
