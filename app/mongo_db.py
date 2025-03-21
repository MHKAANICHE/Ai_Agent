from pymongo import MongoClient
import os

class StateDB:
    def __init__(self):
        mongo_uri = os.getenv("MONGO_URI")
        db_name = os.getenv("DB_NAME", "code_copilot")
        
        if not mongo_uri:
            raise ValueError("MONGO_URI environment variable is not set")
        
        self.client = MongoClient(mongo_uri)
        self.db = self.client[db_name]
        self.sessions = self.db.sessions
        self.summaries = self.db.summaries

    def log_operation(self, session_id, operation):
        """Store individual interaction"""
        self.sessions.update_one(
            {"session_id": session_id},
            {"$push": {"operations": operation}},
            upsert=True
        )

    def log_summary(self, session_id, summary):
        """Store generated summary"""
        self.summaries.update_one(
            {"session_id": session_id},
            {"$push": {"summaries": summary}},
            upsert=True
        )

    def get_history(self, session_id):
        """Retrieve full interaction history"""
        return self.sessions.find_one({"session_id": session_id}) or {"operations": []}

    def get_summaries(self, session_id):
        """Retrieve all summaries for a session"""
        return self.summaries.find_one({"session_id": session_id}) or {"summaries": []}