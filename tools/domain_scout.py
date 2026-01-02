from graph_state import ResearchState
from tools.domain_sources import (
    get_github_trending_domains,
    get_arxiv_recent_domains
)
from tools.domain_ranker import rank_domains

def domain_scout_agent(state: ResearchState) -> dict:
    github_signals = get_github_trending_domains()
    arxiv_signals = get_arxiv_recent_domains()

    all_signals = github_signals + arxiv_signals

    ranked_domains = rank_domains(all_signals)

    # 🚨 SAFETY FALLBACK (CRITICAL)
    if not ranked_domains:
        ranked_domains = [{
            "domain": "emerging interdisciplinary computational science",
            "score": 1,
            "sources": ["fallback"]
        }]

    selected = ranked_domains[0]

    return {
        "domains": ranked_domains,
        "selected_domain": selected
    }
