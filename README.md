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

GitHub API → Data Collection → Analysis Layer → Prompt Builder → LLM → Markdown Output

---

# 🛠 Tech Stack

* Python
* requests (GitHub API communication)
* python-dotenv (environment variable management)
* google-genai (LLM integration)
* Markdown (output formatting)

---

# 📦 Installation

## 1. Clone the repository

```bash
git clone https://github.com/your-username/github-interviewer.git
cd github-interviewer
```

## 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Set up environment variables

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_api_key_here
```

## 5. Run the project

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

# 🚀 Purpose

This project was built to explore:

* Real world API integration
* Data extraction from developer profiles
* Prompt engineering for LLMs
* Building structured AI pipelines
* Turning raw data into meaningful insights

---

# 👨‍💻 Summary

GitHub AI Interviewer transforms raw GitHub activity into an intelligent, personalized interview experience using AI.
