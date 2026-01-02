def uncertainty_agent(state):
    confidence = 0.0
    notes = []

    # ---- Experiment-based confidence ----
    exp = state.experiment_results
    if exp and isinstance(exp, dict):
        p_value = exp.get("p_value")
        corr = exp.get("correlation")

        if p_value is not None:
            if p_value < 0.05:
                confidence += 0.4
                notes.append("Statistically significant result (p < 0.05).")
            else:
                notes.append("Result not statistically significant.")

        if corr is not None:
            if abs(corr) > 0.3:
                confidence += 0.3
                notes.append("Moderate to strong effect size.")
            else:
                notes.append("Weak effect size.")

    # ---- Critic decision ----
    critique = state.critique
    if critique and critique.get("decision") == "accept":
        confidence += 0.2
        notes.append("Critic agent accepted methodology.")

    # ---- Data volume ----
    data_sources = state.data_sources or []
    for src in data_sources:
        records = src.get("records")
        if isinstance(records, int) and records >= 20:
            confidence += 0.1
            notes.append("Sufficient data volume.")
            break

    # ---- Clamp ----
    confidence = min(confidence, 1.0)

    abstain = confidence < 0.6

    return {
        "confidence_score": round(confidence, 2),
        "uncertainty_notes": notes,
        "abstain": abstain
    }
