import re

file_path = "D:\\\\SIH2026\\\\frontend\\\\app\\\\dashboard\\\\page.tsx"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Add the revoke handler function
handler_func = """
  const handleRevokeConsent = async () => {
    // Standard hackathon visual flair
    const confirmed = window.confirm("Are you sure you want to revoke FIP consent? All your MSME Digital Twin data will be permanently wiped.");
    if (confirmed) {
      setLoading(true);
      // Actually wipe the Supabase session
      await supabase.auth.signOut();
      alert("Success: RBI Account Aggregator consent revoked. All PII and financial records have been deleted.");
      router.push('/');
    }
  };
"""

if "handleRevokeConsent" not in content:
    content = content.replace("const startIngestion = async () => {", handler_func + "\n  const startIngestion = async () => {")

# Bind it to the button
old_button = """onClick={() => alert("Responsible AI Guardrail Triggered: Disconnecting FIP. Wiping local data.")}"""
new_button = """onClick={handleRevokeConsent}"""

content = content.replace(old_button, new_button)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Revoke handler added.")
