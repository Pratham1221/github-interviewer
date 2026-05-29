# 📊 GitHub AI Interviewer

GitHub AI Interviewer is an AI-powered tool that analyzes a developer’s GitHub profile and automatically generates a personalized technical interview.

It uses the GitHub API to extract user data such as repositories, languages, and README files, then sends this structured information to a large language model to generate meaningful interview questions tailored to the developer’s experience.

The final output is saved as a structured Markdown report.

---

# 🧠 What It Does

This project takes a GitHub username and performs the following steps:

* Fetches user profile information from GitHub
* Retrieves all public repositories
* Extracts repository metadata (language, stars, description)
* Decodes and reads README files when available
* Builds a structured representation of the developer’s skills and projects
* Sends the data to a language model for analysis
* Generates a personalized technical interview
* Saves the result as a Markdown file

---

# ⚙️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    React Frontend (Vite)                    │
│              (http://localhost:3000)                        │
└─────────────────┬───────────────────────────────────────────┘
                  │ axios calls
                  ↓
┌─────────────────────────────────────────────────────────────┐
│              FastAPI Backend (Uvicorn)                      │
│              (http://localhost:8000)                        │
│  • /api/analyze - Generate interview for username          │
│  • /docs - Interactive API documentation                   │
└────────┬─────────────────┬────────────────────┬─────────────┘
         │                 │                    │
         ↓                 ↓                    ↓
   GitHub API      Prompt Builder         LLM (Gemini)
   Data Extract    + Analysis              Interview Gen
```

---

# 🛠 Tech Stack

## Backend
* **Python** - Core language
* **FastAPI** - Modern async web framework
* **Uvicorn** - ASGI server
* **requests** - GitHub API communication
* **python-dotenv** - Environment variable management
* **google-genai** - LLM integration (Gemini)

## Frontend
* **React 18** - UI framework
* **Vite** - Fast build tool
* **Axios** - HTTP client
* **CSS3** - Styling with animations

## Additional
* **Pydantic** - Data validation
* **Docker** - Containerization

---

# 📦 Installation & Setup

## Quick Start (Web App)

The easiest way to run the web app with both backend and frontend:

### macOS / Linux

```bash
chmod +x start.sh
./start.sh
```

### Windows

```bash
start.bat
```

This will:
- Install Python and Node dependencies
- Start FastAPI backend (http://localhost:8000)
- Start React frontend (http://localhost:3000)

## Manual Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/github-interviewer.git
cd github-interviewer
```

### 2. Set up environment variables

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_api_key_here
```

### 3. Install backend dependencies

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 4. Install frontend dependencies

```bash
cd frontend
npm install
```

### 5. Run the application

In one terminal (backend):
```bash
source venv/bin/activate  # On Windows: venv\Scripts\activate
cd app
python server.py
```

In another terminal (frontend):
```bash
cd frontend
npm run dev
```

Then visit:
- Frontend: http://localhost:3000
- Backend API docs: http://localhost:8000/docs

### CLI Mode (Original)

To use the original CLI mode:

```bash
python app/main.py
```

---

# 📄 Output

After execution, the tool generates a file:

```text
interview.md
```

This file contains a structured AI-generated interview based on the user’s GitHub profile, including:

* Technical questions
* Project-based questions
* Architecture discussions
* Behavioral insights

---

# 🔧 Notes

* GitHub API rate limits may apply for unauthenticated requests
* Some repositories may not include README files
* Forked or empty repositories may return limited data
* Ensure your API key is valid and stored securely in `.env`

---

# 🌐 Deployment

## Docker

Build and run with Docker:

```bash
docker build -t github-interviewer .
docker run -p 8000:8000 -e GEMINI_API_KEY=your_key github-interviewer
```

## Cloud Deployment

### Backend (FastAPI)
- **Railway**: `railway up` 
- **Render**: Connect GitHub repo, set start command to `cd app && python server.py`
- **Fly.io**: Use provided Dockerfile

### Frontend (React)
- **Vercel**: `vercel` (auto-detected)
- **Netlify**: `npm run build`, deploy `dist/` folder

---

This project was built to explore:

* Real world API integration
* Data extraction from developer profiles
* Prompt engineering for LLMs
* Building structured AI pipelines
* Turning raw data into meaningful insights

---

# 👨‍💻 Summary

GitHub AI Interviewer transforms raw GitHub activity into an intelligent, personalized interview experience using AI.
