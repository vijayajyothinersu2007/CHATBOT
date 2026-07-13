import sqlite3
import os
from config import Config

def get_db_connection():
    """Returns a relational mapping operational link to our SQLite file."""
    conn = sqlite3.connect(Config.DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    # Enforce cascading referential actions inside SQLite engine
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def init_db():
    """Initializes tables and relation maps inside the SQLite cluster."""
    os.makedirs(Config.DB_FOLDER, exist_ok=True)
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Sessions log data table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS conversations (
            id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Chat records tracking details structure
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            conversation_id TEXT NOT NULL,
            sender TEXT CHECK(sender IN ('user', 'bot')) NOT NULL,
            message TEXT NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (conversation_id) REFERENCES conversations(id) ON DELETE CASCADE
        )
    ''')
    
    conn.commit()
    conn.close()
    print("Local database schema deployed successfully.")

if __name__ == '__main__':
    init_db()