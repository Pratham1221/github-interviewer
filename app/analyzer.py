from collections import Counter


def analyze_repos(user, repos, get_readme_fn):
    """
    Converts raw GitHub data into a structured developer profile.
    """

    profile = {
        "username": user.get("login"),
        "bio": user.get("bio"),
        "public_repos": user.get("public_repos"),
        "followers": user.get("followers"),
        "languages": [],
        "top_repos": [],
        "project_summaries": []
    }

    # -------------------------
    # Extract languages
    # -------------------------

    languages = []

    for repo in repos:
        if repo.get("language"):
            languages.append(repo["language"])

    language_counts = Counter(languages)

    profile["languages"] = [
        lang for lang, _ in language_counts.most_common(5)
    ]

    # -------------------------
    # Top repositories
    # -------------------------

    sorted_repos = sorted(
        repos,
        key=lambda r: r.get("stargazers_count", 0),
        reverse=True
    )

    top_repos = sorted_repos[:5]

    for repo in top_repos:

        repo_data = {
            "name": repo.get("name"),
            "description": repo.get("description"),
            "language": repo.get("language"),
            "stars": repo.get("stargazers_count")
        }

        profile["top_repos"].append(repo_data)

        # -------------------------
        # README Analysis
        # -------------------------

        try:
            readme = get_readme_fn(
                user.get("login"),
                repo.get("name")
            )

            profile["project_summaries"].append({
                "repo": repo.get("name"),
                "readme_preview": readme
            })

        # except Exception as e:
        #     profile["project_summaries"].append({
        #         "repo": repo.get("name"),
        #         "readme_preview": "README not available"
        #     })
        except Exception as e:
            print(f"README error for {repo.get('name')}: {e}")

    return profile