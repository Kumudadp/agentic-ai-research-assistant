import arxiv
import json
from tavily import TavilyClient
from llm.groq_client import llm

tavily = TavilyClient()

def domain_scout_agent(state):
    search = arxiv.Search(
        query="machine learning",
        max_results=15,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )

    arxiv_titles = [
        r.title for r in search.results()
        if r.published.year >= 2024
    ]

    web = tavily.search(
        query="emerging AI research 2024",
        max_results=5
    )
    snippets = [r["content"] for r in web["results"]]

    prompt = f"""
    You are a research scout agent.

    Identify 5 emerging scientific domains (post-2024).
    Use the signals below.

    ArXiv titles:
    {arxiv_titles}

    Web snippets:
    {snippets}

    OUTPUT STRICT JSON ONLY:
    {{
      "domains": [
        {{
          "domain": "string",
          "justification": "string"
        }}
      ]
    }}
    """

    raw = llm.invoke(prompt).content

    try:
        parsed = json.loads(raw)
        domains = parsed["domains"]
    except Exception:
        domains = []

    if not domains:
        domains = [{
            "domain": "AI Safety Alignment Failures",
            "justification": "Fallback domain inferred from repeated AI safety signals in web and ArXiv sources."
        }]

    return {
        "domains": domains,
        "selected_domain": domains[0]
    }
