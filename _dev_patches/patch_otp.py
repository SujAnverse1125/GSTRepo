import re

file_path = "D:\\\\SIH2026\\\\frontend\\\\app\\\\login\\\\page.tsx"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Change the OTP input from type="text" to type="password"
content = content.replace('type="text" \n                maxLength={6}\n                value={otp}', 'type="password" \n                maxLength={6}\n                value={otp}')

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("OTP masked successfully.")
