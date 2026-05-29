"""
FastAPI server for GitHub Interviewer web app.
Provides REST endpoints for interview generation.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import os
import sys

# Add app directory to path so we can import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

from interview_service import InterviewService

# Initialize FastAPI app
app = FastAPI(
    title="GitHub Interviewer API",
    description="Generate personalized interviews from GitHub profiles",
    version="1.0.0"
)

# Enable CORS for local development and deployment
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Pydantic models for request/response
class InterviewRequest(BaseModel):
    username: str


class InterviewResponse(BaseModel):
    username: str
    interview: str | None = None
    profile: dict | None = None
    status: str
    error: str | None = None


@app.post("/api/analyze", response_model=InterviewResponse)
def analyze_github_user(request: InterviewRequest):
    """
    Analyze a GitHub user and generate a personalized interview.
    
    Args:
        request: Contains the GitHub username
        
    Returns:
        Interview data with generated questions and profile analysis
    """
    result = InterviewService.generate_interview_for_user(request.username)
    return InterviewResponse(**result)


@app.get("/api/health")
def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}


# Serve built frontend files if available
frontend_dist = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "frontend", "dist")
)

if os.path.isdir(frontend_dist):
    app.mount("/", StaticFiles(directory=frontend_dist, html=True), name="frontend")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
