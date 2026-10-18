# Flask REST API — Notes App

A RESTful API for a notes application with full CRUD operations, SQLite persistence, and API key authentication.

## Portfolio Description

A RESTful API built with Flask that powers a simple notes application. Supports full CRUD operations with SQLite persistence, input validation, and API key authentication. Includes proper HTTP status codes and error responses. Deployable to a free cloud platform — a solid demonstration of backend web development, REST principles, and Python in a production-like context.

## Features

- Full CRUD: create, read, update, delete notes
- SQLite database via SQLAlchemy
- API key authentication
- Input validation with proper HTTP status codes
- Structured JSON error responses
- Deployable to Railway or Render (free tier)

## Tech Stack

- Python 3
- `Flask`, `Flask-SQLAlchemy`
- `python-dotenv`
- `pytest`

## Project Structure

```
08-flask-notes-api/
├── README.md
├── requirements.txt
├── .env.example
├── app/
│   ├── __init__.py         # Flask app factory
│   ├── models.py           # SQLAlchemy Note model
│   ├── routes.py           # API route handlers
│   ├── auth.py             # API key authentication
│   └── errors.py           # error handlers
├── tests/
│   ├── conftest.py
│   └── test_notes.py
└── run.py                  # app entry point
```

## API Endpoints

| Method | Endpoint         | Description         |
|--------|-----------------|---------------------|
| GET    | /notes          | List all notes      |
| GET    | /notes/`<id>`   | Get a single note   |
| POST   | /notes          | Create a note       |
| PUT    | /notes/`<id>`   | Update a note       |
| DELETE | /notes/`<id>`   | Delete a note       |

## Getting Started

```bash
pip install -r requirements.txt
cp .env.example .env
python run.py
```

## Environment Variables

```
SECRET_KEY=your_secret_key
API_KEY=your_api_key
DATABASE_URL=sqlite:///notes.db
```

## Status

🚧 In progress
