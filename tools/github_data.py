import requests

def fetch_github_repo_stats(keyword: str):
    url = f"https://api.github.com/search/repositories?q={keyword}&sort=stars"
    response = requests.get(url, timeout=15)

    items = response.json().get("items", [])[:10]

    data = []
    for repo in items:
        data.append({
            "name": repo["name"],
            "stars": repo["stargazers_count"],
            "created_at": repo["created_at"][:4]  # year
        })

    return data
