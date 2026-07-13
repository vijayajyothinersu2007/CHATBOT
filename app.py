import os
from flask import Flask, render_template
from config import Config
from database import get_db_connection
from routes.chat_routes import chat_blueprint

app = Flask(__name__)
app.config.from_object(Config)

# Register the chat and history blueprints
app.register_blueprint(chat_blueprint)

def init_db():
    """Initializes the local SQLite database schema safely if tables don't exist."""
    try:
        conn = get_db_connection()
        
        # Create Conversations table
        conn.execute('''
            CREATE TABLE IF NOT EXISTS conversations (
                id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Create Messages table with Foreign Key reference
        conn.execute('''
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                conversation_id TEXT NOT NULL,
                sender TEXT NOT NULL,
                message TEXT NOT NULL,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (conversation_id) REFERENCES conversations (id) ON DELETE CASCADE
            )
        ''')
        
        conn.commit()
        conn.close()
        print("Local database schema deployed and verified successfully.")
    except Exception as e:
        print(f"Database initialization alert: {e}")

@app.route('/')
def index():
    """Renders the main single-page UI dashboard."""
    return render_template('index.html')

if __name__ == '__main__':
    # Initialize SQLite structural layers before starting the server
    init_db()
    
    # Run the Flask production-ready development node
    app.run(debug=True, port=5000)