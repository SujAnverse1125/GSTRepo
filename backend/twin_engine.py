import numpy as np
import datetime
from typing import List, Dict, Any

class DigitalTwinEngine:
    """
    Core Mathematical Engine for the MSME Digital Twin.
    Responsible for Stage 3, 4, 5, and 7 of the blueprint.
    Implements deterministic math and statistical ML logic for cash flow,
    GST liability paradox tracking, and buyer variance analysis.
    """

    def __init__(self):
        pass

    def calculate_daily_balance(self, previous_balance: float, inflows: List[float], outflows: List[float]) -> float:
        """
        Digital Twin Daily Balance Formula.
        
        Formula:
        DB_t = DB_{t-1} + Σ(Inflows_t) - Σ(Outflows_t)
        
        Where:
        - DB_t: Daily Balance at day t
        - DB_{t-1}: Daily Balance at previous day
        - Inflows_t: All cash entering on day t
        - Outflows_t: All cash leaving on day t
        
        Returns:
            Calculated daily balance for day t.
        """
        return previous_balance + sum(inflows) - sum(outflows)

    def calculate_buyer_variance(self, payment_delays: List[float]) -> Dict[str, float]:
        """
        Buyer Payment Weighting and Standard Deviation confidence intervals.
        
        Formula for Standard Deviation (σ):
        σ = sqrt( Σ(x_i - μ)² / N )
        Where:
        - x_i: Individual payment delay in days
        - μ: Mean payment delay
        - N: Total number of payments
        
        Confidence Interval:
        CI = μ ± Z * (σ / sqrt(N))
        
        Returns:
            Dictionary containing mean delay, standard deviation, and confidence intervals.
        """
        if not payment_delays:
            return {"mean": 0.0, "std_dev": 0.0, "ci_lower": 0.0, "ci_upper": 0.0}
            
        mean = np.mean(payment_delays)
        std_dev = np.std(payment_delays, ddof=0)
        n = len(payment_delays)
        
        # 95% Confidence Interval (Z ≈ 1.96)
        z = 1.96
        margin_of_error = z * (std_dev / np.sqrt(n)) if n > 0 else 0
        
        return {
            "mean": float(mean),
            "std_dev": float(std_dev),
            "ci_lower": float(mean - margin_of_error),
            "ci_upper": float(mean + margin_of_error)
        }

    def check_gst_liquidity_paradox(self, invoices: List[Dict[str, Any]]) -> Dict[str, float]:
        """
        GST Liability Paradox tracker.
        
        Loops through a list of mock invoices, calculates 18% of the amount, 
        and returns a dictionary of tax liabilities mapped to the 20th of the 
        month following the invoice `issue_date`.
        
        Expected invoice format: {"id": "INV-1", "amount": 1000.0, "issue_date": "2026-08-15"}
        
        Returns:
            Dictionary mapping due date string (YYYY-MM-DD) to total GST liability.
        """
        liabilities = {}
        
        for invoice in invoices:
            amount = invoice.get("amount", 0.0)
            issue_date_str = invoice.get("issue_date")
            if not issue_date_str:
                continue
                
            issue_date = datetime.datetime.strptime(issue_date_str, "%Y-%m-%d").date()
            
            # Due on the 20th of the following month
            if issue_date.month == 12:
                due_month = 1
                due_year = issue_date.year + 1
            else:
                due_month = issue_date.month + 1
                due_year = issue_date.year
                
            due_date = datetime.date(due_year, due_month, 20).strftime("%Y-%m-%d")
            
            # 18% GST liability
            gst_amount = amount * 0.18
            
            liabilities[due_date] = liabilities.get(due_date, 0.0) + gst_amount
            
        return liabilities
