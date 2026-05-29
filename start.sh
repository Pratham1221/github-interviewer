#!/bin/bash
# Start script for GitHub Interviewer web app
# Runs both backend (FastAPI) and frontend (Vite) concurrently

set -e

echo "🚀 Starting GitHub Interviewer Web App..."
echo ""

# Check if Python dependencies are installed
if [ ! -d "venv" ]; then
    echo "📦 Installing Python dependencies..."
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
else
    source venv/bin/activate
fi

# Check if Node dependencies are installed
if [ ! -d "frontend/node_modules" ]; then
    echo "📦 Installing Node dependencies..."
    cd frontend
    npm install
    cd ..
fi

echo ""
echo "✨ Starting services..."
echo "  Backend: http://localhost:8000 (API docs: http://localhost:8000/docs)"
echo "  Frontend: http://localhost:3000"
echo ""
echo "Press Ctrl+C to stop both services."
echo ""

# Start backend in background
echo "Starting FastAPI backend..."
cd app
python server.py &
BACKEND_PID=$!
cd ..

# Start frontend
echo "Starting Vite frontend..."
cd frontend
npm run dev

# Cleanup on exit
trap "kill $BACKEND_PID" EXIT
