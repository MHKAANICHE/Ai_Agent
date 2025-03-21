from datetime import datetime
from .mongo_db import StateDB

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
            "summaries": self.get_key_summaries()
            #,"project_state": self.get_project_snapshot()
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