import re
from pathlib import Path

file_path = Path("D:\\SIH2026\\frontend\\app\\dashboard\\page.tsx")
content = file_path.read_text(encoding="utf-8")

# Extract everything up to "const translations = {"
start_idx = content.find("  const translations = {")
end_idx = content.find("  const t = translations[lang];")

if start_idx != -1 and end_idx != -1:
    new_translations = """  const translations: Record<string, any> = {
    en: {
      title: "Command Center", subtitle: "Your MSME Digital Twin is live.",
      ccc_title: "Cash Conversion Cycle", ccc_desc: "Days to convert inventory to cash",
      current_balance: "Current Balance", shortfall_risk: "Shortfall Risk",
      buyer_delay: "Avg Buyer Delay", predictive_model: "Predictive Model",
      forecast: "90-Day Liquidity Forecast", action_matrix: "AI Action Matrix",
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
  };
"""
    content = content[:start_idx] + new_translations + content[end_idx:]
    file_path.write_text(content, encoding="utf-8")
    print("TypeScript translations object successfully patched.")
else:
    print("Could not find translation object boundaries.")
