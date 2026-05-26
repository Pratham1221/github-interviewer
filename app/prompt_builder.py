def build_interview_prompt(profile):

    prompt = f"""
You are a senior software engineering interviewer.

Your task is to generate personalized interview questions
based on the candidate's GitHub profile.

Candidate Information:

Username:
{profile["username"]}

Bio:
{profile["bio"]}

Top Languages:
{", ".join(profile["languages"])}

Top Projects:
"""

    for repo in profile["top_repos"]:

        prompt += f"""

Project Name:
{repo["name"]}

Description:
{repo["description"]}

Primary Language:
{repo["language"]}

Stars:
{repo["stars"]}
"""

    prompt += "\nProject README Insights:\n"

    for summary in profile["project_summaries"]:

        prompt += f"""

Repository:
{summary["repo"]}

README Preview:
{summary["readme_preview"]}
"""

    prompt += """

Generate:

1. Technical interview questions
2. Architecture discussion questions
3. Behavioral questions
4. Follow-up questions based on project decisions

Make the questions personalized and specific.
"""

    return prompt