import re

file_path = "D:\\SIH2026\\frontend\\app\\login\\page.tsx"

with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

# Make the OTP button always enabled if phone is not empty
text = text.replace('disabled={phone.length === 0 || loading}', '')
text = text.replace('disabled={otp.length !== 6 || loading}', '')

# Bypass Supabase for the demo
handle_send = """  const handleSendOtp = async () => {
    if (phone.length >= 10) {
      setLoading(true);
      setTimeout(() => {
        setLoading(false);
        setShowOtp(true);
      }, 1000);
    }
  };"""

handle_verify = """  const handleVerifyOtp = async () => {
    if (otp.length > 0) {
      setLoading(true);
      setTimeout(() => {
        setLoading(false);
        setStep('consent');
        setTimeout(() => router.push('/dashboard'), 4000);
      }, 1000);
    }
  };"""

# Replace the original functions
import re
text = re.sub(r'const handleSendOtp = async \(\) => \{.*?\n  \};\n', handle_send + '\n', text, flags=re.DOTALL)
text = re.sub(r'const handleVerifyOtp = async \(\) => \{.*?\n  \};\n', handle_verify + '\n', text, flags=re.DOTALL)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Bypassed Supabase OTP for seamless demo")
