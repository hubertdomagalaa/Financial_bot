# Financial Advisor Bot

The **Financial Advisor Bot** is a robust, AI-driven financial analysis tool designed to assist users in collecting, processing, analyzing, and generating insights on financial data. This project integrates **stock market data collection**, **news scraping**, **data preprocessing**, **financial analysis**, and **natural language-based reports** powered by machine learning models. The bot is built to streamline financial decision-making by automating key processes with cutting-edge technologies such as **Yahoo Finance API**, **Hugging Face transformers**, and more.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Modules](#modules)
  - [Data Collection](#data-collection)
  - [Data Preprocessing](#data-preprocessing)
  - [Financial Analysis](#financial-analysis)
  - [Language Model Integration](#language-model-integration)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/Financial_Advisor_Bot.git
    ```

2. Navigate to the project directory:
    ```bash
    cd Financial_Advisor_Bot
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Configuration**: 
   Edit the `config/config.yaml` file to set up the required data sources, financial metrics, normalization strategies, and API keys. Example configuration parameters include stock data APIs (e.g., Yahoo Finance), financial metrics (e.g., P/E ratio, debt-to-equity ratio), and model-specific settings (e.g., LLM model configurations).

2. **Run the Bot**: 
   Once configured, run the bot’s main script:
    ```bash
    python src/main.py
    ```

   The bot will collect stock data, preprocess the data, analyze financial metrics, and generate an AI-powered financial report.

3. **Example Use Case**:
   The bot fetches and processes stock data for companies like `AAPL`, `MSFT`, and `GOOGL`. It evaluates their financial health based on key ratios, normalizes the data, removes outliers, and uses a language model to summarize insights on the stock’s performance.

## Configuration

The configuration file `config/config.yaml` drives the functionality of the bot. You must customize this file to define data sources, financial metrics, normalization techniques, and model details.

### Example `config/config.yaml`:
```yaml
data_sources:
  - name: "Yahoo Finance"
    url: "https://finance.yahoo.com"
    
missing_data_strategies:
  pe_ratio: 'mean'
  debt_to_equity: 'zero'
  return_on_equity: 'drop'

normalization:
  current_price: 'min_max'
  pe_ratio: 'z_score'

min_values:
  current_price: 100
  pe_ratio: 5

max_values:
  current_price: 500
  pe_ratio: 40

llm:
  model: 'facebook/opt-350m'
  max_length: 100
  temperature: 0.7
```

## Modules

The bot is composed of several modules, each handling specific aspects of data collection, preprocessing, analysis, and reporting.

### Data Collection

- **`data_collector.py`**:
  - Collects stock market data and financial news from online sources such as Yahoo Finance.
  - Scrapes relevant financial headlines and article summaries using BeautifulSoup.
  - Fetches detailed stock data like **P/E ratio**, **debt-to-equity**, **current price**, and more.
  - Handles multiple tickers, allowing simultaneous data collection for multiple companies.

### Data Preprocessing

- **`data_preprocessing.py`**:
  - Preprocesses the collected data by handling missing values based on defined strategies (`mean`, `zero`, `drop`).
  - Normalizes key financial metrics using different techniques such as **min-max scaling**, **z-score normalization**, and **logarithmic scaling**.
  - Removes outliers using statistical techniques such as the **Interquartile Range (IQR)**.
  - Extensible with additional preprocessing pipelines (e.g., feature scaling for machine learning).

### Financial Analysis

- **`financial_analyzer.py`**:
  - Analyzes stock performance against predefined financial thresholds like P/E ratio, debt-to-equity, and return on equity.
  - Evaluates and flags metrics as "Good" or "Concern" based on whether they meet or exceed the set thresholds.
  - Generates structured reports on the financial health of companies based on the collected data.

### Language Model Integration

- **`llm_analyzer.py`**:
  - Integrates a **transformers-based language model** (such as `facebook/opt-350m`) to generate human-readable financial insights and summaries.
  - Prepares input prompts with stock performance data and returns detailed analyses.
  - Can be extended to integrate other language models for more complex insights or stock price predictions.

## Testing

### Unit Tests
The bot comes with unit tests for each key component:
- **`test_data_collection.py`**: Verifies the functionality of the data collection module, including stock data retrieval and news scraping.
- **`test_financial_metrics.py`**: Tests the financial metrics calculations and ensures accurate evaluations based on thresholds.

### Running Tests
Run all unit tests using the following command:
```bash
python -m unittest discover tests
```
This will run all the tests in the `tests` folder to ensure the bot is functioning as expected.

## Contributing

We welcome contributions from the community! If you would like to contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Submit a pull request for review.

Please refer to [CONTRIBUTING.md](CONTRIBUTING.md) for more detailed contribution guidelines.

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.
