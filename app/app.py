from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from database import init_db

app = Flask(__name__)

# Initialize the database when the app starts
init_db()

# Helper function to connect to the database
def get_db_connection():
    conn = sqlite3.connect('feedback.db')
    conn.row_factory = sqlite3.Row  # This lets us access columns by name
    return conn

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the data from the HTML form
        name = request.form['name']
        message = request.form['message']
        
        # Save it to the database
        if name and message:
            conn = get_db_connection()
            conn.execute('INSERT INTO feedback (name, message) VALUES (?, ?)', (name, message))
            conn.commit()
            conn.close()
            # Refresh the page to show the new feedback
            return redirect(url_for('index'))
    
    # If it's a GET request (just loading the page), fetch all existing feedback
    conn = get_db_connection()
    feedbacks = conn.execute('SELECT * FROM feedback ORDER BY id DESC').fetchall()
    conn.close()
    
    # Pass the feedback to the HTML template
    return render_template('index.html', feedbacks=feedbacks)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)