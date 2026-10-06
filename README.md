# Mini Task Management Application

## Overview
This project is a small full-stack task management application built with a React frontend, a FastAPI backend, and a PostgreSQL-compatible SQLAlchemy database layer. It is designed to be practical, readable, and easy to explain in an interview while still covering the core CRUD workflow, validation, filtering, and production-ready environment configuration.

## Features
- Create tasks
- View all tasks
- View a single task
- Update task details
- Delete tasks
- Change task status: Pending, In Progress, Completed
- Filter by status and priority
- Search by title and description
- Frontend validation and friendly error messages
- Responsive layout for desktop and mobile
- Clean API error handling

## Tech Stack
- Frontend: React + Vite + JavaScript
- Backend: FastAPI + Python
- Database: PostgreSQL (with SQLAlchemy)
- Validation: Pydantic
- API: REST with JSON responses

## Architecture
The application follows a simple three-layer structure:

Frontend (React) -> REST API (FastAPI) -> PostgreSQL Database

## Project Structure
```text
Task1/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── database.py
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   └── tasks.py
│   │   └── services/
│   │       ├── __init__.py
│   │       └── task_service.py
│   ├── database/
│   │   └── __init__.py
│   ├── tests/
│   │   └── test_tasks_api.py
│   ├── .env
│   ├── .env.example
│   └── requirements.txt
├── frontend/
│   ├── src/
│   ├── .env
│   ├── .env.example
│   ├── package.json
│   └── vite.config.*
├── .env.example
├── .gitignore
├── README.md
└── package-lock.json
```

## Database Schema
The task table includes:

- id: integer primary key, auto-incremented
- title: string, required, max length 150
- description: text, optional
- status: string, required, values are PENDING, IN_PROGRESS, COMPLETED
- priority: string, required, values are LOW, MEDIUM, HIGH
- created_at: timestamp, automatically set
- updated_at: timestamp, automatically updated

## API Endpoints
Base path: `/api/tasks`

- `POST /api/tasks` - Create a task
- `GET /api/tasks` - Return all tasks with optional query filters
- `GET /api/tasks/{id}` - Return one task
- `PUT /api/tasks/{id}` - Update a task
- `DELETE /api/tasks/{id}` - Delete a task

Optional query parameters:
- `search=react`
- `status=PENDING`
- `priority=HIGH`

Example combinations:
- `GET /api/tasks?search=assignment`
- `GET /api/tasks?status=COMPLETED&priority=HIGH`

## Local Setup
### 1. Clone the project and open the folder
```bash
cd Task1
```

### 2. Backend setup
```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Frontend setup
```bash
cd frontend
npm install
```

### 4. Database setup
For local development, create a PostgreSQL database and assign the connection string in `.env`.

Example PostgreSQL connection string:
```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/task_manager
```

For quick local testing, the project also supports a SQLite fallback when `DATABASE_URL` is not configured. The included `.env` file uses SQLite so the app can run immediately without a database server.

## Environment Variables
### Backend
Create a `.env` file in `backend/`:
```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/task_manager
CORS_ORIGINS=http://localhost:5173,http://127.0.0.1:5173
```

### Frontend
Create a `.env` file in `frontend/`:
```env
VITE_API_URL=http://localhost:8000
```

## How to Run Frontend
```bash
cd frontend
npm run dev -- --host 127.0.0.1 --port 5173
```

Open: `http://127.0.0.1:5173/`

## How to Run Backend
```bash
cd backend
.venv\Scripts\activate
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

## How to Run Database
For PostgreSQL production use:
```bash
createdb task_manager
```

Then update the `DATABASE_URL` environment variable to match your local or hosted PostgreSQL instance.

## Testing
Run backend tests:
```bash
cd backend
.venv\Scripts\activate
python -m pytest -q
```

The test suite covers:
- task creation
- reading tasks
- update flow
- delete flow
- search and filter behavior
- invalid task IDs
- empty title validation
- invalid status validation
- invalid priority validation

## Deployment
### Frontend
Use Vercel or a similar host.

Set environment variable:
```env
VITE_API_URL=https://your-backend-url.example.com
```

### Backend
Use Render or any compatible Python hosting service.

Set environment variable:
```env
DATABASE_URL=postgresql://user:password@host:5432/dbname
CORS_ORIGINS=https://your-frontend-url.example.com
```

### Database
Use a managed PostgreSQL instance such as Neon, Supabase, or Render Postgres.

## Screenshots
Add screenshots here after you start the app locally.

Example placeholder:
- Dashboard view
- Task add/edit form
- Mobile responsive layout

## Future Improvements
- Add task sorting by due date or priority
- Add user authentication
- Add pagination for large task lists
- Add dark mode
- Add task comments or notes
- Add automated UI tests

## Interview Notes
This project is intentionally simple and practical:
- React handles the UI and state transitions.
- FastAPI exposes a clean REST endpoint layer.
- SQLAlchemy maps Python models to database tables.
- Pydantic protects the API from invalid input.
- Environment variables keep production configuration separate from code.
- The structure stays small enough to explain clearly in a technical conversation.
