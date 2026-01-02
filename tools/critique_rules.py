def apply_critique(experiments):
    reasons = []
    decision = "accept"

    for exp in experiments:
        p = exp.get("p_value", 1.0)

        # Rule 1: Statistical significance
        if p > 0.05:
            decision = "reject"
            reasons.append(
                f"{exp['test']} failed significance test (p={p})"
            )

        # Rule 2: Effect size (for correlation)
        if exp["test"] == "pearson_correlation":
            corr = abs(exp.get("correlation", 0))
            if corr < 0.3:
                decision = "reject"
                reasons.append(
                    f"Correlation effect size too small ({corr})"
                )

    return {
        "decision": decision,
        "reasons": reasons if reasons else ["Results are statistically meaningful"]
    }
