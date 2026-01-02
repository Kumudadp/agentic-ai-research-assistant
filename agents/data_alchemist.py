import arxiv
import requests
import pandas as pd

def data_alchemist_agent(state):
    domain = state.selected_domain["domain"].lower()
    question = state.selected_question["question"].lower()

    data_sources = []
    dataset = None

    # ---- CASE 1: Generative AI / Agentic Systems ----
    if "agent" in domain or "generative" in domain:
        # GitHub repo metadata (real, domain-relevant)
        url = "https://api.github.com/search/repositories?q=agentic+ai+created:>2024-01-01"
        repos = requests.get(url).json().get("items", [])

        df = pd.DataFrame([{
            "stars": r["stargazers_count"],
            "forks": r["forks_count"],
            "open_issues": r["open_issues_count"]
        } for r in repos])

        
        data_sources.append({
            "source": "GitHub",
            "description": "Agentic AI repositories created after 2024",
            "records": len(repos),
            "query": "agentic ai created:>2024-01-01"
        })

        dataset = df
    # ---- CASE 2: Graph / Network / GNN domains ----
    elif "graph" in domain or "gnn" in domain:
        url = "https://raw.githubusercontent.com/graphdeeplearning/benchmarking-gnns/master/data/ENZYMES.zip"
        # (in real systems, you'd download + parse; here we signal source)
        dataset = None
        data_sources.append("Graph benchmarking datasets (ENZYMES, PROTEINS)")

    # ---- CASE 3: Fallback: ArXiv metadata ----
    else:
        search = arxiv.Search(
            query=question,
            max_results=10
        )

        df = pd.DataFrame([{
            "year": r.published.year,
            "title_length": len(r.title)
        } for r in search.results()])

        dataset = df
        data_sources.append({
            "source": "ArXiv",
            "description": "Metadata from recent ArXiv publications related to the research question",
            "records": len(df),
            "fields": list(df.columns)
        })

    return {
        "data_sources": data_sources,
        "experiment_results": {
            "dataset": dataset
        }
    }
