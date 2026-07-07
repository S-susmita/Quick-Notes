from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from datetime import datetime
import sqlite3
import os

app = Flask(__name__)
CORS(app)

DATABASE = 'notes.db'

def get_db_connection():
    """Create a database connection."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initialize the database with notes table."""
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    """Serve the main page."""
    return render_template('index.html')

@app.route('/api/notes', methods=['GET'])
def get_notes():
    """Retrieve all notes from the database."""
    try:
        conn = get_db_connection()
        notes = conn.execute('SELECT * FROM notes ORDER BY created_at DESC').fetchall()
        conn.close()
        
        return jsonify([{
            'id': note['id'],
            'content': note['content'],
            'created_at': note['created_at']
        } for note in notes])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/notes', methods=['POST'])
def create_note():
    """Create a new note."""
    try:
        data = request.get_json()
        
        if not data or 'content' not in data:
            return jsonify({'error': 'Content is required'}), 400
        
        content = data['content'].strip()
        
        if not content:
            return jsonify({'error': 'Content cannot be empty'}), 400
        
        conn = get_db_connection()
        cursor = conn.execute('INSERT INTO notes (content) VALUES (?)', (content,))
        note_id = cursor.lastrowid
        conn.commit()
        
        # Fetch the created note
        note = conn.execute('SELECT * FROM notes WHERE id = ?', (note_id,)).fetchone()
        conn.close()
        
        return jsonify({
            'id': note['id'],
            'content': note['content'],
            'created_at': note['created_at']
        }), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/notes/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    """Delete a note by ID."""
    try:
        conn = get_db_connection()
        cursor = conn.execute('DELETE FROM notes WHERE id = ?', (note_id,))
        conn.commit()
        conn.close()
        
        if cursor.rowcount == 0:
            return jsonify({'error': 'Note not found'}), 404
        
        return jsonify({'message': 'Note deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)
