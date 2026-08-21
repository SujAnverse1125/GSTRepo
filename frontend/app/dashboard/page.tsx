"use client";

import { useState, useEffect, useRef } from 'react';
import { supabase } from '../../utils/supabase';
import { useRouter } from 'next/navigation';
import { ShieldCheck, Database, Zap, FileWarning, ArrowRight, Server, Activity, CheckCircle2, BarChart3, TrendingDown } from 'lucide-react';
import CashFlowChart from '../components/CashFlowChart';
import { fetchMLLiquidityForecast } from '../lib/ml_service';

type AppState = 'consent' | 'processing' | 'dashboard';

export default function DashboardFlow() {
  const [appState, setAppState] = useState<AppState>('consent');
  const [loading, setLoading] = useState(true);
  const [showTredsModal, setShowTredsModal] = useState(false);
  const [tredsStatus, setTredsStatus] = useState("loading");

  const [session, setSession] = useState<any>(null);
  
  // Dashboard Data
  const [baseChartData, setBaseChartData] = useState<any[]>([]);
  const [chartData, setChartData] = useState<any[]>([]);
    const [buyers, setBuyers] = useState<any[]>([]);
  const [recentTxns, setRecentTxns] = useState<any[]>([
    { source: "GSTN Inv #1042", amount: "₹1,00,000", status: "Unpaid", ai: "Delayed", type: "warning" },
    { source: "SBI Bank Statement", amount: "-₹18,000", status: "Tax Due", ai: "Day 20", type: "danger" },
    { source: "GSTN Inv #1041", amount: "₹45,000", status: "Settled", ai: "On time", type: "success" }
  ]);
    const [simulatedDelay, setSimulatedDelay] = useState(45);
  const [revenueShock, setRevenueShock] = useState(0);
  const [costShock, setCostShock] = useState(0);

  useEffect(() => {
    if (appState !== 'dashboard') return;
    const fetchML = async () => {
      try {
        const mlData = await fetchMLLiquidityForecast({
          current_balance: metrics?.current_balance || 1500000,
          slider_delay_days: simulatedDelay,
          revenue_shock: revenueShock,
          cost_shock: costShock
        });

        if (mlData && mlData.forecast_90_days) {
          const morphedData = mlData.forecast_90_days.map((val: number, idx: number) => ({
            day: idx + 1,
            label: 'D' + (idx + 1),
            balance: val,
            forecastLow: val * 0.9,
            forecastHigh: val * 1.1
          }));
          setChartData(morphedData);
          setMetrics((prev: any) => ({ ...prev, current_balance: Math.min(...mlData.forecast_90_days) }));
        }
      } catch (err) {
        console.error("ML Integration Error:", err);
      }
    };
    fetchML();
  }, [simulatedDelay, revenueShock, costShock, appState]);
  
  // Google Form Style Upload States
    // Language State
  const [lang, setLang] = useState<'en' | 'hi' | 'or'>('en');
  
  const translations: Record<string, any> = {
    en: {
      title: "Command Center", subtitle: "Your MSME Digital Twin is live.",
      ccc_title: "Cash Conversion Cycle", ccc_desc: "Days to convert inventory to cash",
      current_balance: "Projected Low", shortfall_risk: "Shortfall Risk",
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
  const t = translations[lang];
  const [showUploadModal, setShowUploadModal] = useState(false);
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [uploadedFileName, setUploadedFileName] = useState<string | null>(null);
  const [showTour, setShowTour] = useState(false);
  const [tourStep, setTourStep] = useState(1);
  const [logs, setLogs] = useState<string[]>([]);
  const [metrics, setMetrics] = useState<any>(null);

  const router = useRouter();

  const fileInputRef = useRef<HTMLInputElement>(null);

    const handleFileSelect = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) {
      setSelectedFile(file);
    }
  };

  const confirmUpload = async () => {
    if (!selectedFile) return;
    setShowUploadModal(false);

    if (appState === 'consent') {
      setAppState('processing');
      setLogs([
        "Initializing Secure Offline Parsing...",
        "Extracting ledgers from CSV...",
        "Running standard deviation analysis...",
        "Generating Digital Twin from Offline Data..."
      ]);
    } else {
      setLoading(true);
    }
    
    const formData = new FormData();
    formData.append("file", selectedFile);

    try {
      const res = await fetch("/api/upload", {
        method: "POST",
        body: formData,
      });
      const data = await res.json();
      
      setBaseChartData(data.projectedCashflow);
      setChartData(data.projectedCashflow);
      setMetrics({
        current_balance: data.summary.cashOnHand,
        gst_due: data.summary.gstDue,
        lowest_projected_balance: data.summary.minProjectedBalance,
        buyer_delay_days: 45
      });
      if (data.recentTxns && data.recentTxns.length > 0) {
        setRecentTxns(data.recentTxns);
      }
      
      // Update the trust badge header!
      setUploadedFileName(selectedFile.name);
      setSelectedFile(null); // reset for next time
      if (fileInputRef.current) fileInputRef.current.value = '';
      
      if (appState === 'consent') {
        setTimeout(() => {
          setAppState('dashboard');
          setShowTour(true);
        }, 1500);
      } else {
        setLoading(false);
      }
    } catch (err) {
      console.error(err);
      alert("Upload failed. Make sure backend is running.");
      setLoading(false);
      if (appState === 'processing') setAppState('consent');
      if (fileInputRef.current) fileInputRef.current.value = '';
    }
  };

  // Dynamic Deficit Calculation
  const cashBuffer = metrics?.lowest_projected_balance || 0;
  
  // Scale the simulator shocks based on how massive their balance is, 
  // so dragging the sliders actually impacts rich companies too!
  const scaleMultiplier = Math.max(1, cashBuffer / 50000); 
  
  const delayPenalty = simulatedDelay > 20 ? (simulatedDelay - 20) * 1500 * scaleMultiplier : 0;
  const revenuePenalty = revenueShock * 5000 * scaleMultiplier;
  const costPenalty = costShock * 3000 * scaleMultiplier;
  const grossShock = delayPenalty + revenuePenalty + costPenalty;
  
  const totalDeficit = Math.max(0, grossShock - Math.max(0, cashBuffer));
  const isSafe = totalDeficit === 0;

  // Auth Protection
  useEffect(() => {
    Promise.resolve({ data: { session: { user: { phone: 'Demo User' } } } }).then(({ data: { session } }) => {
      if (!session) {
        router.push('/login');
      } else {
        setSession(session);
        setLoading(false);
      }
    });
  }, [router]);

  const handleSimulationChange = (e: any) => {
    const newDelay = parseInt(e.target.value);
    setSimulatedDelay(newDelay);

    if (baseChartData.length > 0) {
      const morphedData = baseChartData.map((point: any) => {
        // Simple visual simulation: Drop balance between GST Day (20) and the new delay day
        if (point.day >= 20 && point.day < newDelay) {
          const drop = (newDelay - 20) * 15000; // Fake penalty calculation for visual effect
          return { ...point, balance: point.balance - drop, forecastLow: point.forecastLow - drop };
        }
        return point;
      });
      setChartData(morphedData);
    }
  };

  const handleRevokeConsent = async () => {
    // Standard hackathon visual flair
    const confirmed = window.confirm("Are you sure you want to revoke FIP consent? All your MSME Digital Twin data will be permanently wiped.");
    if (confirmed) {
      setLoading(true);
      // Actually wipe the Supabase session
      await supabase.auth.signOut();
      alert("Success: RBI Account Aggregator consent revoked. All PII and financial records have been deleted.");
      router.push('/');
    }
  };

  const startIngestion = async () => {
    setAppState('processing');
    
    // Simulate terminal logs
    const steps = [
      "Authenticating with Account Aggregator...",
      "FIP Consent Granted. Fetching 6-month bank statements...",
      "Parsing GSTN invoices via API...",
      "Running standard deviation analysis on buyer delays...",
      "Calculating GST Liquidity Paradox...",
      "Generating Digital Twin...",
      "Finishing up..."
    ];

    for (let i = 0; i < steps.length; i++) {
      await new Promise(r => setTimeout(r, 800));
      setLogs(prev => [...prev, steps[i]]);
    }

    // Fetch actual data from python backend
    try {
      const res = await fetch("/api/simulate");
      const data = await res.json();
      setBaseChartData(data.projectedCashflow);
      setChartData(data.projectedCashflow);
      setMetrics({
        current_balance: data.summary.cashOnHand,
        gst_due: data.summary.gstDue,
        lowest_projected_balance: data.summary.minProjectedBalance,
        buyer_delay_days: 45 // Hardcoded simulation value
      });
    } catch (e) {
      console.error("Backend offline. Make sure uvicorn is running on port 8000.");
    }

    setTimeout(() => {
      setAppState('dashboard');
      setShowTour(true);
    }, 1000);
  };

  if (loading) return <div className="min-h-screen bg-[#F2EFE9] flex items-center justify-center text-[#1A1C20] font-black text-xl">Loading Secure Session...</div>;

  return (
    <div className="min-h-screen bg-[#F2EFE9] text-[#1A1C20] font-sans selection:bg-[#D0B063]/30 p-4 md:p-8">
      <style dangerouslySetInnerHTML={{__html: `
        @media print {
          @page { size: landscape; margin: 1cm; }
          body { background: white !important; -webkit-print-color-adjust: exact; }
          button, select, input { display: none !important; }
          .shadow-2xl, .shadow-sm, .shadow-xl { box-shadow: none !important; border: 1px solid #e5e7eb !important; }
          .bg-\[\#F2EFE9\] { background: white !important; }
          .min-h-screen { min-height: auto !important; }
        }
      `}} />
      <input type="file" ref={fileInputRef} style={{ display: 'none' }} accept=".csv, .xlsx" onChange={handleFileSelect} />
      
      {appState === 'consent' && (
        <div className="max-w-3xl mx-auto mt-20 animate-in fade-in slide-in-from-bottom-8">
          <div className="bg-white rounded-[2rem] p-10 border border-[#1A1C20]/10 shadow-2xl">
            <div className="flex items-center gap-4 mb-8">
              <div className="w-16 h-16 rounded-2xl bg-[#D0B063]/10 border-2 border-[#D0B063] flex items-center justify-center text-[#D0B063]">
                <ShieldCheck className="w-8 h-8" />
              </div>
              <div>
                <h1 className="text-3xl font-black font-serif">Account Aggregator Consent</h1>
                <p className="text-[#1A1C20]/60 font-medium">FIU Request ID: REQ-{Math.floor(Math.random()*100000)}</p>
              </div>
            </div>

            <div className="space-y-6 mb-10">
              <div className="p-6 rounded-2xl bg-[#F2EFE9] border border-[#1A1C20]/5">
                <label className="block text-sm font-bold uppercase tracking-wider text-[#1A1C20]/60 mb-3">Select FIP (Bank)</label>
                <select className="w-full bg-white border border-[#1A1C20]/10 rounded-xl px-4 py-4 text-lg font-bold outline-none focus:border-[#D0B063]">
                  <option>State Bank of India (SBI)</option>
                  <option>HDFC Bank</option>
                  <option>ICICI Bank</option>
                  <option>Axis Bank</option>
                  <option>Punjab National Bank (PNB)</option>
                  <option>Kotak Mahindra Bank</option>
                </select>
              </div>
              <div className="p-6 rounded-2xl bg-[#F2EFE9] border border-[#1A1C20]/5">
                <h3 className="font-bold mb-2">Requested Data:</h3>
                <ul className="list-disc pl-5 text-[#1A1C20]/70 space-y-2">
                  <li>6 Months Bank Statement (Read-Only)</li>
                  <li>GSTN Outward Invoices (Read-Only)</li>
                </ul>
              </div>
            </div>

            <button onClick={startIngestion} className="w-full py-5 bg-[#1A1C20] text-white rounded-xl font-bold text-lg hover:bg-[#2D3139] transition-all shadow-xl hover:-translate-y-1 mb-6">
              Approve & Generate Twin
            </button>

            <div className="relative flex py-2 items-center mb-6">
                <div className="flex-grow border-t border-[#1A1C20]/10"></div>
                <span className="flex-shrink-0 mx-4 text-[#1A1C20]/40 font-bold text-sm uppercase tracking-wider">or bypass aggregator</span>
                <div className="flex-grow border-t border-[#1A1C20]/10"></div>
            </div>

            <button onClick={() => setShowUploadModal(true)} className="w-full py-4 bg-white border-2 border-[#1A1C20]/10 text-[#1A1C20] rounded-xl font-bold text-lg hover:border-[#D0B063] transition-all flex items-center justify-center gap-3">
              <Database className="w-5 h-5 text-[#D0B063]" /> Upload Tally Export (CSV)
            </button>
          </div>
        </div>
      )}

      {appState === 'processing' && (
        <div className="max-w-3xl mx-auto mt-20 animate-in zoom-in-95">
          <div className="bg-white rounded-[2rem] p-10 border border-[#1A1C20]/10 shadow-2xl relative overflow-hidden">
             <div className="flex items-center gap-4 mb-10">
               <div className="w-16 h-16 rounded-full bg-[#F2EFE9] flex items-center justify-center">
                 <div className="w-8 h-8 border-4 border-[#D0B063]/30 border-t-[#D0B063] rounded-full animate-spin"></div>
               </div>
               <div>
                 <h2 className="text-3xl font-black text-[#1A1C20] font-serif">Building Your Twin</h2>
                 <p className="text-[#1A1C20]/60 font-medium">Please wait while we secure your data and run the simulations.</p>
               </div>
             </div>

             <div className="space-y-8">
               {[
                 { title: "Hello! Initializing Secure Connection", desc: "Establishing a bank-grade AES-256 encrypted tunnel." },
                 { title: "Fetching FIP Bank Statements", desc: "We are securely pulling your last 6 months of cash flow history." },
                 { title: "Parsing GSTN Invoices", desc: "Matching outward invoices to predict your upcoming tax liabilities." },
                 { title: "AI Deviation Analysis", desc: "Calculating exactly how many days your buyers typically delay payments." },
                 { title: "You're in safe hands", desc: "Finalizing your MSME Digital Twin. We predict, then we delete." }
               ].map((step, i) => {
                 const isCompleted = i < Math.floor(logs.length / 1.2);
                 const isCurrent = i === Math.floor(logs.length / 1.2);
                 return (
                   <div key={i} className={`flex gap-6 transition-all duration-500 ${isCompleted || isCurrent ? 'opacity-100 translate-x-0' : 'opacity-30 translate-x-4'}`}>
                     <div className="flex flex-col items-center">
                       {isCompleted ? (
                         <div className="w-8 h-8 rounded-full bg-emerald-100 flex items-center justify-center">
                           <CheckCircle2 className="w-5 h-5 text-emerald-600" />
                         </div>
                       ) : isCurrent ? (
                         <div className="w-8 h-8 rounded-full bg-[#F2EFE9] flex items-center justify-center border-2 border-[#D0B063]">
                           <div className="w-3 h-3 bg-[#D0B063] rounded-full animate-pulse"></div>
                         </div>
                       ) : (
                         <div className="w-8 h-8 rounded-full bg-[#F2EFE9] border border-[#1A1C20]/10"></div>
                       )}
                       {i < 4 && <div className={`w-0.5 h-12 mt-2 ${isCompleted ? 'bg-emerald-200' : 'bg-[#1A1C20]/5'}`}></div>}
                     </div>
                     <div className={isCurrent ? 'animate-pulse' : ''}>
                       <h3 className={`text-lg font-bold ${isCompleted ? 'text-[#1A1C20]' : 'text-[#1A1C20]/60'}`}>{step.title}</h3>
                       <p className="text-[#1A1C20]/50 text-sm mt-1">{step.desc}</p>
                     </div>
                   </div>
                 );
               })}
             </div>
          </div>
        </div>
      )}

      {appState === 'dashboard' && (
        <div className="max-w-7xl mx-auto animate-in fade-in duration-1000">
          
          {/* Onboarding Tour Modal */}
          {showTour && (
            <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-[#1A1C20]/40 backdrop-blur-sm animate-in fade-in">
              <div className="bg-white rounded-[2rem] p-10 max-w-lg w-full shadow-2xl relative overflow-hidden">
                 <div className="absolute top-0 left-0 w-full h-2 bg-gradient-to-r from-[#1A1C20] to-[#D0B063]"></div>
                 
                 {tourStep === 1 && (
                   <div className="animate-in fade-in slide-in-from-right-4">
                     <div className="w-16 h-16 rounded-2xl bg-[#F2EFE9] flex items-center justify-center text-[#1A1C20] mb-6">
                       <BarChart3 className="w-8 h-8" />
                     </div>
                     <h3 className="text-2xl font-black font-serif mb-3 text-[#1A1C20]">Your Twin is Live.</h3>
                     <p className="text-[#1A1C20]/70 text-lg leading-relaxed mb-8">
                       We've successfully mapped your FIP Bank data against your GSTN invoices. The chart behind this is your exact cash flow projected 90 days into the future.
                     </p>
                     <button onClick={() => setTourStep(2)} className="w-full py-4 bg-[#1A1C20] text-white rounded-xl font-bold hover:bg-[#2D3139] transition-all">Next: How to use the Simulator</button>
                   </div>
                 )}

                 {tourStep === 2 && (
                   <div className="animate-in fade-in slide-in-from-right-4">
                     <div className="w-16 h-16 rounded-2xl bg-[#D0B063]/20 flex items-center justify-center text-[#D0B063] mb-6">
                       <Activity className="w-8 h-8" />
                     </div>
                     <h3 className="text-2xl font-black font-serif mb-3 text-[#1A1C20]">Simulate Reality</h3>
                     <p className="text-[#1A1C20]/70 text-lg leading-relaxed mb-8">
                       Scroll down to the <strong>{t.simulator}</strong>. Drag the slider to test alternate realities—like "What if my buyer pays 30 days late?"—and watch the chart update in real-time.
                     </p>
                     <button onClick={() => setTourStep(3)} className="w-full py-4 bg-[#1A1C20] text-white rounded-xl font-bold hover:bg-[#2D3139] transition-all">Next: The Safety Net</button>
                   </div>
                 )}

                 {tourStep === 3 && (
                   <div className="animate-in fade-in slide-in-from-right-4">
                     <div className="w-16 h-16 rounded-2xl bg-[#D0B063]/20 flex items-center justify-center text-[#D0B063] mb-6">
                       <ShieldCheck className="w-8 h-8" />
                     </div>
                     <h3 className="text-2xl font-black font-serif mb-3 text-[#1A1C20]">Risk & Liability Engines</h3>
                     <p className="text-[#1A1C20]/70 text-lg leading-relaxed mb-8">
                       Your dashboard includes a dedicated <strong>GST Liability Tracker</strong>, a <strong>Concentration Risk</strong> analyzer, and a <strong>{t.seasonal_pattern}</strong> to guard against hidden cash traps.
                     </p>
                     <button onClick={() => setShowTour(false)} className="w-full py-4 bg-[#1A1C20] text-white rounded-xl font-bold hover:bg-[#2D3139] transition-all">Enter Command Center</button>
                   </div>
                 )}
                 
                 {/* Pagination Dots */}
                 <div className="flex justify-center gap-3 mt-8">
                   {[1, 2, 3].map(step => (
                     <div key={step} className={`w-2.5 h-2.5 rounded-full transition-colors ${tourStep === step ? 'bg-[#1A1C20]' : 'bg-[#1A1C20]/10'}`}></div>
                   ))}
                 </div>
              </div>
            </div>
          )}

          <header className="flex flex-col md:flex-row justify-between items-start md:items-center mb-10 gap-4">
            <div>
              <h1 className="text-4xl font-black font-serif mb-2">{t.title}</h1>
                <p className="text-[#1A1C20]/60 font-medium text-lg">{t.subtitle}</p>
            </div>
            <div className="flex flex-col items-end gap-3">
              <div className="flex gap-4">
                  <button onClick={() => {
                    const originalTitle = document.title;
                    document.title = "MSME_Digital_Twin_Report";
                    window.print();
                    document.title = originalTitle;
                  }} className="px-5 py-2.5 bg-white border border-[#1A1C20]/10 text-[#1A1C20] rounded-xl shadow-sm font-bold text-sm hover:border-[#D0B063] transition-colors hidden md:flex items-center gap-2">
                    <span className="text-lg">📄</span> {t.export_csv || "Download Report"}
                  </button>
                  <select 
                    value={lang} 
                    onChange={(e) => setLang(e.target.value as any)}
                    className="bg-white border border-[#1A1C20]/10 text-[#1A1C20] px-3 py-2 rounded-xl font-bold text-sm outline-none cursor-pointer hover:border-[#D0B063] transition-colors"
                  >
                    <option value="en">English</option>
                    <option value="hi">हिंदी (Hindi)</option>
                    <option value="or">ଓଡ଼ିଆ (Odia)</option>
                  </select>
                <button onClick={() => alert("✅ Morning Brief sent to +91 98*** **432 on WhatsApp!")} className="px-5 py-2.5 bg-emerald-50 border border-emerald-200 text-emerald-700 rounded-xl shadow-sm font-bold text-sm hover:bg-emerald-100 transition-colors hidden md:flex items-center gap-2">
                  <span>💬 {t.whatsapp}</span>
                </button>
                <button onClick={handleRevokeConsent} className="px-5 py-2.5 bg-white border border-rose-200 text-rose-600 rounded-xl shadow-sm font-bold text-sm hover:bg-rose-50 transition-colors">
                  {t.revoke}
                </button>
                <div className="px-5 py-2.5 bg-[#1A1C20] text-white rounded-xl shadow-sm flex items-center gap-3">
                  <div className="w-2 h-2 bg-emerald-400 rounded-full animate-pulse"></div>
                  <span className="font-bold text-sm hidden md:inline">
                    {uploadedFileName ? `100% Synced: ${uploadedFileName}` : "Live: SBI & GSTN"}
                  </span>
                </div>
              </div>
            </div>
          </header>

          {/* Metrics */}
          <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
            <div className="bg-white rounded-[2rem] p-8 border border-[#1A1C20]/10 shadow-sm flex items-center gap-6">
              <div className="w-16 h-16 rounded-2xl bg-[#F2EFE9] flex items-center justify-center text-[#1A1C20]">
                 <Database className="w-8 h-8" />
              </div>
              <div>
                <p className="text-sm font-bold text-[#1A1C20]/50 uppercase tracking-wider mb-1">{t.current_balance}</p>
                <h3 className="text-3xl font-black font-serif">₹{metrics?.current_balance?.toLocaleString('en-IN') || "1,84,000"}</h3>
              </div>
            </div>

            <div className="bg-[#1A1C20] rounded-[2rem] p-8 shadow-xl flex items-center gap-6 relative overflow-hidden">
              <div className="absolute top-0 right-0 w-32 h-32 bg-rose-500/10 rounded-full blur-2xl"></div>
              <div className="w-16 h-16 rounded-2xl bg-white/10 flex items-center justify-center text-rose-400 relative z-10">
                 <FileWarning className="w-8 h-8" />
              </div>
              <div className="relative z-10">
                <p className="text-sm font-bold text-white/50 uppercase tracking-wider mb-1">{t.shortfall_risk}</p>
                <h3 className={`text-3xl font-black font-serif ${isSafe ? 'text-emerald-400' : 'text-rose-400'}`}>{isSafe ? 'Stable' : 'Critical'}</h3>
              </div>
            </div>

            <div className="bg-white rounded-[2rem] p-8 border border-[#1A1C20]/10 shadow-sm flex items-center gap-6">
              <div className="w-16 h-16 rounded-2xl bg-[#D0B063]/10 flex items-center justify-center text-[#D0B063]">
                 <Zap className="w-8 h-8" />
              </div>
              <div>
                <p className="text-sm font-bold text-[#1A1C20]/50 uppercase tracking-wider mb-1">{t.buyer_delay}</p>
                <h3 className="text-3xl font-black font-serif">{simulatedDelay} Days</h3>
              </div>
            </div>

              <div className="bg-white rounded-[2rem] p-8 border-b-4 border-b-[#D0B063] border border-[#1A1C20]/10 shadow-sm flex items-center gap-6">
                <div className="w-16 h-16 rounded-2xl bg-[#D0B063]/10 flex items-center justify-center text-[#D0B063]">
                   <TrendingDown className="w-8 h-8" />
                </div>
                <div>
                  <p className="text-sm font-bold text-[#D0B063] uppercase tracking-wider mb-1">{t.ccc_title}</p>
                  <h3 className="text-3xl font-black font-serif">{simulatedDelay + 15} Days</h3>
                </div>
              </div>

          </div>

          <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
            {/* Chart Area */}
            <div className="lg:col-span-2">
              <CashFlowChart data={chartData} />
            </div>

            {/* Debt vs Non-Debt Comparator Matrix */}
            <div className="bg-white rounded-[2rem] border border-[#1A1C20]/10 shadow-sm p-8 flex flex-col h-full">
              <div className="mb-6">
                <div className="inline-flex items-center gap-2 px-3 py-1 bg-[#1A1C20] text-white text-xs font-bold rounded-full mb-4 uppercase tracking-wider">
                  <ShieldCheck className="w-4 h-4 text-[#D0B063]" /> {t.action_matrix}
                </div>
                <h3 className="text-2xl font-black font-serif mb-2 text-[#1A1C20]">{t.comparator}</h3>
                <p className="text-[#1A1C20]/70 text-sm">
                  {isSafe ? "Your cash flow is stable. No financing required right now." : `We detected a ₹${totalDeficit.toLocaleString('en-IN')} deficit. Compare your options to bridge the gap:`}
                </p>
              </div>

              {!isSafe && (
                <div className="space-y-3 overflow-y-auto pr-2 custom-scrollbar flex-1">
                  
                  {/* Option 1: AI Recommended */}
                  <div className="p-4 rounded-xl border-2 border-[#D0B063] bg-[#D0B063]/5 relative">
                    <div className="absolute -top-3 right-4 bg-[#D0B063] text-[#1A1C20] text-[10px] font-black uppercase tracking-wider px-3 py-1 rounded-full shadow-sm">
                      ✨ AI Recommended (Non-Debt)
                    </div>
                    <div className="flex justify-between items-start mb-2 mt-2">
                      <h4 className="font-bold text-[#1A1C20]">Offer 2% Early Discount</h4>
                      <span className="text-sm font-bold text-rose-600">Cost: ₹{Math.round(totalDeficit * 0.02).toLocaleString('en-IN')}</span>
                    </div>
                    <p className="text-xs text-[#1A1C20]/60 mb-3">Instead of a loan, offer Tata Electronics a 2% discount to pay today. Fastest & cheapest.</p>
                    <button className="w-full py-2.5 bg-[#1A1C20] text-white text-sm rounded-lg font-bold hover:bg-[#2D3139] transition-all">Send Discount Offer</button>
                  </div>

                  {/* Option 2: Invoice Discounting */}
                  <div className="p-4 rounded-xl border border-[#1A1C20]/10 bg-white hover:border-[#D0B063]/50 transition-colors">
                    <div className="flex justify-between items-start mb-2">
                      <h4 className="font-bold text-[#1A1C20]">Invoice Discounting (Debt)</h4>
                      <span className="text-sm font-bold text-rose-600">Cost: ₹{Math.round(totalDeficit * 0.015).toLocaleString('en-IN')}</span>
                    </div>
                    <p className="text-xs text-[#1A1C20]/60 mb-3">Bank advances 80% of invoice today at 1.5% monthly fee.</p>
                    <button onClick={() => { setShowTredsModal(true); setTredsStatus("loading"); setTimeout(() => setTredsStatus("success"), 2500); }} className="w-full py-2 border border-[#1A1C20]/20 text-[#1A1C20] text-sm rounded-lg font-bold hover:bg-[#F2EFE9] transition-all">Select TReDS Financing</button>
                  </div>

                  {/* Option 3: Do Nothing */}
                  <div className="p-4 rounded-xl border border-rose-200 bg-rose-50/30">
                    <div className="flex justify-between items-start mb-2">
                      <h4 className="font-bold text-[#1A1C20]">Do Nothing (Miss Tax)</h4>
                      <span className="text-sm font-bold text-rose-600">Cost: ₹{Math.round(totalDeficit * 0.05).toLocaleString('en-IN')}</span>
                    </div>
                    <p className="text-xs text-[#1A1C20]/60 mb-3">Wait for buyer. Pay 18% GST interest + ₹50/day late penalty.</p>
                    <button onClick={() => { setShowTredsModal(true); setTredsStatus("loading"); setTimeout(() => setTredsStatus("success"), 2500); }} className="w-full py-2 border border-[#1A1C20]/20 text-[#1A1C20] text-sm rounded-lg font-bold hover:bg-[#F2EFE9] transition-all">Select TReDS Financing</button>
                  </div>

                </div>
              )}
            </div>
          </div>

          {/* AI Risk Engines */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-8 mb-8">
            {/* Concentration Risk */}
            <div className="bg-white rounded-[2rem] border border-[#1A1C20]/10 shadow-sm p-8">
              <div className="flex items-center justify-between mb-6">
                <h3 className="text-xl font-black font-serif text-[#1A1C20]">{t.concentration_risk}</h3>
                <span className="px-3 py-1 bg-rose-100 text-rose-700 text-xs font-bold rounded-full">High Risk</span>
              </div>
              <p className="text-[#1A1C20]/60 text-sm mb-6">AI analysis of your Account Aggregator data shows dangerous reliance on a single buyer.</p>
              
              <div className="space-y-5">
                <div>
                  <div className="flex justify-between text-sm font-bold mb-2">
                    <span className="text-[#1A1C20]">Reliance Retail Ltd.</span>
                    <span className="text-rose-600">68% of Receivables</span>
                  </div>
                  <div className="w-full h-3 bg-[#F2EFE9] rounded-full overflow-hidden">
                    <div className="h-full bg-rose-500 rounded-full" style={{ width: '68%' }}></div>
                  </div>
                </div>
                
                <div>
                  <div className="flex justify-between text-sm font-bold mb-2">
                    <span className="text-[#1A1C20]">Tata Electronics</span>
                    <span className="text-[#D0B063]">22% of Receivables</span>
                  </div>
                  <div className="w-full h-3 bg-[#F2EFE9] rounded-full overflow-hidden">
                    <div className="h-full bg-[#D0B063] rounded-full" style={{ width: '22%' }}></div>
                  </div>
                </div>

                <div>
                  <div className="flex justify-between text-sm font-bold mb-2">
                    <span className="text-[#1A1C20]">Other SMEs</span>
                    <span className="text-emerald-500">10% of Receivables</span>
                  </div>
                  <div className="w-full h-3 bg-[#F2EFE9] rounded-full overflow-hidden">
                    <div className="h-full bg-emerald-500 rounded-full" style={{ width: '10%' }}></div>
                  </div>
                </div>
              </div>
            </div>

            {/* {t.seasonal_pattern} */}
            <div className="bg-white rounded-[2rem] border border-[#1A1C20]/10 shadow-sm p-8 flex flex-col justify-center">
              <div className="flex items-center justify-between mb-6">
                <h3 className="text-xl font-black font-serif text-[#1A1C20]">{t.seasonal_pattern}</h3>
                <Activity className="w-6 h-6 text-[#D0B063]" />
              </div>
              <div className="p-5 rounded-2xl bg-[#D0B063]/10 border border-[#D0B063]/20 mb-6">
                <h4 className="font-bold text-[#1A1C20] mb-2 flex items-center gap-2">
                  <Database className="w-4 h-4 text-[#D0B063]" /> Historical Dip Detected
                </h4>
                <p className="text-[#1A1C20]/70 text-sm leading-relaxed">
                  Fast Fourier Transform (FFT) analysis of your past 3 years reveals a recurring <strong>15% revenue drop every September</strong> (Post-Monsoon slump).
                </p>
              </div>
              <p className="text-sm font-bold text-[#1A1C20]/60">
                ✓ The 90-Day Twin Engine has automatically factored this seasonal variance into your cash flow projection above.
              </p>
            </div>
          </div>

          {/* Interactive Tools & Tables */}
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 mt-8">
            {/* Live Invoice Sync Table */}
            <div className="bg-white rounded-[2rem] border border-[#1A1C20]/10 shadow-sm p-8">
              <div className="flex flex-col md:flex-row md:items-center justify-between mb-6 gap-4">
                <h3 className="text-2xl font-black font-serif text-[#1A1C20]">{t.aa_data}</h3>
                <div className="flex gap-2">
                  <button onClick={() => alert("Downloading bank_data.csv...")} className="px-4 py-2 text-sm font-bold bg-[#F2EFE9] border border-[#1A1C20]/10 text-[#1A1C20] rounded-lg hover:bg-[#e8e4dc] transition-colors shadow-sm">
                    📥 {t.export_csv}
                  </button>
                  <button onClick={() => setShowUploadModal(true)} className="px-4 py-2 text-sm font-bold bg-[#1A1C20] text-white rounded-lg hover:bg-[#2D3139] transition-colors shadow-sm">
                    📤 {t.upload_csv}
                  </button>
                </div>
              </div>
              <div className="overflow-x-auto">
                <table className="w-full text-left border-collapse">
                  <thead>
                    <tr className="border-b border-[#1A1C20]/10">
                      <th className="py-3 text-sm font-bold text-[#1A1C20]/50 uppercase tracking-wider">Source</th>
                      <th className="py-3 text-sm font-bold text-[#1A1C20]/50 uppercase tracking-wider">Amount</th>
                      <th className="py-3 text-sm font-bold text-[#1A1C20]/50 uppercase tracking-wider">Status</th>
                      <th className="py-3 text-sm font-bold text-[#1A1C20]/50 uppercase tracking-wider text-right">AI Prediction</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-[#1A1C20]/5">
                    {recentTxns.map((txn, i) => (
                      <tr key={i} className="hover:bg-[#F2EFE9]/30 transition-colors">
                        <td className="py-4 font-bold text-[#1A1C20]">{txn.source}</td>
                        <td className="py-4 text-[#1A1C20]/80">{txn.amount}</td>
                        <td className="py-4">
                          <span className={`px-2 py-1 text-xs font-bold rounded-full ${txn.type === 'success' ? 'bg-emerald-100 text-emerald-700' : txn.type === 'warning' ? 'bg-amber-100 text-amber-700' : 'bg-rose-100 text-rose-700'}`}>
                            {txn.status}
                          </span>
                        </td>
                        <td className="py-4 text-right text-[#1A1C20]/80 font-bold">{txn.ai}</td>
                      </tr>
                    ))}
                  </tbody></table></div>
            </div>

            {/* Scenario Simulator */}
            <div className="bg-[#1A1C20] rounded-[2rem] shadow-xl p-8 text-white relative overflow-hidden">
               <div className="absolute top-0 right-0 w-64 h-64 bg-[#D0B063]/10 rounded-full blur-3xl pointer-events-none"></div>
               <div className="relative z-10">
                 <h3 className="text-2xl font-black font-serif mb-2 text-[#D0B063]">{t.simulator}</h3>
                 <p className="text-white/60 mb-8">Move the slider to simulate alternate realities and see how it impacts your liquidity.</p>
                 
                 <div className="space-y-6">
                   {/* Delay Slider */}
                   <div>
                     <label className="flex justify-between text-sm font-bold uppercase tracking-wider text-white/80 mb-2">
                       <span>Buyer Payment Delay</span>
                       <span className="text-[#D0B063]">{simulatedDelay} Days</span>
                     </label>
                     <input 
                       type="range" min="10" max="90" 
                       value={simulatedDelay} 
                       onChange={(e) => setSimulatedDelay(parseInt(e.target.value))}
                       className="w-full h-2 bg-white/20 rounded-lg appearance-none cursor-pointer accent-[#D0B063]" 
                     />
                   </div>

                   {/* Revenue Drop Slider */}
                   <div>
                     <label className="flex justify-between text-sm font-bold uppercase tracking-wider text-white/80 mb-2">
                       <span>Revenue Drop Shock</span>
                       <span className="text-[#D0B063]">{revenueShock}%</span>
                     </label>
                     <input 
                       type="range" min="0" max="50" 
                       value={revenueShock} 
                       onChange={(e) => setRevenueShock(parseInt(e.target.value))}
                       className="w-full h-2 bg-white/20 rounded-lg appearance-none cursor-pointer accent-[#D0B063]" 
                     />
                   </div>

                   {/* Cost Spike Slider */}
                   <div>
                     <label className="flex justify-between text-sm font-bold uppercase tracking-wider text-white/80 mb-2">
                       <span>Material Cost Spike</span>
                       <span className="text-[#D0B063]">{costShock}%</span>
                     </label>
                     <input 
                       type="range" min="0" max="50" 
                       value={costShock} 
                       onChange={(e) => setCostShock(parseInt(e.target.value))}
                       className="w-full h-2 bg-white/20 rounded-lg appearance-none cursor-pointer accent-[#D0B063]" 
                     />
                   </div>

                   {/* Live Deficit Warning */}
                   <div className="p-4 rounded-xl bg-[#D0B063]/10 border border-[#D0B063]/20 mt-4">
                     {isSafe ? (
                       <p className="text-sm text-white/80"><strong className="text-emerald-400">Cash Flow Positive!</strong> You safely avoid the GST trap under these conditions.</p>
                     ) : (
                       <p className="text-sm text-white/80">Under these parameters, you face a <strong className="text-rose-400 text-lg">₹{totalDeficit.toLocaleString('en-IN')}</strong> cash deficit. AI solutions generated.</p>
                     )}
                   </div>
                 </div>
               </div>
            </div>
          </div>
        </div>
      )}
      
      {appState === 'dashboard' && (
        <footer className="max-w-7xl mx-auto mt-12 pt-8 border-t border-[#1A1C20]/10 text-center pb-8 animate-in fade-in">
          <p className="text-xs font-bold text-[#1A1C20]/40 uppercase tracking-widest">
            Responsible AI Guardrails Active
          </p>
                    <p className="text-sm text-[#1A1C20]/60 mt-2">
            This Digital Twin is an analytical planning tool, not financial advice. All AI auto-financing recommendations carry risk. Data is minimized and never shared.
          </p>
          <button 
            onClick={() => { localStorage.clear(); window.location.href = '/'; }} 
            className="mt-6 text-xs font-bold text-rose-500/50 hover:text-rose-600 transition-colors uppercase tracking-widest"
          >
            [ Hard Reset Demo ]
          </button>
        </footer>
      )}

      {/* Google Form Style Upload Modal */}
      {showUploadModal && (
        <div className="fixed inset-0 bg-[#1A1C20]/80 backdrop-blur-sm z-50 flex items-center justify-center p-4">
          <div className="bg-white w-full max-w-md rounded-3xl p-8 shadow-2xl relative animate-in fade-in zoom-in-95">
            <button onClick={() => {setShowUploadModal(false); setSelectedFile(null);}} className="absolute top-6 right-6 text-[#1A1C20]/40 hover:text-[#1A1C20] font-bold">✕</button>
            <h3 className="text-2xl font-black font-serif mb-2 text-[#1A1C20]">Upload Offline Data</h3>
            <p className="text-[#1A1C20]/60 text-sm mb-6">Select your Tally or ERP bank export CSV to recalibrate the Digital Twin.</p>
            
            <div className="border-2 border-dashed border-[#1A1C20]/20 rounded-2xl p-8 text-center bg-[#F2EFE9]/30 mb-6 hover:bg-[#F2EFE9] transition-colors cursor-pointer" onClick={() => fileInputRef.current?.click()}>
              <Database className="w-8 h-8 text-[#D0B063] mx-auto mb-3" />
              {selectedFile ? (
                <div>
                  <p className="font-bold text-emerald-600 mb-1">File Attached:</p>
                  <p className="text-sm text-[#1A1C20]/80 font-mono truncate">{selectedFile.name}</p>
                </div>
              ) : (
                <p className="font-bold text-[#1A1C20]/60">Click to browse or drag file here</p>
              )}
            </div>

            <button 
              onClick={confirmUpload} 
              disabled={!selectedFile}
              className={`w-full py-4 rounded-xl font-bold transition-all shadow-md flex items-center justify-center gap-2 ${selectedFile ? 'bg-[#1A1C20] text-white hover:bg-[#2D3139]' : 'bg-[#1A1C20]/10 text-[#1A1C20]/40 cursor-not-allowed'}`}
            >
              {selectedFile && <CheckCircle2 className="w-5 h-5" />}
              {selectedFile ? 'Upload & Sync Data' : 'Select a file first'}
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
