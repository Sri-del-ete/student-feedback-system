import sqlite3

def init_db():
    # This creates a database file named 'feedback.db'
    conn = sqlite3.connect('feedback.db')
    cursor = conn.cursor()
    # Create a table for the feedback if it doesn't already exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            message TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
    print("Database initialized successfully!")