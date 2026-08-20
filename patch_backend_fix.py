import re
from pathlib import Path

file_path = Path("D:\\SIH2026\\backend\\main.py")
content = file_path.read_text(encoding="utf-8")

old_code = """    # Generate the base simulation
    base_data = _generate_digital_twin_forecast(days=90)"""

new_code = """    # Generate the base simulation
    base_data = await simulate_cashflow()"""

content = content.replace(old_code, new_code)

file_path.write_text(content, encoding="utf-8")
print("Backend fixed.")
