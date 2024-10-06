import yfinance as yf
import requests
import yaml
from bs4 import BeautifulSoup

class DataCollector:
    def __init__(self, config_path):
        # Load configuration from the provided YAML file
        with open(config_path, 'r') as file:
            self.config = yaml.safe_load(file)

    def fetch_stock_data(self, ticker):
        """Fetch stock data for a single ticker from Yahoo Finance."""
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

        # Optionally handle missing or invalid data
        for key, value in data.items():
            if value is None:
                print(f"Warning: {key} data missing for {ticker}")

        return data

    def collect_multiple_stocks(self, tickers):
        """Collect data for multiple stock tickers."""
        stock_data = {}
        for ticker in tickers:
            data = self.fetch_stock_data(ticker)
            if data:
                stock_data[ticker] = data
        return stock_data

    def scrape_financial_news(self, url):
        """Scrape financial news from a given URL."""
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')

            news_items = []
            articles = soup.find_all('article')  # Adjust based on website structure

            for article in articles:
                headline_tag = article.find('h3')
                link_tag = article.find('a')
                time_tag = article.find('time')

                if headline_tag and link_tag:
                    headline = headline_tag.get_text().strip()
                    link = link_tag['href'] if 'href' in link_tag.attrs else None
                    publication_date = time_tag.get_text().strip() if time_tag else "Unknown"

                    news_items.append({
                        'headline': headline,
                        'link': link,
                        'publication_date': publication_date
                    })

            return news_items
        except requests.RequestException as e:
            print(f"Error fetching news from {url}: {e}")
            return []

    def collect_data(self, ticker):
        """Collect both stock data and financial news."""
        stock_data = self.fetch_stock_data(ticker)
        news = self.scrape_financial_news(self.config['data_sources'][0]['url'])
        return {'stock_data': stock_data, 'news': news}


if __name__ == "__main__":
    # Load the config file
    collector = DataCollector('config/config.yaml')

    # Test single stock collection
    stock_data = collector.collect_data('AAPL')
    print("\nSingle Stock Data for AAPL:")
    print(stock_data)

    # Test multiple stocks collection
    tickers = ['AAPL', 'MSFT', 'GOOGL']
    multiple_stock_data = collector.collect_multiple_stocks(tickers)
    print("\nMultiple Stock Data:")
    for ticker, data in multiple_stock_data.items():
        print(f"\n{ticker}:")
        print(data)
