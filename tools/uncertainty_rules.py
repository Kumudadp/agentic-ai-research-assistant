def compute_confidence(experiments, data_size):
    """
    Confidence is based on:
    - statistical significance
    - effect size
    - data coverage
    """

    score = 0.0
    reasons = []

    # --- Data coverage ---
    if data_size >= 20:
        score += 0.3
    elif data_size >= 10:
        score += 0.2
        reasons.append("Limited data size")
    else:
        reasons.append("Insufficient data")

    # --- Statistical strength ---
    for exp in experiments:
        p = exp.get("p_value", 1.0)

        if p <= 0.05:
            score += 0.3
        else:
            reasons.append(f"Weak statistical evidence (p={p})")

        if exp["test"] == "pearson_correlation":
            corr = abs(exp.get("correlation", 0))
            if corr >= 0.5:
                score += 0.2
            elif corr >= 0.3:
                score += 0.1
            else:
                reasons.append("Low effect size")

    confidence = min(round(score, 2), 1.0)

    return confidence, reasons
