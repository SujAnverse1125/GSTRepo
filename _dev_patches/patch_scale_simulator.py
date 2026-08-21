import re
from pathlib import Path

file_path = Path("D:\\SIH2026\\frontend\\app\\dashboard\\page.tsx")
content = file_path.read_text(encoding="utf-8")

old_calc = """  // Dynamic Deficit Calculation
  const delayPenalty = simulatedDelay > 20 ? (simulatedDelay - 20) * 1500 : 0;
  const revenuePenalty = revenueShock * 5000;
  const costPenalty = costShock * 3000;
  const grossShock = delayPenalty + revenuePenalty + costPenalty;
  
  // The magic: we subtract their actual AI-projected cash buffer from the shock. 
  // If the CSV they uploaded gave them a massive cash buffer, it absorbs the shock!
  const cashBuffer = metrics?.lowest_projected_balance || 0;
  const totalDeficit = Math.max(0, grossShock - Math.max(0, cashBuffer));
  const isSafe = totalDeficit === 0;"""

new_calc = """  // Dynamic Deficit Calculation
  const cashBuffer = metrics?.lowest_projected_balance || 0;
  
  // Scale the simulator shocks based on how massive their balance is, 
  // so dragging the sliders actually impacts rich companies too!
  const scaleMultiplier = Math.max(1, cashBuffer / 50000); 
  
  const delayPenalty = simulatedDelay > 20 ? (simulatedDelay - 20) * 1500 * scaleMultiplier : 0;
  const revenuePenalty = revenueShock * 5000 * scaleMultiplier;
  const costPenalty = costShock * 3000 * scaleMultiplier;
  const grossShock = delayPenalty + revenuePenalty + costPenalty;
  
  const totalDeficit = Math.max(0, grossShock - Math.max(0, cashBuffer));
  const isSafe = totalDeficit === 0;"""

content = content.replace(old_calc, new_calc)

file_path.write_text(content, encoding="utf-8")
print("Dynamic scaling multiplier added to simulator.")
