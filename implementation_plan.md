# Hackathon Execution Plan: Consent-Based MSME Cash-Flow Digital Twin

> **🤖 AGENT DIRECTIVE (NORTH STAR):** 
> This document is the absolute source of truth and the definitive architectural blueprint for this project. Every single line of code written, every UI component designed, and every backend route created MUST be cross-referenced against this plan. I will not deviate from this flowchart. I will not build a "glorified dashboard." I am building a true Mathematical Simulation Engine.

Based on the provided SOAIDEATHON-S42 Strategy Brief and the approved 9-Step Architectural Flowchart, here is the complete breakdown of the project.

## 1. The Problem Statement
Indian MSMEs have ₹7.34 lakh crore locked in delayed payments. Large buyers delay payments by 90-120 days, but under the Indian GST framework, tax obligations crystallize the moment an invoice is raised. 
**The Core Issue:** MSMEs must pay GST with money they haven't received yet, forcing them into expensive working capital loans.

## 2. The Winning Solution (What We Are Building)
Most teams will build a simple dashboard where users type in invoices manually. We will build a **true Digital Twin**—a live simulation engine with the following critical differentiators:

1.  **Account Aggregator & GSTN Integration:** Zero manual data entry.
2.  **The GST Liquidity Paradox Tracker:** Forecasts exact GST shortfalls.
3.  **Shock Simulator:** Allows users to test "What-if" scenarios.
4.  **Buyer Payment Behaviour Profiling:** Machine learning to predict actual payment dates.
5.  **Concentration Risk Engine:** Existential risk alerts for buyer dependency.
6.  **Explainable Recommendations:** Cost comparisons of Debt vs. Non-Debt options.
7.  **Alert Layer:** WhatsApp/SMS notifications for critical cash stress and bad buyer concentration.
8.  **Responsible AI & Governance:** Consent, revocation, and no protected-characteristic-based decisions.

### 2.1 MVP vs. Demo-Ready Scope
To keep the project credible and buildable within hackathon constraints, we divide the work into two layers:

**MVP (must-have):**
- consent-based onboarding concept + mock AA flow
- GST paradox tracker
- 90-day cash-flow forecast
- buyer concentration and delay risk
- dashboard + chart UI
- shock simulator
- explainable recommendation cards

**Demo-ready (stretch but expected):**
- real WhatsApp/SMS alert trigger
- multilingual text layer (Hindi/Odia)
- stronger dashboard storytelling and polished UI
- consent revocation and governance notes
- cleaner recommendation engine and edge-case logic

The MVP is the minimum viable product. The demo-ready layer is what makes the product feel complete in front of judges.

---

## 3. The 9-Step Architectural Workflow (The Blueprint)

This is the exact pipeline the code must follow, as defined by our flowchart. The order matters; do not build dashboard features before the simulation pipeline is stable.

*   **Step 1: Onboarding & Data Import (Day 0)**
    *   Enter Udyam/GSTIN via public API.
    *   Initiate Account Aggregator (AA) Consent Flow.
    *   Fetch Raw Data (Bank Statements, GST Invoices, UPI Data).
    *   Deliverable: user starts from a consent-based onboarding flow, not a manual form.
*   **Step 2: Data Parsing & Master Ledger State**
    *   Bank Statement Parser (Categorize Operating, Financing, Tax flows).
    *   Invoice Parser (Extract Buyers, Amounts, Due Dates, GST).
    *   Baseline CCC (Cash Conversion Cycle) Calculation.
    *   Generate the Encrypted Master Ledger State.
    *   Deliverable: a clean ledger used by the simulation engine.
*   **Step 3: The Twin Engine - CORE (90-Day Rolling Timeline)**
    *   Daily Liquidity Calculation (Day N-1 + Weighted Inflows - Outflows).
    *   Weighted Buyer Reliability Scores (Historical auto-shift of payment dates).
    *   Confidence Intervals on Forecasts (Standard deviation / range estimates).
    *   Deliverable: the actual 90-day future cash timeline.
*   **Step 4: Risk Analysis & Prediction**
    *   Concentration Risk Radar (Buyer dependence alerts).
    *   Buyer Payment Behaviour Profiler (Delay trends, reliability).
    *   Seasonal Pattern Detection (Recurring annual gaps).
    *   Deliverable: explainable risk layers visible to the user.
*   **Step 5: GST Liability Paradox Tracker**
    *   GST Due-Date Forecaster (Based purely on *raised* invoices).
    *   GST Liability Gap Alert (Fired before inflow is received).
    *   Deliverable: the central business insight that differentiates this product.
*   **Step 6: Shock Simulator**
    *   Sliders for: Buyer Delay / Revenue Drop / Cost Rise.
    *   Re-run Twin Engine with modified parameters.
    *   Compare Shocked vs. Baseline cash flows on the visual chart.
    *   Deliverable: a real scenario analysis flow.
*   **Step 7: Multimodal Decision Engine**
    *   Trigger: Liquidity Gap detected.
    *   Logic: Non-Debt vs. Debt option comparator (side-by-side cost breakdown).
    *   Explainable Recommendations (Wait, Chase Buyer, Invoice Discounting, Loan).
    *   Deliverable: clear next-step financial guidance.
*   **Step 8: Interface & Alert Layer**
    *   Update Web Dashboard (rolling timeline with bands, health tables).
    *   Trigger WhatsApp/SMS Fallback (daily summaries, critical alerts).
    *   Multilingual Translation capability (Hindi, Odia).
    *   Deliverable: judge-ready dashboard with a clear story and alert path.
*   **Step 9: Responsible AI & Guardrails**
    *   Unit & Integration testing.
    *   Consent Revocation Flow (Delete data within 24h).
    *   No protected characteristics used (No automatic lending decisions).
    *   Deliverable: governance compliance and safer product behavior.

### 3.1 Execution Order for the Team
To avoid confusion, the team must follow this real order:

1. Project Lead defines scope and checks north-star alignment.
2. Delivery Coordinator sets task dependencies and milestone order.
3. Backend Engineer builds data contract and simulation API.
4. Math and Logic Checker validates the formulas.
5. Frontend Coder consumes the contract and builds the dashboard.
6. Compliance and Plan Reviewer checks architecture fit.
7. Code Error Detector runs final bug and integration review.
8. Project Lead gives final demo-go decision.

This is the actual collaboration model expected for the project.

---

## 4. What You Need (Tech Stack & Prerequisites)

*   **Backend:** Python (FastAPI), PostgreSQL (or SQLite for speed), Redis, Celery (for background simulations).
*   **Frontend:** React (Next.js/Vite), Tailwind CSS, Recharts.
*   **Integrations to mock/setup:** Sahamati Account Aggregator Sandbox, GSTN Public API, WhatsApp Business API / Twilio.
*   **Analytics/ML:** Time-series forecasting (Prophet), Buyer reliability scoring (Scikit-learn), Standard deviation/variance (NumPy).
*   **Operational Requirements:** a working local dev setup, a utility logger, a tracked task board, and a clear person-to-task ownership list.

### 4.1 Agent Collaboration Structure
The project must not be treated as a single-person app build. The recommended collaboration structure:

- **Project Lead:** defines success, scope, priority, and final go/no-go.
- **Delivery Coordinator:** creates sequence and milestone checkpoints.
- **Backend Engineer:** handles FastAPI, simulation logic, and data services.
- **Frontend Coder:** handles the user experience, dashboard, and scenario interactions.
- **Math and Logic Checker:** validates formulas, variance, and risk logic.
- **Compliance and Plan Reviewer:** checks against the plan and the grand business problem.
- **Code Error Detector:** catches bugs before demo and integration review.

This setup is essential to stay aligned with the plan and avoid heroic but fragile single-agent work.

---

## 5. Detailed Implementation Phases

### Phase 1: Foundation & The "Zero-Entry" Data Layer (Steps 1 & 2)
*   **Backend Initialization:** Set up FastAPI structure and SQLite.
*   **Frontend Initialization:** Create Next.js project with Tailwind CSS.
*   **Mock Data:** Write scripts to generate realistic JSONs for 6-months of AA bank statements and GSTN invoices.
*   **Reference UI Flow:** Onboard with AA -> consent -> ledger -> dashboard.
*   **Deliverable:** A running API serving mock data, and a React app with an "Onboard with AA" flow that parses into the Master Ledger State.

### Phase 2: The Core "Digital Twin" Simulation Engine (Steps 3, 4, 5)
*   **Categorization & Profiling:** Parse bank statements automatically. Calculate Buyer Standard Deviation and assign Reliability Scores.
*   **The GST Paradox Tracker:** Force 18% Cash Outflows on the 20th of next month for unpaid invoices.
*   **The Engine Loop:** Calculate `Tomorrow's Cash = Today's Cash + Expected Receivables - Payables - GST`.
*   **Risk triggers:** concentration > 40%, buyer delay slope increasing, GST shortfall visible before cash inflow arrives.
*   **Deliverable:** An API endpoint (`/api/simulate`) returning a 90-day JSON array of exact future cash balances with confidence bands.

### Phase 3: The Interactive Dashboard & Shock Simulator (Steps 6 & 8)
*   **The Main Visuals:** Draw the 90-day cash flow timeline in Recharts with shaded variance bands.
*   **The Shock Simulator:** Build UI sliders (Buyer Delay, Revenue Drop). Dragging sliders pings the FastAPI backend, re-runs the simulation, and re-draws the chart live.
*   **Dashboard UX:** show KPIs, alerts, concentration, health score, and scenario comparison.
*   **Deliverable:** A highly visual web dashboard where you can play with the future of the business in real-time.

### Phase 4: Intelligence, Alerts & The "Demo Moment" (Steps 7, 8, 9)
*   **Decision Matrix:** When cash goes negative, generate options in a UI card (e.g., "Option A: 30-day loan. Option B: Discount Invoice #102").
*   **WhatsApp / SMS Trigger:** Integrate Twilio or Meta WhatsApp webhook. A severe cash gap triggers an actual text message to the judge's phone.
*   **Multilingual alert layer:** follow up in Hindi or Odia for local relevance.
*   **Guardrails:** consent revocation, no protected characteristics, no automatic lending decisions.
*   **Deliverable:** The complete, hackathon-ready product with live WhatsApp alerts and a clean judge demo narrative.

### Phase 5: Final Demo Readiness & QA
*   **Plan compliance review:** verify every step against the plan.
*   **Bug sweep:** validate frontend/backend integration, API contract, and edge cases.
*   **Demo rehearsal:** ensure story flows naturally in under 3 minutes.
*   **Deliverable:** a final product that feels intelligent, reliable, and demo-proof.

---

## 6. The Core Math (The Engine's Logic)

*   **The Digital Twin Daily Balance Formula:** 
    `Balance (Day N) = Balance (Day N-1) + Weighted Inflows - Scheduled Outflows - Tax Obligations ± Historical Variance`
*   **Buyer Payment Weighting & Standard Deviation:** We don't trust due dates. If buyer history shows average payment at 45 days, the engine shifts the cash inflow to Day 45. Calculate the **Standard Deviation (σ)** for confidence intervals.
*   **Cash Conversion Cycle (CCC):** `Days Inventory Outstanding + Days Sales Outstanding - Days Payable Outstanding`.
*   **Concentration Risk & Worsening Trends:** `(Total money owed by Buyer X / Total receivables) * 100`. Trigger alert if > 40%. Slope of payment delays over the last 6 invoices detects early existential risk.
*   **GST Shortfall Trigger:** When GST due exceeds expected inflow in the next cycle, system raises a liquidity alert before the cash crunch manifests.

## 7. Required Domain Knowledge & Study Guide

*   **Account Aggregator (AA) Framework:** Learn consent-based financial data sharing. (Sahamati)
*   **The GST Paradox (Accrual vs. Cash Accounting):** Understand why GST is owed when the invoice is *generated*.
*   **Invoice Discounting:** Selling unpaid invoices to a bank for a small fee for instant cash.
*   **Time-Series ML:** Facebook Prophet to predict cash dips based on seasonal trends.
*   **Standard Deviation:** How variance creates "confidence intervals".
*   **WhatsApp/SMS Notification Logic:** Understand how critical cash alerts can be delivered to the user or judge.

## 8. Final Product Story for Judges
The product story must be crisp and easy to explain:

> "Our platform models the true liquidity problem faced by Indian MSMEs. Even when invoices are issued, GST creates a cash obligation before payment arrives. We simulate future cash flow, forecast risk, identify buyer concentration, test what-if stress scenarios, and recommend the best financing or recovery action."

This is the judge-facing narrative we must repeatedly validate against the work.

## 9. Working Rule: No Scope Drift
The project must never become a generic dashboard or a generic accounting tool. Every feature must trace back to one of the 9 steps above and one of the core business pains: delayed payments, GST shortfall, buyer concentration, and working capital stress.
