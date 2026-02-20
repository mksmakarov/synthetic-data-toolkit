from dotenv import load_dotenv
from openai import OpenAI, OpenAIError
import os
import datetime
import logging

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class SyntheticDataGenerator:
    def __init__(self, api_key=None, model="gpt-4o-mini"):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=self.api_key)
        self.model = model
    
    def generate(self, prompt, max_tokens=1000, temperature=0.7):
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=max_tokens,
                temperature=temperature
            )
            return response.choices[0].message.content.strip()
        except OpenAIError as e:
            logging.error("OpenAI API error: %s", e)
            return None
        except (IndexError, AttributeError, KeyError) as e:
            logging.error("Unexpected response structure: %s", e)
            return None
        except Exception as e:
            logging.exception("An unexpected error occurred")
            return None

class CSVSyntheticDataGenerator(SyntheticDataGenerator):
    def __init__(self):
        super().__init__()
    
    def run(self, prompt, max_tokens=1000, temperature=0.7):
        '''
        @param filename: str - file with prompt.
        '''
        relative_dir = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(relative_dir, prompt), 'r') as f:
            prompt = f.read()
        response = self.generate(prompt, max_tokens=max_tokens, temperature=temperature)
        self.__save_to_csv(response)
    
    def __save_to_csv(self, response):
        try:
            filename = f"synthetic_data_{int(datetime.datetime.now().timestamp())}.csv"
            with open(filename, 'w') as f:
                f.write(response)
            logging.info(f"Synthetic data saved to {filename}")
        except Exception as e:
            logging.error("Error saving to CSV: %s", e)
