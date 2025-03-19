from .gemini_brain import GeminiCoder
from .file_ops import execute_command, list_files  # Updated import
from .mongo_db import StateDB
import os

class CodeEngine:
    def __init__(self):
        self.ai = GeminiCoder()
        self.db = StateDB()
        self.session_id = "github_codespace_1"
    
    def process_command(self, user_input):
        # Get context
        context = f"Project files:\n{list_files()}"  # Now properly imported
        
        # Generate code
        generated_code = self.ai.generate_code(user_input, context)
        
        # Execute and log
        result = execute_command(generated_code)
        self.db.log_operation(self.session_id, {
            "input": user_input,
            "code": generated_code,
            "result": result
        })
        
        return generated_code, result