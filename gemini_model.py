# gemini_model.py

import os
import logging
import genai  # Assuming 'genai' is the correct module for Google Gemini

class GeminiModel:
    def __init__(self):
        # Fetch the API key from environment variables
        self.api_key = os.getenv('GEMINI_API_KEY')
        if not self.api_key:
            raise ValueError("API key not found. Please set the GEMINI_API_KEY environment variable.")
        
        # Configure the API client with the API key
        genai.configure(api_key=self.api_key)
        
        # Initialize the model, assuming 'gemini-1.5-flash' is the correct model ID
        self.model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Set up logging for debugging and information purposes
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("GeminiModel initialized.")
    
    def query_llm(self, question):
        """
        Sends a question to the Google Gemini API and returns the response.

        :param question: The question to ask the LLM.
        :return: The response text from the LLM.
        """
        try:
            logging.debug(f"Sending question to LLM: {question}")
            
            # Assuming 'generate' is the method to get a response from the LLM
            response = self.model.generate(prompt=question, max_tokens=150)
            
            logging.debug(f"Received response: {response}")
            return response['choices'][0]['text'].strip()
        except Exception as e:
            logging.error(f"Error querying LLM: {e}")
            return f"Error querying LLM: {e}"

