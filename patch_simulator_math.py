import re
from pathlib import Path

file_path = Path("D:\\SIH2026\\frontend\\app\\dashboard\\page.tsx")
content = file_path.read_text(encoding="utf-8")

old_calc = """  // Dynamic Deficit Calculation
  const delayPenalty = simulatedDelay > 20 ? (simulatedDelay - 20) * 1500 : 0;
  const revenuePenalty = revenueShock * 5000;
  const costPenalty = costShock * 3000;
  const totalDeficit = delayPenalty + revenuePenalty + costPenalty;
  const isSafe = totalDeficit === 0;"""

new_calc = """  // Dynamic Deficit Calculation
  const delayPenalty = simulatedDelay > 20 ? (simulatedDelay - 20) * 1500 : 0;
  const revenuePenalty = revenueShock * 5000;
  const costPenalty = costShock * 3000;
  const grossShock = delayPenalty + revenuePenalty + costPenalty;
  
  // The magic: we subtract their actual AI-projected cash buffer from the shock. 
  // If the CSV they uploaded gave them a massive cash buffer, it absorbs the shock!
  const cashBuffer = metrics?.lowest_projected_balance || 0;
  const totalDeficit = Math.max(0, grossShock - Math.max(0, cashBuffer));
  const isSafe = totalDeficit === 0;"""

content = content.replace(old_calc, new_calc)
file_path.write_text(content, encoding="utf-8")
print("Simulator math fixed to respect CSV data.")
