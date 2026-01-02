from graph_state import ResearchState
from tools.uncertainty_rules import compute_confidence

def uncertainty_agent(state: ResearchState) -> dict:
    if not state.experiment_results or "experiments" not in state.experiment_results:
        return {
            "confidence_score": 0.0,
            "uncertainty_notes": ["Insufficient data for confidence estimation"],
            "abstain": True
        }

    experiments = state.experiment_results["experiments"]
    data_size = len(state.experiment_results["dataset"])

    confidence, reasons = compute_confidence(experiments, data_size)

    abstain = confidence < 0.6

    return {
        "confidence_score": confidence,
        "uncertainty_notes": reasons,
        "abstain": abstain
    }
