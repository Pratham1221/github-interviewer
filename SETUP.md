# 🚀 Setup Guide - GitHub Interviewer Web App

This guide covers all setup methods for running the GitHub Interviewer as a web application.

## Prerequisites

- **Python 3.8+** (Backend)
- **Node.js 16+** (Frontend)
- **Git**
- **GEMINI_API_KEY** (Get from [Google AI Studio](https://aistudio.google.com))

---

## 🎯 Method 1: Quickest Start (Recommended)

### macOS / Linux
```bash
chmod +x start.sh
./start.sh
```

### Windows
```bash
start.bat
```

This automatically:
✅ Creates virtual environment
✅ Installs all dependencies
✅ Starts backend on http://localhost:8000
✅ Starts frontend on http://localhost:3000

---

## 🛠 Method 2: Manual Setup

### Step 1: Clone and enter directory
```bash
git clone https://github.com/your-username/github-interviewer.git
cd github-interviewer
```

### Step 2: Create `.env` file
```
GEMINI_API_KEY=sk-proj-xxxxx
```

### Step 3: Set up backend

```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt

cd app
python server.py
```

### Step 4: Set up frontend (new terminal)
```bash
cd frontend
npm install
npm run dev
```

---

## 🐳 Method 3: Docker

### Single command:
```bash
docker run -p 8000:8000 -e GEMINI_API_KEY=your_key github-interviewer
```

### Or with Docker Compose:
```bash
docker-compose up
```

---

## 📍 Access Points

| Component | URL | Purpose |
|-----------|-----|---------|
| Frontend | http://localhost:3000 | Web interface |
| Backend API | http://localhost:8000 | REST API |
| API Docs | http://localhost:8000/docs | Interactive Swagger UI |

---

## 🔧 API Endpoint

### POST `/api/analyze`

Send a GitHub username to generate an interview.

**Request:**
```json
{
  "username": "torvalds"
}
```

**Response:**
```json
{
  "username": "torvalds",
  "status": "success",
  "interview": "...",
  "profile": {
    "username": "torvalds",
    "bio": "...",
    "languages": ["C", "..."],
    "top_repos": [...],
    "project_summaries": [...]
  }
}
```

---

## 🧪 Test the Setup

```bash
# Test backend
curl http://localhost:8000/

# Test API
curl -X POST http://localhost:8000/api/analyze \
  -H "Content-Type: application/json" \
  -d '{"username": "gvanrossum"}'
```

---

## 📂 Project Structure

```
github-interviewer/
├── app/
│   ├── server.py              # FastAPI server
│   ├── interview_service.py   # Core business logic
│   ├── main.py                # CLI mode
│   ├── github_api.py
│   ├── analyzer.py
│   ├── llm.py
│   └── prompt_builder.py
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── components/
│   │   └── styles/
│   ├── package.json
│   ├── vite.config.js
│   └── Dockerfile
├── start.sh                   # macOS/Linux starter
├── start.bat                  # Windows starter
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## 🚨 Troubleshooting

### "Port 8000 already in use"
```bash
# Find and kill process on port 8000
lsof -i :8000
kill -9 <PID>

# Or use a different port by editing app/server.py
```

### "GEMINI_API_KEY not found"
- Create `.env` file in root directory
- Add `GEMINI_API_KEY=your_key`
- Restart the server

### Frontend can't reach backend
- Ensure backend is running on http://localhost:8000
- Check CORS settings in `app/server.py`
- Check browser console for errors

### Dependencies not installing
```bash
# Clear cache and reinstall
rm -rf venv node_modules
python3 -m venv venv
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 🌐 Production Deployment

### Backend (Railway, Render, Fly.io)
1. Set `GEMINI_API_KEY` environment variable
2. Deploy with command: `cd app && python server.py`
3. Expose port 8000

### Frontend (Vercel, Netlify)
1. Connect GitHub repository
2. Set build command: `cd frontend && npm run build`
3. Set output directory: `frontend/dist`
4. Set API URL environment variable

---

## 📚 More Info

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React Documentation](https://react.dev/)
- [Vite Documentation](https://vitejs.dev/)
- [Google Gemini API](https://ai.google.dev/)

---

**Ready to go?** Start with Method 1! 🎉
