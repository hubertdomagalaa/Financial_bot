import yaml

class FinancialMetrics:
    def __init__(self, config_path):
        with open(config_path, 'r') as file:
            self.config = yaml.safe_load(file)
        self.thresholds = {metric['name']: metric['threshold'] for metric in self.config['financial_metrics']}

    def calculate_pe_ratio(self, price, earnings):
        return price / earnings if earnings != 0 else float('inf')

    def calculate_debt_to_equity(self, total_debt, total_equity):
        return total_debt / total_equity if total_equity != 0 else float('inf')

    def evaluate_metrics(self, stock_data):
        pe_ratio = self.calculate_pe_ratio(stock_data['currentPrice'], stock_data['trailingEps'])
        debt_to_equity = self.calculate_debt_to_equity(stock_data['totalDebt'], stock_data['totalStockholderEquity'])

        evaluation = {
            'P/E Ratio': {'value': pe_ratio, 'status': 'Good' if pe_ratio < self.thresholds['P/E Ratio'] else 'Concern'},
            'Debt to Equity': {'value': debt_to_equity, 'status': 'Good' if debt_to_equity < self.thresholds['Debt to Equity'] else 'Concern'}
        }

        return evaluation

if __name__ == "__main__":
    metrics = FinancialMetrics('config/config.yaml')
    sample_data = {
        'currentPrice': 150,
        'trailingEps': 5,
        'totalDebt': 100000000,
        'totalStockholderEquity': 200000000
    }
    evaluation = metrics.evaluate_metrics(sample_data)
    print(evaluation)