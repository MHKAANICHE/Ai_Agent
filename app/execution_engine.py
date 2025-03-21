from .gemini_brain import GeminiCoder
from .file_ops import execute_command, list_files, analyze_project
from .librarian import Librarian  # New import
from datetime import datetime
import os

class CodeEngine:
    def __init__(self):
        self.ai = GeminiCoder()
        self.librarian = Librarian(session_id="github_codespace_1")
      
    def process_command(self, user_input):
            # Handle memory recall requests
            if "what did we do last" in user_input.lower():
                return self._recall_last_action(), "Memory recall complete"

            if "study all the files" in user_input.lower():
                return self.analyze_project(), "Analysis complete"

            # Get context from Librarian
            context = self._build_context(user_input)
            
            # Generate code with full context
            generated_code = self.ai.generate_code(user_input, context)
            
            # Execute and log
            result = execute_command(generated_code)
            self.librarian.log_interaction(user_input, generated_code, result)
            
            return generated_code, result
    def _recall_last_action(self):
            """Retrieve and format the last action from memory."""
            recent_history = self.librarian.get_recent_history(limit=1)
            if not recent_history:
                return "No recent actions found."
            
            last_action = recent_history[0]
            return f"Last Action:\n- Input: {last_action['input']}\n- Result: {last_action['result']}"
            
    def _build_context(self, user_input):
        """Combine memory sources for AI context"""
        return (
            f"Previous Interactions:\n{self._get_history()}\n"
            f"Project Structure:\n{list_files()}\n"
            f"Current Request: {user_input}"
        )

    def _get_history(self):
        """Format conversation history from Librarian"""
        recent_history = self.librarian.get_recent_history()
        return "\n".join(
            f"- {op['input']} → {op['result']}" 
            for op in recent_history
        )

    def analyze_project(self):
        """Analyze project files and determine capabilities"""
        project_structure = analyze_project()
        capabilities = []

        # Determine capabilities based on file types
        for path, data in project_structure.items():
            if ".py" in data["file_types"]:
                capabilities.append("Python development")
            if ".js" in data["file_types"] or ".ts" in data["file_types"]:
                capabilities.append("JavaScript/TypeScript development")
            if ".html" in data["file_types"]:
                capabilities.append("Web development")
            if ".md" in data["file_types"]:
                capabilities.append("Documentation support")

        return "Capabilities: " + ", ".join(set(capabilities))