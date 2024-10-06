from transformers import AutoTokenizer, AutoModelForCausalLM
import torch 



class LLMAnalyzer:
    def __init__(self, config):
        self.config = config['llm']
        self.tokenizer = AutoTokenizer.from_pretrained(self.config['model'])
        self.model = AutoModelForCausalLM.from_pretrained(self.config['model'])

    def generate_analysis(self, financial_data):
        # Prepare the prompt
        prompt = f"Analyze the following financial data:\n{financial_data}\n\nAnalysis:"
        
        # Tokenize the input
        inputs = self.tokenizer(prompt, return_tensors="pt")
        
        # Generate the output
        with torch.no_grad():
            outputs = self.model.generate(
                inputs.input_ids,
                max_length=self.config['max_length'],
                temperature=self.config['temperature'],
                num_return_sequences=1,
            )
        
        # Decode and return the generated text
        analysis = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return analysis.split("Analysis:")[1].strip()

# Test the LLMAnalyzer
if __name__ == "__main__":
    sample_config = {
        'llm': {
            'model': 'facebook/opt-350m',
            'max_length': 100,
            'temperature': 0.7
        }
    }
    analyzer = LLMAnalyzer(sample_config)
    sample_data = "P/E Ratio: 15.2, Debt to Equity: 1.1, Return on Equity: 22%, Current Ratio: 1.8"
    analysis = analyzer.generate_analysis(sample_data)
    print(analysis)

    def generate_analysis(self, financial_data):
        # Prepare the prompt
        prompt = f"Analyze the following financial data:\n{financial_data}\n\nAnalysis:"
        
        # Tokenize the input
        inputs = self.tokenizer(prompt, return_tensors="pt")
        
        # Generate the output
        with torch.no_grad():
            outputs = self.model.generate(
                inputs.input_ids,
                max_length=self.config['max_length'],
                temperature=self.config['temperature'],
                num_return_sequences=1,
            )
        
        # Decode and return the generated text
        analysis = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return analysis.split("Analysis:")[1].strip()

# Test the LLMAnalyzer
if __name__ == "__main__":
    sample_config = {
        'llm': {
            'model': 'facebook/opt-350m',
            'max_length': 100,
            'temperature': 0.7
        }
    }
    analyzer = LLMAnalyzer(sample_config)
    sample_data = "P/E Ratio: 15.2, Debt to Equity: 1.1, Return on Equity: 22%, Current Ratio: 1.8"
    analysis = analyzer.generate_analysis(sample_data)
    print(analysis)