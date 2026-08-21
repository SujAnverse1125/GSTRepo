import re
from pathlib import Path

file_path = Path("D:\\SIH2026\\frontend\\app\\dashboard\\page.tsx")
content = file_path.read_text(encoding="utf-8")

# 1. Add new state variables
new_state = """  const [simulatedDelay, setSimulatedDelay] = useState(45);
  const [revenueShock, setRevenueShock] = useState(0);
  const [costShock, setCostShock] = useState(0);
  
  // Google Form Style Upload States
  const [showUploadModal, setShowUploadModal] = useState(false);
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [uploadedFileName, setUploadedFileName] = useState<string | null>(null);"""

content = re.sub(r'const \[simulatedDelay, setSimulatedDelay\] = useState\(45\);\s*const \[revenueShock, setRevenueShock\] = useState\(0\);\s*const \[costShock, setCostShock\] = useState\(0\);', new_state, content, count=1)

# 2. Refactor handleFileUpload to handleFileSelect and confirmUpload
old_handler = re.search(r'const handleFileUpload = async.*?e\.target\.value = \'\';\n\s*\}\n\s*\}\n\s*\};', content, re.DOTALL).group(0)

new_handler = """  const handleFileSelect = (e: React.ChangeEvent<HTMLInputElement>) => {
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
      const res = await fetch("http://localhost:8000/api/upload", {
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
  };"""

content = content.replace(old_handler, new_handler)

# 3. Change file input onChange to handleFileSelect
content = content.replace("onChange={handleFileUpload}", "onChange={handleFileSelect}")

# 4. Change buttons to open the modal instead of clicking the input directly
content = content.replace("onClick={() => fileInputRef.current?.click()}", "onClick={() => setShowUploadModal(true)}")

# 5. Update the Header badge
old_header_badge = """<span className="font-bold text-sm hidden md:inline">Live: SBI & GSTN</span>"""
new_header_badge = """<span className="font-bold text-sm hidden md:inline">
                    {uploadedFileName ? `100% Synced: ${uploadedFileName}` : "Live: SBI & GSTN"}
                  </span>"""
content = content.replace(old_header_badge, new_header_badge)

# 6. Inject the Upload Modal JSX at the very end of the component before the final closing div
modal_jsx = """
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
  );"""

content = re.sub(r'    </div>\n  \);\n}', modal_jsx + '\n}', content)

file_path.write_text(content, encoding="utf-8")
print("Upload Modal and Header Trust Badge injected.")
