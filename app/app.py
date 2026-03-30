from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import database

app = Flask(__name__)

# Initialize the database when the app starts
database.init_db()

def get_db_connection():
    conn = sqlite3.connect('feedback.db')
    conn.row_factory = sqlite3.Row
    return conn

# Route for the main page where users submit feedback
@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        
        # Save to database
        conn = get_db_connection()
        conn.execute('INSERT INTO feedback (name, message) VALUES (?, ?)', (name, message))
        conn.commit()
        conn.close()
        return redirect(url_for('feedback')) # Redirect to see the feedback
    
    return render_template('index.html')

# Route to display all submitted feedback
@app.route('/feedback')
def feedback():
    conn = get_db_connection()
    # Fetch all feedback entries
    feedbacks = conn.execute('SELECT * FROM feedback ORDER BY id DESC').fetchall()
    conn.close()
    return render_template('feedback.html', feedbacks=feedbacks)

if __name__ == '__main__':
    # Run the app on port 5000
    app.run(host='0.0.0.0', port=5000)