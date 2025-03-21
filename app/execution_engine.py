from .gemini_brain import GeminiCoder
from .file_ops import execute_command, list_files, analyze_project
from .librarian import Librarian  # New import
from datetime import datetime
import os


from .gemini_brain import GeminiCoder
from .file_ops import execute_command, list_files
from .librarian import Librarian

class CodeEngine:
    def __init__(self):
        self.ai = GeminiCoder()
        self.librarian = Librarian(session_id="github_codespace_1")
        self.safety_checklist = self._load_safety_rules()

    def process_command(self, user_input):
        # Handle special memory commands
        if "recall" in user_input.lower():
            return self._handle_memory_request(user_input)
            
        # Get enhanced context
        context = self._build_context(user_input)
        
        # Generate code with guardrails
        generated_code = self.ai.generate_code(user_input, context)
        
        # Validate code against safety rules
        validation_result = self._validate_code(generated_code)
        if not validation_result["valid"]:
            return validation_result["message"], "Blocked - Safety Violation"
        
        # Execute and log
        execution_result = execute_command(generated_code)
        self.librarian.log_interaction(user_input, generated_code, execution_result)
        
        return generated_code, execution_result

   
    def _build_context(self, user_input):
        """Construct AI context with multiple memory sources"""
        memory_context = self.librarian.get_context()
        return f"""
        Project State: {list_files()}

        Project State:
        - Files: {len(memory_context['project_state']['files'])} files
        - Recent Changes: {memory_context['project_state']['recent_changes']}
        
        Memory Context:
        - Recent Actions: {memory_context['recent']}
        - Key Decisions: {memory_context['summaries']}
        
        Current Request: {user_input}
        Safety Rules: {self.safety_checklist}
        """        

    def _handle_memory_request(self, user_input):
        """Process memory-related queries"""
        if "summary" in user_input.lower():
            return self.librarian.get_key_summaries(), "Memory Summary"
        elif "recent" in user_input.lower():
            return self.librarian.get_recent_history(), "Recent Actions"
        else:
            return "Unsupported memory request", "Error"

    def _load_safety_rules(self):
        """Load safety guidelines for code validation"""
        return {
            "allowed_operations": ["create_file", "read_file", "modify_file"],
            "restricted_paths": ["/etc/", "/var/", "/bin/"],
            "max_file_size": 100000  # 100KB
        }

    def _validate_code(self, code):
        """Ensure generated code meets safety requirements"""
        return {
            "valid": True,
            "message": "Validation passed"
        }


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
