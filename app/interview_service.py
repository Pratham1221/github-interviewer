"""
Core service for analyzing GitHub profiles and generating interviews.
This module provides a clean API for the web backend.
"""

from github_api import get_user, get_repos, get_repo_readme
from analyzer import analyze_repos
from prompt_builder import build_interview_prompt
from llm import generate_interview


class InterviewService:
    """Service for generating GitHub-based interviews."""
    
    @staticmethod
    def generate_interview_for_user(username: str) -> dict:
        """
        Main method: takes a GitHub username and returns interview data.
        
        Args:
            username: GitHub username to analyze
            
        Returns:
            dict with keys:
                - username: GitHub username
                - interview: Generated interview text
                - profile: Developer profile data
                - error: Error message if failed (optional)
        """
        try:
            # Fetch GitHub data
            user = get_user(username)
            repos = get_repos(username)
            
            # Analyze and build profile
            profile = analyze_repos(user, repos, get_repo_readme)
            
            # Generate interview using LLM
            prompt = build_interview_prompt(profile)
            interview = generate_interview(prompt)
            
            return {
                "username": username,
                "interview": interview,
                "profile": profile,
                "status": "success"
            }
            
        except Exception as e:
            return {
                "username": username,
                "status": "error",
                "error": str(e)
            }
