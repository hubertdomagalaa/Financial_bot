from data_collector import DataCollector  # Import the DataCollector class

# If you want to test this module independently
if __name__ == "__main__":
    # Sample config for testing
    sample_config = {
        'data_sources': [{'name': 'Yahoo Finance'}]
    }
    
    collector = DataCollector(sample_config)

    # Test single stock
    single_stock_data = collector.collect_stock_data('AAPL')
    print("\nSingle Stock Data for AAPL:")
    print(single_stock_data)

    # Test multiple stocks
    tickers = ['AAPL', 'MSFT', 'GOOGL']
    multiple_stock_data = collector.collect_multiple_stocks(tickers)
    print("\nMultiple Stock Data:")
    for ticker, data in multiple_stock_data.items():
        print(f"\n{ticker}:")
        print(data)
