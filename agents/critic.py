from graph_state import ResearchState
from tools.critique_rules import apply_critique

def critic_agent(state: ResearchState) -> dict:
    if not state.experiment_results or "experiments" not in state.experiment_results:
        return {
            "critique": {
                "decision": "reject",
                "reasons": ["No experimental results available"]
            }
        }

    experiments = state.experiment_results["experiments"]

    critique = apply_critique(experiments)

    return {
        "critique": critique
    }
