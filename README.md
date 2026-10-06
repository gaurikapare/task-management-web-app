````markdown
# Mini Task Management Web App

A full-stack Task Management application built with **React, FastAPI, SQLAlchemy, and PostgreSQL**.

The application allows users to create, view, update, delete, search, and filter tasks based on status and priority.

## 🚀 Live Demo

**Frontend:**  
https://task-management-web-app-blkj.vercel.app

**Backend API:**  
https://task-management-web-app-wine.vercel.app

**API Documentation (Swagger):**  
https://task-management-web-app-wine.vercel.app/docs

---

## 📌 Features

- Create new tasks
- View all tasks
- View individual task details
- Update existing tasks
- Delete tasks
- Search tasks by title/description
- Filter tasks by status
- Filter tasks by priority
- Task status management
- Task priority management
- RESTful API architecture
- PostgreSQL database integration
- Interactive Swagger API documentation
- Responsive and clean user interface
- Production deployment using Vercel

---

## 🛠️ Tech Stack

### Frontend
- React.js
- Vite
- JavaScript
- CSS

### Backend
- Python
- FastAPI
- SQLAlchemy
- Pydantic
- Uvicorn

### Database
- PostgreSQL
- PostgreSQL-compatible SQLAlchemy configuration

### Deployment
- Vercel
- GitHub

### Development Tools
- VS Code
- Git
- GitHub
- Swagger / OpenAPI

---

## 🏗️ Project Architecture

```text
                   ┌─────────────────────────┐
                   │       User / Browser    │
                   └────────────┬────────────┘
                                │
                                ▼
                   ┌─────────────────────────┐
                   │     React Frontend      │
                   │       (Vite)            │
                   └────────────┬────────────┘
                                │
                         REST API Requests
                                │
                                ▼
                   ┌─────────────────────────┐
                   │      FastAPI Backend    │
                   │       (Python)          │
                   └────────────┬────────────┘
                                │
                         SQLAlchemy ORM
                                │
                                ▼
                   ┌─────────────────────────┐
                   │      PostgreSQL DB      │
                   └─────────────────────────┘
````

---

## 📂 Project Structure

```text
task-management-web-app/
│
├── backend/
│   │
│   ├── app/
│   │   ├── routes/
│   │   │   └── tasks.py
│   │   │
│   │   ├── services/
│   │   │
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── database.py
│   │   ├── main.py
│   │   ├── models.py
│   │   └── schemas.py
│   │
│   ├── tests/
│   │
│   ├── requirements.txt
│   ├── .env.example
│   └── tasks.db
│
├── frontend/
│   │
│   ├── src/
│   │   ├── components/
│   │   │   ├── TaskCard.jsx
│   │   │   └── TaskForm.jsx
│   │   │
│   │   ├── App.jsx
│   │   └── ...
│   │
│   ├── package.json
│   └── ...
│
├── .gitignore
├── README.md
└── ...
```

---

## 🔌 API Endpoints

The backend provides the following REST APIs:

| Method | Endpoint               | Description         |
| ------ | ---------------------- | ------------------- |
| GET    | `/health`              | Health check        |
| GET    | `/api/tasks`           | Get all tasks       |
| POST   | `/api/tasks`           | Create a new task   |
| GET    | `/api/tasks/{task_id}` | Get a specific task |
| PUT    | `/api/tasks/{task_id}` | Update a task       |
| DELETE | `/api/tasks/{task_id}` | Delete a task       |

---

## 📖 API Documentation

The backend provides interactive Swagger documentation using FastAPI.

Open:

```text
https://task-management-web-app-wine.vercel.app/docs
```

From Swagger UI, the API endpoints can be tested directly.

---

## 🗃️ Task Model

Each task contains information such as:

```text
Task
├── ID
├── Title
├── Description
├── Status
├── Priority
└── Created / Updated information
```

### Status

Tasks can have different statuses such as:

* Pending
* In Progress
* Completed

### Priority

Tasks can have different priority levels:

* Low
* Medium
* High

---

## 🔍 Search and Filtering

The frontend provides:

### Search

Users can search tasks using keywords.

### Status Filter

Tasks can be filtered according to their current status.

### Priority Filter

Tasks can be filtered according to their priority.

These features make it easier to manage a larger number of tasks.

---

## 💻 Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/gaurikapare/task-management-web-app.git
```

```bash
cd task-management-web-app
```

---

# Backend Setup

### 2. Create a virtual environment

```bash
cd backend
```

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file inside the `backend` directory.

Example:

```env
DATABASE_URL=your_postgresql_database_url
```

Do not commit your real database credentials to GitHub.

### 5. Start the backend

```bash
uvicorn app.main:app --reload
```

Backend will run at:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

---

# Frontend Setup

### 6. Open a new terminal

From the project root:

```bash
cd frontend
```

### 7. Install dependencies

```bash
npm install
```

### 8. Start the frontend

```bash
npm run dev
```

The frontend will normally run at:

```text
http://localhost:5173
```

---

## 🌐 Environment Configuration

For production, the frontend communicates with the deployed FastAPI backend.

Example:

```env
VITE_API_URL=https://task-management-web-app-wine.vercel.app
```

Make sure environment variables are configured correctly for the deployment environment.

---

## 🚀 Deployment

The application is deployed using **Vercel**.

### Backend

The FastAPI backend is deployed separately from the `backend` directory.

Production backend:

```text
https://task-management-web-app-wine.vercel.app
```

### Frontend

The React frontend is deployed separately from the `frontend` directory.

Production frontend:

```text
https://task-management-web-app-blkj.vercel.app
```

Both applications are connected through REST APIs.

---

## 🔐 CORS Configuration

The FastAPI backend is configured to allow requests from the deployed frontend.

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

This allows the React frontend to communicate with the FastAPI backend in production.

---

## 🧪 Testing

The API can be tested using:

* Swagger UI
* Browser
* Frontend application
* REST API clients such as Postman

Example health check:

```http
GET /health
```

Expected response:

```json
{
  "status": "ok"
}
```

---

## 📸 Application

The application provides a dashboard where users can:

* View tasks
* Search tasks
* Filter tasks
* Create tasks
* Edit tasks
* Delete tasks
* Change status
* Change priority

---

## 🎯 Project Objective

The objective of this project is to build a simple but production-ready full-stack task management system demonstrating:

* REST API development
* Backend architecture
* Database integration
* Frontend and backend communication
* CRUD operations
* API documentation
* CORS configuration
* Cloud deployment
* Git/GitHub workflow

---

## 👩‍💻 Author

**Gauri Kapare**

B.Tech – Information Technology and Data Science


---
