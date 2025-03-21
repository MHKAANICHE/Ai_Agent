from datetime import datetime
from .mongo_db import StateDB



class Librarian:
    def __init__(self, session_id="default_session"):
        self.db = StateDB()
        self.session_id = session_id

    def log_interaction(self, user_input, ai_response, result):
        """Log a user-AI interaction with metadata."""
        self.db.log_operation(self.session_id, {
            "timestamp": datetime.now(),
            "input": user_input,
            "response": ai_response,
            "result": result,
            "tags": self._generate_tags(user_input, ai_response, result)
        })

    def get_recent_history(self, limit=5):
        """Retrieve recent interactions for context."""
        history = self.db.get_history(self.session_id)
        return history.get("operations", [])[-limit:]

    def summarize_history(self):
        """Generate a summary of key decisions."""
        history = self.db.get_history(self.session_id)
        decisions = [op["input"] for op in history.get("operations", []) if "decision" in op.get("tags", [])]
        return "Key Decisions:\n- " + "\n- ".join(decisions)

    def _generate_tags(self, user_input, ai_response, result):
        """Auto-generate tags for interactions."""
        tags = []
        if "create_file" in ai_response:
            tags.append("file_creation")
        if "error" in result.lower():
            tags.append("needs_fix")
        if "decision" in user_input.lower():
            tags.append("decision")
        return tags

