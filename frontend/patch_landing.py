import re

file_path = "D:\\\\SIH2026\\\\frontend\\\\app\\\\page.tsx"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# The new sections to insert before the CTA section
new_sections = """
      {/* How it Works (Under the Hood) */}
      <section className="py-32 px-6 bg-white border-y border-[#1A1C20]/10">
        <div className="max-w-6xl mx-auto">
          <div className="text-center mb-20">
            <h2 className="text-4xl md:text-5xl font-black text-[#1A1C20] mb-6 font-serif">
              Under the <span className="text-[#D0B063]">Hood.</span>
            </h2>
            <p className="text-xl text-[#1A1C20]/70 max-w-2xl mx-auto">
              A transparent look at how data flows securely from your bank to our AI engine.
            </p>
          </div>

          <div className="relative flex flex-col md:flex-row justify-between items-center gap-12 md:gap-4">
            {/* Connecting Line */}
            <div className="hidden md:block absolute top-1/2 left-0 w-full h-1 bg-gradient-to-r from-transparent via-[#D0B063]/30 to-transparent -translate-y-1/2 z-0"></div>

            {/* Step 1 */}
            <div className="relative z-10 flex flex-col items-center text-center max-w-xs">
              <div className="w-20 h-20 rounded-2xl bg-[#F2EFE9] border-2 border-[#D0B063] flex items-center justify-center mb-6 shadow-xl shadow-[#D0B063]/10">
                <ShieldCheck className="w-10 h-10 text-[#1A1C20]" />
              </div>
              <h3 className="text-2xl font-bold text-[#1A1C20] mb-3">1. Secure Consent</h3>
              <p className="text-[#1A1C20]/60">You grant read-only access via the RBI Account Aggregator framework. No passwords shared.</p>
            </div>

            {/* Step 2 */}
            <div className="relative z-10 flex flex-col items-center text-center max-w-xs">
              <div className="w-20 h-20 rounded-2xl bg-[#1A1C20] border-2 border-[#1A1C20] flex items-center justify-center mb-6 shadow-xl">
                <Activity className="w-10 h-10 text-[#D0B063]" />
              </div>
              <h3 className="text-2xl font-bold text-[#1A1C20] mb-3">2. AI Ingestion</h3>
              <p className="text-[#1A1C20]/60">Our Python engine parses 6 months of historical transactions and GST invoices to find patterns.</p>
            </div>

            {/* Step 3 */}
            <div className="relative z-10 flex flex-col items-center text-center max-w-xs">
              <div className="w-20 h-20 rounded-2xl bg-[#D0B063] border-2 border-[#D0B063] flex items-center justify-center mb-6 shadow-xl shadow-[#D0B063]/30">
                <BarChart3 className="w-10 h-10 text-[#1A1C20]" />
              </div>
              <h3 className="text-2xl font-bold text-[#1A1C20] mb-3">3. Actionable Twin</h3>
              <p className="text-[#1A1C20]/60">A 90-day predictive timeline is generated, highlighting exactly when you will face a cash crunch.</p>
            </div>
          </div>
        </div>
      </section>

      {/* Security & Trust Block */}
      <section className="py-24 px-6 bg-[#1A1C20] text-white overflow-hidden relative">
        <div className="absolute top-0 right-0 w-96 h-96 bg-[#D0B063]/10 rounded-full blur-[100px] pointer-events-none"></div>
        <div className="max-w-5xl mx-auto flex flex-col md:flex-row items-center gap-16">
          <div className="flex-1 space-y-8">
            <h2 className="text-4xl md:text-5xl font-black font-serif leading-tight">
              Bank-Grade Security. <br />
              <span className="text-[#D0B063]">Zero Data Retention.</span>
            </h2>
            <div className="space-y-6">
              <div className="flex items-start gap-4">
                <div className="w-10 h-10 rounded-full bg-emerald-500/10 flex items-center justify-center shrink-0">
                  <Check className="w-5 h-5 text-emerald-400" />
                </div>
                <div>
                  <h4 className="text-xl font-bold mb-1">RBI Compliant</h4>
                  <p className="text-white/60">Built strictly on the Sahamati Account Aggregator guidelines.</p>
                </div>
              </div>
              <div className="flex items-start gap-4">
                <div className="w-10 h-10 rounded-full bg-emerald-500/10 flex items-center justify-center shrink-0">
                  <Check className="w-5 h-5 text-emerald-400" />
                </div>
                <div>
                  <h4 className="text-xl font-bold mb-1">AES-256 Encryption</h4>
                  <p className="text-white/60">Your financial data is encrypted in transit and at rest.</p>
                </div>
              </div>
              <div className="flex items-start gap-4">
                <div className="w-10 h-10 rounded-full bg-emerald-500/10 flex items-center justify-center shrink-0">
                  <Check className="w-5 h-5 text-emerald-400" />
                </div>
                <div>
                  <h4 className="text-xl font-bold mb-1">We Predict, Then We Delete</h4>
                  <p className="text-white/60">You can revoke consent at any time. When you do, your data is wiped instantly.</p>
                </div>
              </div>
            </div>
          </div>
          <div className="flex-1 w-full relative">
            <div className="aspect-square max-w-sm mx-auto rounded-full border border-white/10 flex items-center justify-center relative">
               <div className="absolute inset-0 rounded-full border border-dashed border-white/20 animate-spin-slow"></div>
               <ShieldCheck className="w-32 h-32 text-[#D0B063]" />
            </div>
          </div>
        </div>
      </section>

      {/* FAQs */}
      <section className="py-32 px-6 bg-[#FCFDFD]">
        <div className="max-w-4xl mx-auto">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-black text-[#1A1C20] mb-4 font-serif">Common Questions</h2>
            <p className="text-xl text-[#1A1C20]/60">Everything you need to know about MSME Twin.</p>
          </div>
          <div className="space-y-6">
            {[
              {
                q: "Does this replace my accountant or CA?",
                a: "No. MSME Twin works alongside your CA. While your CA looks at the past to file taxes, MSME Twin looks at the future to ensure you have the cash to pay those taxes."
              },
              {
                q: "What if I have multiple bank accounts?",
                a: "Our Account Aggregator integration can sync with multiple FIPs (Financial Information Providers) simultaneously, merging all your cash flows into one holistic twin."
              },
              {
                q: "Do I have to upload invoices manually?",
                a: "Never. By connecting to the GSTN portal, we automatically pull your B2B invoices and match them against your bank inflows."
              }
            ].map((faq, i) => (
              <div key={i} className="p-8 rounded-2xl bg-white border border-[#1A1C20]/10 shadow-sm hover:shadow-md transition-shadow">
                <h3 className="text-2xl font-bold text-[#1A1C20] mb-3">{faq.q}</h3>
                <p className="text-lg text-[#1A1C20]/70 leading-relaxed">{faq.a}</p>
              </div>
            ))}
          </div>
        </div>
      </section>
"""

# Inject before the CTA section
cta_marker = "{/* CTA Section */}"
content = content.replace(cta_marker, new_sections + "\n      " + cta_marker)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Landing page expanded successfully.")
