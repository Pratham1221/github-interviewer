from github_api import *
import json
from analyzer import analyze_repos
from prompt_builder import build_interview_prompt
from llm import generate_interview

def save_to_markdown(content, filename="interview.md"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

username = input("Enter GitHub username: ")

# user = get_user(username)
# repos = get_repos(username)
# repo_readme = get_repo_readme(username, repos[0]['name'])

user = get_user(username)
repos = get_repos(username)

profile = analyze_repos(
    user,
    repos,
    get_repo_readme
)

prompt = build_interview_prompt(profile)
response = generate_interview(prompt)
save_to_markdown(response)
print("Interview saved to interview.md")
#print(response)

#print(profile["project_summaries"])

# print("\nUSER INFO")
# print("Name:", user.get("name"))
# print("Bio:", user.get("bio"))
# print("Followers:", user.get("followers"))

# print("\nREPOSITORIES")

# for repo in repos:
#     print("-------------------")
#     print("Name:", repo.get("name"))
#     print("Language:", repo.get("language"))
#     print("Description:", repo.get("description"))

# print("\nUSER JSON:")
# print(json.dumps(user, indent=2))
# print("\nFIRST REPO JSON:")
# print(json.dumps(repos[0], indent=2))

# print("\nFIRST REPO README JSON:")
# print(json.dumps(repo_readme, indent=2))

# print("\nDecoded README Content:")
# print(decode_github_content(repo_readme['content']))

def save_to_markdown(content, filename="interview.md"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)