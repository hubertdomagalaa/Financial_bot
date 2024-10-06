import unittest
from src.financial_metrics.metrics import FinancialMetrics

class TestFinancialMetrics(unittest.TestCase):
    def setUp(self):
        """Set up a sample config for testing."""
        self.sample_config = {
            'financial_metrics': [
                {'name': 'P/E Ratio', 'threshold': 20},
                {'name': 'Debt to Equity', 'threshold': 1.5}
            ]
        }
        self.metrics = FinancialMetrics('config/sample_config.yaml')
        self.metrics.thresholds = {
            'P/E Ratio': 20,
            'Debt to Equity': 1.5
        }

    def test_calculate_pe_ratio(self):
        """Test the calculation of P/E Ratio."""
        price = 150
        earnings = 10
        result = self.metrics.calculate_pe_ratio(price, earnings)
        self.assertEqual(result, 15)
    
    def test_calculate_debt_to_equity(self):
        """Test the calculation of Debt to Equity."""
        total_debt = 100000
        total_equity = 200000
        result = self.metrics.calculate_debt_to_equity(total_debt, total_equity)
        self.assertEqual(result, 0.5)

    def test_evaluate_metrics(self):
        """Test the evaluation of multiple financial metrics."""
        stock_data = {
            'currentPrice': 150,
            'trailingEps': 5,
            'totalDebt': 100000,
            'totalStockholderEquity': 200000
        }
        
        result = self.metrics.evaluate_metrics(stock_data)
        
        # P/E Ratio should be good because 150/5 = 30, which is less than 20
        self.assertEqual(result['P/E Ratio']['status'], 'Concern')
        # Debt to Equity should be good because 100000/200000 = 0.5, which is below 1.5
        self.assertEqual(result['Debt to Equity']['status'], 'Good')

if __name__ == "__main__":
    unittest.main()
