import requests
from bs4 import BeautifulSoup
import arxiv
from datetime import datetime

# ---------- GitHub Trending ----------
def get_github_trending_domains():
    url = "https://github.com/trending?since=monthly"
    html = requests.get(url, timeout=15).text
    soup = BeautifulSoup(html, "html.parser")

    repos = soup.select("article h2 a")
    domains = []

    for repo in repos[:15]:
        name = repo.text.strip().replace("\n", "").lower()

        keywords = [
            "quantum", "graph", "biomedical", "genomics",
            "drug", "neural", "climate", "robot", "vision"
        ]

        if any(k in name for k in keywords):
            domains.append({
                "source": "github",
                "signal": name,
                "timestamp": datetime.utcnow().isoformat()
            })

    return domains


# ---------- ArXiv Recent ----------
def get_arxiv_recent_domains():
    search = arxiv.Search(
        query="",
        max_results=20,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )

    domains = []
    for result in search.results():
        year = result.published.year
        if year >= 2024:
            domains.append({
                "source": "arxiv",
                "signal": result.title.lower(),
                "timestamp": result.published.isoformat()
            })

    return domains
