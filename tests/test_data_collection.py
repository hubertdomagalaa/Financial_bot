import unittest
from unittest.mock import patch
#from src.data_collection.data_collector import DataCollector

class TestDataCollector(unittest.TestCase):
    def setUp(self):
        """Set up a sample config for testing."""
        self.sample_config = {
            'data_sources': [
                {'name': 'Yahoo Finance', 'url': 'https://finance.yahoo.com'}
            ]
        }
        self.collector = DataCollector(self.sample_config)
    
    @patch('yfinance.Ticker')  # Mock yfinance Ticker to prevent actual API call
    def test_fetch_stock_data(self, mock_ticker):
        """Test fetching stock data for a valid ticker."""
        mock_ticker.return_value.info = {
            'currentPrice': 150,
            'trailingPE': 25,
            'debtToEquity': 1.2,
            'returnOnEquity': 0.18,
            'currentRatio': 1.5
        }
        
        data = self.collector.fetch_stock_data('AAPL')
        self.assertEqual(data['currentPrice'], 150)
        self.assertEqual(data['trailingPE'], 25)
    
    @patch('requests.get')  # Mock requests to prevent real HTTP calls
    def test_scrape_financial_news(self, mock_get):
        """Test scraping financial news from a mock webpage."""
        mock_get.return_value.text = "<html><body><p>Sample News Article</p></body></html>"
        
        news = self.collector.scrape_financial_news('https://mockurl.com')
        self.assertEqual(news, [])
    
    def test_collect_data(self):
        """Test full data collection pipeline for a stock."""
        with patch.object(self.collector, 'fetch_stock_data') as mock_fetch, \
             patch.object(self.collector, 'scrape_financial_news') as mock_scrape:
             
            mock_fetch.return_value = {'currentPrice': 150}
            mock_scrape.return_value = ["News Item 1", "News Item 2"]
            
            result = self.collector.collect_data('AAPL')
            self.assertIn('stock_data', result)
            self.assertIn('news', result)
            self.assertEqual(result['stock_data']['currentPrice'], 150)
            self.assertEqual(len(result['news']), 2)

if __name__ == "__main__":
    unittest.main()
