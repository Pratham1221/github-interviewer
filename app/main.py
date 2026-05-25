from github_api import *
import json

username = input("Enter GitHub username: ")

user = get_user(username)
repos = get_repos(username)
repo_readme = get_repo_readme(username, repos[0]['name'])

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

print("\nFIRST REPO README JSON:")
print(json.dumps(repo_readme, indent=2))

print("\nDecoded README Content:")
print(decode_github_content(repo_readme['content']))