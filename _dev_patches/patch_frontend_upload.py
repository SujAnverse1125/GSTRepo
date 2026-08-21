import re
from pathlib import Path

file_path = Path("D:\\SIH2026\\frontend\\app\\dashboard\\page.tsx")
content = file_path.read_text(encoding="utf-8")

# 1. Add useRef to the imports
if "useRef" not in content:
    content = content.replace("import { useState, useEffect } from 'react';", "import { useState, useEffect, useRef } from 'react';")

# 2. Add the ref and handler inside the component
handler_logic = """
  const fileInputRef = useRef<HTMLInputElement>(null);

  const handleFileUpload = async (e: React.ChangeEvent<HTMLInputElement>) => {
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
  };
"""
if "const fileInputRef" not in content:
    content = content.replace("const router = useRouter();", "const router = useRouter();\n" + handler_logic)

# 3. Update the "Upload Corrected Sheet" button to trigger the hidden input
old_button = """                  <button onClick={() => alert("Opening file picker... Once uploaded, the Twin Engine will recalculate.")} className="px-4 py-2 text-sm font-bold bg-[#1A1C20] text-white rounded-lg hover:bg-[#2D3139] transition-colors shadow-sm">
                    📤 Upload Corrected Sheet
                  </button>"""

new_button = """                  <input 
                    type="file" 
                    ref={fileInputRef} 
                    style={{ display: 'none' }} 
                    accept=".csv, .xlsx" 
                    onChange={handleFileUpload} 
                  />
                  <button onClick={() => fileInputRef.current?.click()} className="px-4 py-2 text-sm font-bold bg-[#1A1C20] text-white rounded-lg hover:bg-[#2D3139] transition-colors shadow-sm">
                    📤 Upload Corrected Sheet
                  </button>"""
content = content.replace(old_button, new_button)

file_path.write_text(content, encoding="utf-8")
print("Frontend patched for file upload.")
