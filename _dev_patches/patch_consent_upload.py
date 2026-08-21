import re
from pathlib import Path

file_path = Path("D:\\SIH2026\\frontend\\app\\dashboard\\page.tsx")
content = file_path.read_text(encoding="utf-8")

# 1. Update the handleFileUpload function to transition from Consent -> Processing -> Dashboard
old_handler = """  const handleFileUpload = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;

    // Simulate loading state during upload
    const confirmed = window.confirm(`Upload and parse ${file.name}? The Twin Engine will recalculate your entire forecast.`);
    if (confirmed) {
      setLoading(true); // Re-use the loading screen
      
      const formData = new FormData();
      formData.append("file", file);

      try {
        const res = await fetch("http://localhost:8000/api/upload", {
          method: "POST",
          body: formData,
        });
        const data = await res.json();
        
        // Update dashboard with the new "better" data
        setBaseChartData(data.projectedCashflow);
        setChartData(data.projectedCashflow);
        setMetrics({
          current_balance: data.summary.cashOnHand,
          gst_due: data.summary.gstDue,
          lowest_projected_balance: data.summary.minProjectedBalance,
          buyer_delay_days: 45
        });
        
        alert("Success: CSV data parsed. Twin recalibrated! Notice the chart has shifted upwards.");
      } catch (err) {
        console.error(err);
        alert("Upload failed. Make sure backend is running.");
      } finally {
        setLoading(false);
      }
    }
  };"""

new_handler = """  const handleFileUpload = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;

    const confirmed = window.confirm(`Upload and parse ${file.name}?`);
    if (confirmed) {
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
      formData.append("file", file);

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
        
        if (appState === 'consent') {
          setTimeout(() => {
            setAppState('dashboard');
            setShowTour(true);
          }, 1500);
        } else {
          alert("Success: CSV data parsed. Twin recalibrated! Notice the chart has shifted upwards.");
          setLoading(false);
        }
      } catch (err) {
        console.error(err);
        alert("Upload failed. Make sure backend is running.");
        setLoading(false);
        if (appState === 'processing') setAppState('consent');
      }
    }
  };"""
content = content.replace(old_handler, new_handler)


# 2. Add the Upload button to the Consent UI
old_consent_btn = """            <button onClick={startIngestion} className="w-full py-5 bg-[#1A1C20] text-white rounded-xl font-bold text-lg hover:bg-[#2D3139] transition-all shadow-xl hover:-translate-y-1">
              Approve & Generate Twin
            </button>
          </div>
        </div>
      )}"""

new_consent_btn = """            <button onClick={startIngestion} className="w-full py-5 bg-[#1A1C20] text-white rounded-xl font-bold text-lg hover:bg-[#2D3139] transition-all shadow-xl hover:-translate-y-1 mb-6">
              Approve & Generate Twin
            </button>

            <div className="relative flex py-2 items-center mb-6">
                <div className="flex-grow border-t border-[#1A1C20]/10"></div>
                <span className="flex-shrink-0 mx-4 text-[#1A1C20]/40 font-bold text-sm uppercase tracking-wider">or bypass aggregator</span>
                <div className="flex-grow border-t border-[#1A1C20]/10"></div>
            </div>

            <button onClick={() => fileInputRef.current?.click()} className="w-full py-4 bg-white border-2 border-[#1A1C20]/10 text-[#1A1C20] rounded-xl font-bold text-lg hover:border-[#D0B063] transition-all flex items-center justify-center gap-3">
              <Database className="w-5 h-5 text-[#D0B063]" /> Upload Tally Export (CSV)
            </button>
          </div>
        </div>
      )}"""
content = content.replace(old_consent_btn, new_consent_btn)

# Make sure we don't accidentally duplicate the file input. 
# We'll just leave the one in the dashboard, but since it's an invisible ref, we can just move it to the top level of the return so it's always available.
if '<input type="file" ref={fileInputRef}' not in content:
    # Actually it's already rendered under the dashboard. Let's move it to just above {appState === 'consent'}
    old_root = """  return (
    <div className="min-h-screen bg-[#F2EFE9] text-[#1A1C20] font-sans selection:bg-[#D0B063]/30 p-4 md:p-8">
      
      {appState === 'consent' && ("""
      
    new_root = """  return (
    <div className="min-h-screen bg-[#F2EFE9] text-[#1A1C20] font-sans selection:bg-[#D0B063]/30 p-4 md:p-8">
      <input type="file" ref={fileInputRef} style={{ display: 'none' }} accept=".csv, .xlsx" onChange={handleFileUpload} />
      
      {appState === 'consent' && ("""
    content = content.replace(old_root, new_root)
    
    # Remove the duplicate one from the data table button
    dup_input = """<input \n                    type="file" \n                    ref={fileInputRef} \n                    style={{ display: 'none' }} \n                    accept=".csv, .xlsx" \n                    onChange={handleFileUpload} \n                  />\n                  <button"""
    content = content.replace(dup_input, "<button")
    
    dup_input2 = """<input 
                    type="file" 
                    ref={fileInputRef} 
                    style={{ display: 'none' }} 
                    accept=".csv, .xlsx" 
                    onChange={handleFileUpload} 
                  />
                  <button"""
    content = content.replace(dup_input2, "<button")

file_path.write_text(content, encoding="utf-8")
print("Consent UI updated with Offline option.")
