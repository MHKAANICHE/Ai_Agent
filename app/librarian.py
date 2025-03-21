from datetime import datetime
from .mongo_db import StateDB
import os

class Librarian:
    def __init__(self, session_id="default_session"):
        self.db = StateDB()
        self.session_id = session_id
        self.short_term_memory = []
        self.summary_interval = 5  # Summarize every 5 interactions

    def log_interaction(self, user_input, ai_response, result):
        """Store interaction in both short-term and long-term memory"""
        interaction = {
            "timestamp": datetime.now(),
            "input": user_input,
            "response": ai_response,
            "result": result,
            "tags": self._generate_tags(user_input, ai_response, result)
        }
        
        # Store in short-term memory
        self.short_term_memory.append(interaction)
        
        # Store in long-term DB
        self.db.log_operation(self.session_id, interaction)
        
        # Generate summaries periodically
        if len(self.short_term_memory) % self.summary_interval == 0:
            self._create_summary()

    def get_context(self):
        """Combine recent interactions and key summaries"""
        return {
            "recent": self.get_recent_history(),
            "summaries": self.get_key_summaries(),
            "project_state": self.get_project_snapshot()
        }

    def get_recent_history(self, limit=5):
        """Get recent interactions from short-term memory"""
        return self.short_term_memory[-limit:]

    def get_key_summaries(self):
        """Retrieve important decisions from long-term storage"""
        return self.db.get_summaries(self.session_id)

    def _create_summary(self):
        """Generate and store summary of recent interactions"""
        summary = {
            "type": "summary",
            "timestamp": datetime.now(),
            "content": self._generate_summary_content(),
            "covered_interactions": len(self.short_term_memory)
        }
        self.db.log_summary(self.session_id, summary)
        self.short_term_memory = []  # Reset short-term buffer

    def _generate_tags(self, user_input, ai_response, result):
        """Auto-tag interactions for better retrieval"""
        tags = []
        if "create_file" in ai_response:
            tags.append("file_operation")
        if "error" in result.lower():
            tags.append("needs_attention")
        if any(word in user_input.lower() for word in ["decision", "choose", "select"]):
            tags.append("design_decision")
        return tags

    def _generate_summary_content(self):
        """Create human-readable summary of recent interactions"""
        return "\n".join(
            f"- {item['input']} → {item['result']}"
            for item in self.short_term_memory
        )

    def get_project_snapshot(self):
        """Capture current project state for context"""
        return {
            "files": self._list_project_files(),
            "structure": self._analyze_project_structure(),
            "recent_changes": self._get_recent_changes()
        }

    def _list_project_files(self):
        """List all files in the project"""
        files = []
        for root, _, filenames in os.walk("."):
            for filename in filenames:
                files.append(os.path.join(root, filename))
        return files

    def _analyze_project_structure(self):
        """Analyze project directory structure"""
        structure = {}
        for root, dirs, files in os.walk("."):
            relative_path = os.path.relpath(root, ".")
            structure[relative_path] = {
                "files": files,
                "file_types": set(os.path.splitext(f)[1] for f in files)
            }
        return structure

    def _get_recent_changes(self):
        """Retrieve recent file modifications"""
        recent_changes = []
        for interaction in self.short_term_memory:
            if "file_operation" in interaction.get("tags", []):
                recent_changes.append({
                    "file": self._extract_file_from_code(interaction["response"]),
                    "operation": interaction["input"]
                })
        return recent_changes

    def _extract_file_from_code(self, code):
        """Extract file path from generated code"""
        if "create_file(" in code:
            return code.split("create_file(")[1].split(",")[0].strip("'\"")
        return "unknown"    