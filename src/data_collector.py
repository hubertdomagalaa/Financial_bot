import yfinance as yf

class DataCollector:
    def __init__(self, config):
        self.config = config

    def collect_stock_data(self, ticker):
        try:
            stock = yf.Ticker(ticker)
            info = stock.info
            if not info:
                raise ValueError(f"No stock data found for ticker {ticker}")
        except Exception as e:
            print(f"Error fetching data for {ticker}: {e}")
            return {}

        # Collect additional financial metrics
        data = {
            'symbol': ticker,
            'current_price': info.get('currentPrice', None),
            'market_cap': info.get('marketCap', None),
            'pe_ratio': info.get('trailingPE', None),
            'dividend_yield': info.get('dividendYield', None),
            '52_week_high': info.get('fiftyTwoWeekHigh', None),
            '52_week_low': info.get('fiftyTwoWeekLow', None),
            'debt_to_equity': info.get('debtToEquity', None),
            'return_on_equity': info.get('returnOnEquity', None),
            'current_ratio': info.get('currentRatio', None),
            'earnings_growth': info.get('earningsGrowth', None),
            'revenue_growth': info.get('revenueGrowth', None)
        }
        
        return data

    def collect_multiple_stocks(self, tickers):
        """Collect data for multiple stock tickers."""
        stock_data = {}
        for ticker in tickers:
            data = self.collect_stock_data(ticker)
            if data:
                stock_data[ticker] = data
        return stock_data
''''
# If you want to test this module independently
if __name__ == "__main__":
    # Sample config for testing
    sample_config = {'data_sources': [{'name': 'Yahoo Finance'}]}
    
    collector = DataCollector(sample_config)
    data = collector.collect_stock_data('AAPL')
    print(data)
'''