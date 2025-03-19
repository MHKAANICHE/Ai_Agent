from pymongo import MongoClient
import os
from dotenv import load_dotenv  # Add this line

class StateDB:
    def __init__(self):
        load_dotenv()  # Load environment variables
        self.client = MongoClient(os.getenv("MONGO_URI"))
        self.db = self.client[os.getenv("DB_NAME", "code_copilot")]  # Add default
        self.sessions = self.db.sessions
    
    def log_operation(self, session_id, operation):
        self.sessions.update_one(
            {"session_id": session_id},
            {"$push": {"operations": operation}},
            upsert=True
        )
    
    def get_history(self, session_id):
        return self.sessions.find_one({"session_id": session_id}) or {"operations": []}