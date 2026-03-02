# HRMS Lite

A lightweight Human Resource Management System built to meet the assignment requirements.

## Tech Stack
- **Frontend:** Nuxt 3, Vue 3, Nuxt UI, TailwindCSS
- **Backend:** FastAPI (Python), SQLAlchemy (Async), SQLite (aiosqlite)
- **Tooling:** pnpm, Uvicorn

## Core Features
- **Employee Management:** Add new employees, view a list of all employees, and delete employee records.
- **Attendance Management:** Mark daily attendance (Present/Absent) and view attendance history.

## Steps to run the project locally

### Backend
1. Navigate to the `backend` directory:
   ```bash
   cd backend
   ```
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```
   The backend API will run at `http://localhost:8000`.

### Frontend
1. Open a new terminal and navigate to the `frontend` directory:
   ```bash
   cd frontend
   ```
2. Install dependencies using pnpm:
   ```bash
   pnpm install
   ```
3. Start the Nuxt development server:
   ```bash
   pnpm dev
   ```
   The frontend application will be available at `http://localhost:3000`.

## Assumptions or limitations
- **Database:** Used SQLite (with async driver `aiosqlite`) to keep the setup minimal and self-contained without needing a separate database service running, fulfilling the requirement for persistence.
- **Authentication:** Per constraints, assumed a single admin user, so no login or authentication layers were implemented.
- **Base URLs:** The frontend expects the backend to be running precisely at `http://localhost:8000`. This is hardcoded for the assignment's simplicity but would typically be configured via environment variables in a production setup.