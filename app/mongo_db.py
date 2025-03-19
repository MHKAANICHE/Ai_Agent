from pymongo import MongoClient
import os
from dotenv import load_dotenv  # Add this line

class StateDB:
    def __init__(self):
        # Load environment variables
        mongo_uri = os.getenv("MONGO_URI")
        db_name = os.getenv("DB_NAME", "code_copilot")  # Default to "code_copilot" if not set
        
        if not mongo_uri:
            raise ValueError("MONGO_URI environment variable is not set")
        
        self.client = MongoClient(mongo_uri)
        self.db = self.client[db_name]
        self.sessions = self.db.sessions
    
    def log_operation(self, session_id, operation):
        self.sessions.update_one(
            {"session_id": session_id},
            {"$push": {"operations": operation}},
            upsert=True
        )
    
    def get_history(self, session_id):
        return self.sessions.find_one({"session_id": session_id}) or {"operations": []}
