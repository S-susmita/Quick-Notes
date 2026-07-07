# Quick Note Application

A simple single-page application for writing and saving notes. Features a Python Flask backend with SQLite database storage and a clean, responsive frontend.

## Features

- ✍️ Write and save notes instantly
- 📋 View all saved notes in chronological order
- 🗑️ Delete notes you no longer need
- 💾 Persistent storage with SQLite database
- 🎨 Beautiful, responsive UI with gradient design
- ⚡ Real-time updates without page refresh

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

## Installation

1. Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the Flask server:

```bash
python app.py
```

2. Open your web browser and navigate to:

```
http://localhost:5000
```

## Project Structure

```
quick-note-app/
│
├── app.py                 # Flask backend server
├── templates/
│   └── index.html        # Frontend single-page application
├── requirements.txt      # Python dependencies
├── notes.db             # SQLite database (created automatically)
└── README.md            # This file
```

## API Endpoints

### GET /api/notes
Retrieve all notes from the database.

**Response:**
```json
[
  {
    "id": 1,
    "content": "My first note",
    "created_at": "2026-07-07 10:30:00"
  }
]
```

### POST /api/notes
Create a new note.

**Request Body:**
```json
{
  "content": "This is my note"
}
```

**Response:**
```json
{
  "id": 1,
  "content": "This is my note",
  "created_at": "2026-07-07 10:30:00"
}
```

### DELETE /api/notes/<id>
Delete a note by ID.

**Response:**
```json
{
  "message": "Note deleted successfully"
}
```

## How It Works

1. **Frontend (HTML/CSS/JavaScript):**
   - User writes a note in the textarea
   - JavaScript sends a POST request to the backend
   - Notes are fetched and displayed dynamically
   - Delete functionality sends DELETE requests

2. **Backend (Flask/Python):**
   - Receives HTTP requests from the frontend
   - Processes CRUD operations (Create, Read, Delete)
   - Interacts with SQLite database
   - Returns JSON responses

3. **Database (SQLite):**
   - Stores notes persistently in `notes.db`
   - Automatically created on first run
   - Schema includes: id, content, created_at

## Technologies Used

- **Backend:** Python, Flask, SQLite
- **Frontend:** HTML5, CSS3, Vanilla JavaScript
- **Database:** SQLite
- **API:** RESTful JSON API

## Keyboard Shortcuts

- `Ctrl + Enter` (or `Cmd + Enter` on Mac): Save note

## Development Notes

- The database file (`notes.db`) is created automatically when you first run the application
- CORS is enabled for development purposes
- The app runs in debug mode by default
- Notes are stored with timestamps in UTC

## Future Enhancements

- Edit existing notes
- Search and filter notes
- Categories or tags
- Rich text formatting
- User authentication
- Export notes to file

## License

This project is open source and available for educational purposes.
