class FinancialAnalyzer:
    def __init__(self, config):
        self.config = config
        self.metrics = {metric['name']: metric['threshold'] for metric in config['financial_metrics']}

    def analyze(self, stock_data):
        analysis = {}

        # P/E Ratio
        if stock_data['pe_ratio'] is not None:
            analysis['P/E Ratio'] = self._analyze_metric('P/E Ratio', stock_data['pe_ratio'], lower_is_better=True)

        # Debt to Equity
        if stock_data['debt_to_equity'] is not None:
            analysis['Debt to Equity'] = self._analyze_metric('Debt to Equity', stock_data['debt_to_equity'] / 100, lower_is_better=True)

        # Return on Equity
        if stock_data['return_on_equity'] is not None:
            analysis['Return on Equity'] = self._analyze_metric('Return on Equity', stock_data['return_on_equity'] * 100, lower_is_better=False)

        # Current Ratio
        if stock_data['current_ratio'] is not None:
            analysis['Current Ratio'] = self._analyze_metric('Current Ratio', stock_data['current_ratio'], lower_is_better=False)

        return analysis

    def _analyze_metric(self, metric_name, value, lower_is_better):
        threshold = self.metrics.get(metric_name)
        if threshold is None:
            return f"{value:.2f} (No threshold set)"

        if lower_is_better:
            status = "Good" if value < threshold else "Concern"
        else:
            status = "Good" if value > threshold else "Concern"

        return f"{value:.2f} ({status})"

# If you want to test this module independently
if __name__ == "__main__":
    # Sample config for testing
    sample_config = {
        'financial_metrics': [
            {'name': 'P/E Ratio', 'threshold': 20},
            {'name': 'Debt to Equity', 'threshold': 1.5},
            {'name': 'Return on Equity', 'threshold': 15},
            {'name': 'Current Ratio', 'threshold': 1.5}
        ]
    }
    
    analyzer = FinancialAnalyzer(sample_config)
    sample_data = {
        'pe_ratio': 25,
        'debt_to_equity': 120,
        'return_on_equity': 0.18,
        'current_ratio': 1.2
    }
    analysis = analyzer.analyze(sample_data)
    print(analysis)