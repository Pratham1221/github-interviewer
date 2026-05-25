import requests
import base64

BASE_URL = "https://api.github.com"


def get_user(username):
    url = f"{BASE_URL}/users/{username}"

    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Error fetching user: {response.status_code}")

    return response.json()


def get_repos(username):
    url = f"{BASE_URL}/users/{username}/repos"

    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Error fetching repos: {response.status_code}")

    return response.json()

def get_repo_readme(username, repo_name):
    url = f"{BASE_URL}/repos/{username}/{repo_name}/readme"

    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Error fetching README: {response.status_code}")

    encoded_content = response.json()["content"]
    decoded_bytes = base64.b64decode(encoded_content)
    return decoded_bytes.decode("utf-8")
