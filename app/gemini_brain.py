import os
import google.generativeai as genai
from dotenv import load_dotenv


import os
import google.generativeai as genai


class GeminiCoder:
    def __init__(self):
        
        # Load API key from .env
        # load_dotenv()
        # api_key = os.getenv("GEMINI_API_KEY")


        # CORRECTED API ENDPOINT
        # Load API key from GitHub Secrets
        genai.configure(
            api_key=os.getenv("GEMINI_API_KEY"),
            transport='rest',
            client_options={
                'api_endpoint': 'https://generativelanguage.googleapis.com/'  # v1 instead of v1beta
            }
        )
        
        self.model = genai.GenerativeModel('gemini-2.0-flash')  # Verified working name

   

    def generate_code(self, prompt, context):
        try:
            response = self.model.generate_content(f"""
            You are an AI coding assistant. Convert this request into Python code:
            
            User request: {prompt}
            
            Available functions:
            - create_file(path, content)  # Automatically creates directories
            - read_file(path)
            
            Current project files:
            {context}
            
            Respond ONLY with executable Python code.
            """)
            return response.text.strip().replace("```python", "").replace("```", "")
        except Exception as e:
            print(f"⚠️ AI Error: {str(e)}")
            return "print('Failed to generate valid code')"             