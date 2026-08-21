import re

file_path = "C:\\\\Users\\\\SUJAN\\\\.gemini\\\\antigravity\\\\brain\\\\fa11bf0d-8e36-4bd6-8e60-bbccb95ed292\\\\features_tracking.md"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

new_content = """
## 5. Interface & Notifications (Stage 4 Complete)
* **Feature:** Data Correction via CSV/Sheet Sync
* **What it does:** Allows the user to click "Export CSV", fix any AI miscategorizations in Excel/Google Sheets, and click "Upload Corrected Sheet" to instantly recalculate the Twin.
* **Pitch Value:** Extremely pragmatic. Proves we understand MSMEs don't want to learn complex UI data-grids and prefer working in spreadsheets.

* **Feature:** WhatsApp Morning Brief Integration
* **What it does:** A toggle in the header that activates daily 8 AM WhatsApp summaries of their cash flow.
* **Pitch Value:** Solves the problem of MSME owners being too busy to log into a dashboard every day.
"""

content = content + new_content

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Docs updated.")
