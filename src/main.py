import yaml
from data_collector import DataCollector
from financial_analyzer import FinancialAnalyzer
from llm_analyzer import LLMAnalyzer



def load_config(config_path='/home/hubini/coding/Financial_Advisor_Bot/financial_advisor/config/config.yaml'):

    with open(config_path, 'r') as file:
        return yaml.safe_load(file)

def main():
    # Load configuration
    config = load_config()
  


    # Initialize modules
    data_collector = DataCollector(config)
    financial_analyzer = FinancialAnalyzer(config)
    llm_analyzer = LLMAnalyzer(config)
    
    # Get user input
    ticker = input("Enter a stock ticker symbol: ")
    
    # Collect data
    stock_data = data_collector.collect_stock_data(ticker)
    
    # Analyze data
    analysis = financial_analyzer.analyze(stock_data)
    
    # Print results
    print(f"\nAnalysis for {ticker}:")
    for metric, value in analysis.items():
        print(f"{metric}: {value}")
    
    # Generate LLM analysis
    llm_input = ", ".join([f"{k}: {v}" for k, v in analysis.items()])
    llm_analysis = llm_analyzer.generate_analysis(llm_input)
    
    print("\nLLM Analysis:")
    print(llm_analysis)

if __name__ == "__main__":
    main()