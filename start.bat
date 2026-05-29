@echo off
REM Start script for GitHub Interviewer web app (Windows)
REM Runs both backend (FastAPI) and frontend (Vite) in separate windows

echo.
echo 🚀 Starting GitHub Interviewer Web App...
echo.

REM Check if Python virtual environment exists
if not exist "venv" (
    echo 📦 Installing Python dependencies...
    python -m venv venv
    call venv\Scripts\activate.bat
    pip install -r requirements.txt
) else (
    call venv\Scripts\activate.bat
)

REM Check if Node dependencies are installed
if not exist "frontend\node_modules" (
    echo 📦 Installing Node dependencies...
    cd frontend
    call npm install
    cd ..
)

echo.
echo ✨ Starting services in separate windows...
echo   Backend: http://localhost:8000 (API docs: http://localhost:8000/docs)
echo   Frontend: http://localhost:3000
echo.

REM Start backend in a new window
cd app
start "GitHub Interviewer Backend" python server.py
cd ..

REM Start frontend in a new window
cd frontend
start "GitHub Interviewer Frontend" cmd /k npm run dev
cd ..

echo.
echo 👍 Services are starting. Check the new windows for output.
