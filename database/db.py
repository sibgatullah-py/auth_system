import sqlite3
import os
from datetime import datetime

class DatabaseManager:
    def __init__(self, db_path: str = "data/auth.db"):
        dirpath = os.path.dirname(db_path)
        if dirpath:
            os.makedirs(dirpath, exist_ok=True)

        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        
        self._create_tables()
    
    def _create_tables(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE NOT NULL,
                username TEXT NOT NULL,
                password_hash TEXT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        self.conn.commit()
        
    def close(self):
        self.conn.close()