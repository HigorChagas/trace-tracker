# Trace Tracker

Trace Tracker is an API that analyzes Python error stack traces using AI. Send your error log and get back a clear explanation of what went wrong, the probable cause, and how to fix it.

## Features

- User authentication with JWT
- Error analysis powered by AI (Ollama or any OpenAI-compatible API)
- Analysis history per user
- Python error recognition

## Tech Stack

- **Python** — main language
- **FastAPI** — web framework
- **SQLAlchemy** — ORM
- **SQLite** — database
- **Ollama** — local AI inference
- **JWT** — authentication
- **UV** — package manager

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/HigorChagas/trace-tracker
cd trace-tracker
```

### 2. Install dependencies

```bash
uv sync
```

### 3. Configure environment variables

Create a `.env` file in the root directory:

```env
SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Generate a secure secret key with:

```bash
openssl rand -hex 32
```

### 4. Set up the AI

**Option A — Ollama (local, recommended):**

Install Ollama from [https://ollama.com](https://ollama.com), then pull a model:

```bash
ollama pull qwen2.5-coder:1.5b
```

**Option B — Any OpenAI-compatible API:**

Add your API key to `.env` and update `base_url` in `services/ai.py`.

### 5. Populate the database with known errors

```bash
python seed.py
```

### 6. Run the application

```bash
uv run fastapi dev main.py
```

The API will be available at `http://localhost:8000`.

Interactive docs at `http://localhost:8000/docs`.

## Endpoints

| Method | Endpoint | Description | Auth required |
|--------|----------|-------------|---------------|
| POST | `/register/` | Create a new user | No |
| POST | `/login/` | Login and get JWT token | No |
| POST | `/search-log/` | Analyze an error log | Yes |
| GET | `/history/` | Get user analysis history | Yes |
| DELETE | `/history/{error_id}` | Delete a history entry | Yes |

## Usage Example

**1. Register:**
```json
POST /register/
{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "securepassword"
}
```

**2. Login:**
```json
POST /login/
{
  "email": "john@example.com",
  "password": "securepassword"
}
```

**3. Analyze a log:**
```json
POST /search-log/
Authorization: Bearer <your_token>

{
  "log": "Traceback (most recent call last):\n  File 'main.py', line 4, in <module>\n    result = 10 / 0\nZeroDivisionError: division by zero"
}
```
