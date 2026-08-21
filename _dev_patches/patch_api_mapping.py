import re

file_path = "D:\\\\SIH2026\\\\frontend\\\\app\\\\dashboard\\\\page.tsx"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Fix the API fetching
old_fetch = """    // Fetch actual data from python backend
    try {
      const res = await fetch("http://localhost:8000/api/simulate");
      const data = await res.json();
      setChartData(data.data);
      setMetrics(data.metrics);
    } catch (e) {
      console.error("Backend offline. Make sure uvicorn is running on port 8000.");
    }"""

new_fetch = """    // Fetch actual data from python backend
    try {
      const res = await fetch("http://localhost:8000/api/simulate");
      const data = await res.json();
      setChartData(data.projectedCashflow);
      setMetrics({
        current_balance: data.summary.cashOnHand,
        gst_due: data.summary.gstDue,
        lowest_projected_balance: data.summary.minProjectedBalance,
        buyer_delay_days: 45 // Hardcoded simulation value
      });
    } catch (e) {
      console.error("Backend offline. Make sure uvicorn is running on port 8000.");
    }"""

content = content.replace(old_fetch, new_fetch)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Fixed API mapping for dashboard.")
