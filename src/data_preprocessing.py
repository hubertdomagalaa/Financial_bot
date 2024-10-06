import pandas as pd
import numpy as np

class Preprocessor:
    def __init__(self, config):
        self.config = config

    def handle_missing_data(self, stock_data):
        """Fills missing values with specified strategies."""
        for key, strategy in self.config['missing_data_strategies'].items():
            if key in stock_data and stock_data[key] is None:
                if strategy == 'mean':
                    stock_data[key] = np.mean([v for v in stock_data.values() if v is not None])
                elif strategy == 'zero':
                    stock_data[key] = 0
                elif strategy == 'drop':
                    stock_data[key] = None  # Mark for potential dropping later
        return stock_data

    def normalize_data(self, stock_data):
        """Applies normalization to certain metrics based on config."""
        if 'normalization' in self.config:
            for metric, norm_type in self.config['normalization'].items():
                if metric in stock_data and stock_data[metric] is not None:
                    if norm_type == 'min_max':
                        stock_data[metric] = (stock_data[metric] - self.config['min_values'][metric]) / (
                                self.config['max_values'][metric] - self.config['min_values'][metric])
                    elif norm_type == 'z_score':
                        stock_data[metric] = (stock_data[metric] - np.mean(stock_data[metric])) / np.std(stock_data[metric])
        return stock_data

    def preprocess(self, stock_data):
        """Complete preprocessing pipeline for stock data."""
        stock_data = self.handle_missing_data(stock_data)
        stock_data = self.normalize_data(stock_data)
        # Add more preprocessing steps if needed
        return stock_data

# Test the Preprocessor module
if __name__ == "__main__":
    sample_config = {
        'missing_data_strategies': {
            'pe_ratio': 'mean',
            'debt_to_equity': 'zero',
            'return_on_equity': 'drop'
        },
        'normalization': {
            'current_price': 'min_max',
            'pe_ratio': 'z_score'
        },
        'min_values': {'current_price': 100, 'pe_ratio': 5},
        'max_values': {'current_price': 500, 'pe_ratio': 40}
    }

    sample_stock_data = {
        'symbol': 'AAPL',
        'current_price': 150,
        'pe_ratio': None,
        'debt_to_equity': None,
        'return_on_equity': 0.18
    }

    preprocessor = Preprocessor(sample_config)
    preprocessed_data = preprocessor.preprocess(sample_stock_data)
    print(preprocessed_data)
