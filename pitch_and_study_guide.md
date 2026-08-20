# MSME Digital Twin: Pitch & Study Guide

This document outlines the core mathematical concepts, the required domain knowledge, and exactly **how** and **where** these concepts fit into the codebase and your hackathon pitch. 

---

## 1. The Core Math (How our Engine Actually Works)

If a judge asks, "How does your simulator predict cash?", explain these 4 formulas coded into the backend:

**A. The Digital Twin Daily Balance Formusxla**
*Calculates cash day-by-day.*
> `Balance (Day N) = Balance (Day N-1) + Weighted Inflows - Scheduled Outflows - Tax Obligations ± Historical Variance`

**B. Buyer Payment Weighting & Standard Deviation**
*We don't trust invoice due dates. We use statistical history.*
*   **Math:** If Invoice is due on Day 30, but the buyer's historical average payment time is 45 days, our engine automatically shifts the expected cash inflow to Day 45.
*   **Confidence Interval (Variance):** We calculate the **Standard Deviation (σ)** of the buyer's past payments. If they pay in 45 days ± 5 days, we show the user a range (e.g., "You will have ₹38,000 - ₹52,000").

**C. Cash Conversion Cycle (CCC)**
*The primary health metric. Every MSME owner understands this.*
> `CCC = Days to sell inventory + Days to collect cash from buyers - Days to pay suppliers`
*   **What it means:** How many days does the business's cash stay "tied up" before it comes back as profit? The lower the number, the better.

**D. Concentration Risk & Worsening Trends**
*   **Concentration Math:** `(Total money owed by Buyer X / Total money owed by everyone) * 100`. If this is > 40%, we trigger a critical alert.
*   **Worsening Trend:** We calculate the **Slope** of their payment delays over the last 6 invoices. If the slope is positive (delays are increasing from 5 days -> 10 days -> 15 days), we trigger an early warning.

---

## 2. What You Should Study (The Concepts)

**A. Domain Knowledge (Crucial for the Pitch)**
*   **The India Stack & Account Aggregator (AA):** Understand what Sahamati is. Know how "consent-based data sharing" works in India. Judges love this.
*   **Accrual vs. Cash Accounting (The GST Problem):** Understand why the GST Liquidity Paradox happens. (Hint: Accrual accounting means tax is owed when the invoice is *generated*, even if cash hasn't touched the bank yet).
*   **Invoice Discounting:** Understand this financing option. It means selling an unpaid invoice to a bank for a small fee (like 1.5%) to get cash immediately instead of waiting 90 days.

**B. The Tech Stack (High-Level)**
*   **Python / FastAPI:** This is our backend engine doing the heavy math.
*   **React & Tailwind CSS:** This is our frontend. Know how to read basic React components so you can tweak text, colors, or chart layouts.

**C. The Machine Learning (For the Judges)**
*   **Facebook Prophet:** We will use this library for Time-Series Forecasting (predicting future cash dips based on seasonal trends, like a dip every February). 
*   **Scikit-Learn (Gradient Boosting):** We will use this to generate the "Buyer Reliability Score" (0 to 100 rating on how trustworthy a buyer is).

---

## 3. Resources to Read / Watch

**For the Domain & Business Logic:**
*   **Account Aggregator:** Read the [Sahamati AA overview](https://sahamati.org.in/what-is-account-aggregator/) (Takes 10 mins).
*   **Cash Conversion Cycle:** Watch a quick 5-minute YouTube video on "Cash Conversion Cycle explained simply."
*   **Invoice Discounting:** Search Investopedia for "Invoice Factoring / Discounting."

**For the Tech & Math:**
*   **Standard Deviation:** A quick refresher on Khan Academy or YouTube on what standard deviation is.
*   **Facebook Prophet:** Read the first page of the [Prophet documentation](https://facebook.github.io/prophet/) to understand it's designed for seasonal time-series forecasting.

---

## 4. Why to Learn This: How & Where it Connects to the Pitch

Here is exactly how these concepts map to the code, and how to talk about them to win over the judges:

### 1. Sahamati / Account Aggregator (AA)
*   **Where it goes in the code:** Stage 1 (Onboarding Data Pull).
*   **How it helps the product:** Eliminates manual data entry. App pulls 6 months of bank data instantly.
*   **How it helps YOU (The Pitch):** If you confidently say, *"We utilize the Sahamati AA framework for zero-friction, consent-based onboarding,"* you instantly prove you understand modern, government-backed digital infrastructure. It separates our app from basic accounting tools.

### 2. The GST Paradox (Accrual Accounting)
*   **Where it goes in the code:** The GST Liability Tracker (Stage 2). The code calculates tax owed on the Invoice Date, not the Payment Date.
*   **How it helps the product:** It is the core trigger for our alerts. It calculates the exact day the business runs out of money because of taxes.
*   **How it helps YOU (The Pitch):** This is your **hook**. Tell the judge: *"An MSME bills ₹1 Lakh today. They owe 18% GST next month. But the client won't pay for 90 days. We built a tracker specifically to predict this exact shortfall."* 

### 3. Invoice Discounting
*   **Where it goes in the code:** The "Explainable Recommendations" Engine (Stage 3).
*   **How it helps the product:** When cash hits zero, it generates options: "Take a Loan" OR "Do Invoice Discounting."
*   **How it helps YOU (The Pitch):** Show the judge: *"Look, instead of recommending a high-interest bank loan, our AI calculated that selling this specific unpaid Reliance invoice to a bank at a 1.2% discount is actually cheaper and faster."* This proves the app is a financial advisor.

### 4. Facebook Prophet (Time-Series ML)
*   **Where it goes in the code:** The Seasonal Pattern Detector.
*   **How it helps the product:** Analyzes historical bank data to notice patterns (e.g., "Always runs out of cash in February").
*   **How it helps YOU (The Pitch):** This proves we are not an AI wrapper. Tell the judges: *"We aren't just sending data to ChatGPT. We are running actual time-series ML models like Prophet to predict seasonal revenue dips."*

### 5. Standard Deviation (Variance)
*   **Where it goes in the code:** The Web Dashboard UI (Stage 4).
*   **How it helps the product:** Draws a shaded "band" showing the likely range of cash flow on the chart.
*   **How it helps YOU (The Pitch):** Point to the chart and say: *"We don't give false point-estimates. We calculate the standard deviation of buyer delays to give the MSME a 95% confidence interval of their future cash."* It sounds mathematically rigorous.
