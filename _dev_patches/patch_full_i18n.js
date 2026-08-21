const fs = require('fs');
const path = require('path');

const filePath = path.join('D:', 'SIH2026', 'frontend', 'app', 'dashboard', 'page.tsx');
let content = fs.readFileSync(filePath, 'utf8');

const newTranslations = `  const translations = {
    en: {
      title: "Command Center", subtitle: "Your MSME Digital Twin is live.",
      ccc_title: "Cash Conversion Cycle", ccc_desc: "Days to convert inventory to cash",
      current_balance: "Current Balance", shortfall_risk: "Shortfall Risk",
      buyer_delay: "Avg Buyer Delay", predictive_model: "Predictive Model",
      forecast: "90-Day Liquidity Forecast", action_matrix: "AI ACTION MATRIX",
      comparator: "Resolution Comparator", concentration_risk: "Concentration Risk Engine",
      seasonal_pattern: "Seasonal Pattern Detector", aa_data: "Account Aggregator Data",
      export_csv: "Export CSV", upload_csv: "Upload Corrected Sheet",
      simulator: "Digital Twin Simulator", revoke: "Revoke Consent",
      whatsapp: "WhatsApp Briefs: ON"
    },
    hi: {
      title: "कमांड सेंटर", subtitle: "आपका MSME डिजिटल ट्विन लाइव है।",
      ccc_title: "नकद रूपांतरण चक्र (CCC)", ccc_desc: "इन्वेंट्री को नकदी में बदलने के दिन",
      current_balance: "वर्तमान शेष राशि", shortfall_risk: "कमी का जोखिम",
      buyer_delay: "औसत खरीदार देरी", predictive_model: "पूर्वानुमान मॉडल",
      forecast: "90-दिन तरलता पूर्वानुमान", action_matrix: "AI कार्रवाई मैट्रिक्स",
      comparator: "समाधान तुलनित्र", concentration_risk: "एकाग्रता जोखिम इंजन",
      seasonal_pattern: "मौसमी पैटर्न डिटेक्टर", aa_data: "खाता एग्रीगेटर डेटा",
      export_csv: "CSV निर्यात करें", upload_csv: "सुधारी गई शीट अपलोड करें",
      simulator: "डिजिटल ट्विन सिम्युलेटर", revoke: "सहमति रद्द करें",
      whatsapp: "व्हाट्सएप ब्रीफ: चालू"
    },
    or: {
      title: "କମାଣ୍ଡ ସେଣ୍ଟର", subtitle: "ଆପଣଙ୍କର MSME ଡିଜିଟାଲ୍ ଟ୍ୱିନ୍ ଲାଇଭ୍ ଅଛି।",
      ccc_title: "ନଗଦ ରୂପାନ୍ତର ଚକ୍ର (CCC)", ccc_desc: "ସାମଗ୍ରୀକୁ ନଗଦରେ ପରିଣତ କରିବାର ଦିନ",
      current_balance: "ବର୍ତ୍ତମାନର ବାଲାନ୍ସ", shortfall_risk: "ଅଭାବ ବିପଦ",
      buyer_delay: "ହାରାହାରି କ୍ରେତା ବିଳମ୍ବ", predictive_model: "ପୂର୍ବାନୁମାନ ମଡେଲ୍",
      forecast: "90-ଦିନ ତରଳତା ପୂର୍ବାନୁମାନ", action_matrix: "AI କାର୍ଯ୍ୟ ମ୍ୟାଟ୍ରିକ୍ସ",
      comparator: "ସମାଧାନ ତୁଳନାକାରୀ", concentration_risk: "ଏକାଗ୍ରତା ବିପଦ ଇଞ୍ଜିନ୍",
      seasonal_pattern: "ଋତୁକାଳୀନ ପ୍ୟାଟର୍ଣ୍ଣ ଡିଟେକ୍ଟର୍", aa_data: "ଆକାଉଣ୍ଟ୍ ଆଗ୍ରିଗେଟର୍ ଡାଟା",
      export_csv: "CSV ରପ୍ତାନି କରନ୍ତୁ", upload_csv: "ସଂଶୋଧିତ ସିଟ୍ ଅପଲୋଡ୍ କରନ୍ତୁ",
      simulator: "ଡିଜିଟାଲ୍ ଟ୍ୱିନ୍ ସିମ୍ୟୁଲେଟର୍", revoke: "ସମ୍ମତି ପ୍ରତ୍ୟାହାର କରନ୍ତୁ",
      whatsapp: "ହ୍ଵାଟ୍ସଆପ୍ ବ୍ରିଫ୍: ଅନ୍"
    }
  };`;

content = content.replace(/const translations = \{[\s\S]*?\}\n\s*\};\s/g, newTranslations + '\n\n');

content = content.replace(/>Current Balance</g, '>{t.current_balance}<');
content = content.replace(/>Shortfall Risk</g, '>{t.shortfall_risk}<');
content = content.replace(/>Avg Buyer Delay</g, '>{t.buyer_delay}<');
content = content.replace(/>PREDICTIVE MODEL</g, ' className="uppercase">{t.predictive_model}<');
content = content.replace(/>90-Day Liquidity Forecast</g, '>{t.forecast}<');
content = content.replace(/>AI ACTION MATRIX</g, ' className="uppercase">{t.action_matrix}<');
content = content.replace(/>Resolution Comparator</g, '>{t.comparator}<');
content = content.replace(/>Concentration Risk Engine</g, '>{t.concentration_risk}<');
content = content.replace(/>Seasonal Pattern Detector</g, '>{t.seasonal_pattern}<');
content = content.replace(/>Account Aggregator Data</g, '>{t.aa_data}<');
content = content.replace(/📥 Export CSV</g, '📥 {t.export_csv}<');
content = content.replace(/📤 Upload Corrected Sheet</g, '📤 {t.upload_csv}<');
content = content.replace(/>Digital Twin Simulator</g, '>{t.simulator}<');
content = content.replace(/>Revoke Consent</g, '>{t.revoke}<');
content = content.replace(/>💬 WhatsApp Briefs: ON</g, '>💬 {t.whatsapp}<');

fs.writeFileSync(filePath, content, 'utf8');
console.log("Full Multilingual expansion completed.");
