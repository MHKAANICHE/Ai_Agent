import os
from dotenv import load_dotenv
import google.generativeai as genai  # Correct import

# Load environment variables
load_dotenv()

class GeminiClient:
    def __init__(self):
        # Configure API
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.model = genai.GenerativeModel('gemini-2.0-flash')
    
    def generate_response(self, prompt):
        response = self.model.generate_content(prompt)
        return response.text

# Example usage
if __name__ == "__main__":
    ai = GeminiClient()
    print(ai.generate_response("Explain quantum computing in simple terms"))