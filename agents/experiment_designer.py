from tools.stats import correlation_test

def experiment_designer_agent(state):
    question = state.selected_question["question"].lower()
    results = state.experiment_results

    if not results or not results.get("dataset") is not None:
        return {
            "experiment_analysis": {
                "status": "skipped",
                "reason": "No domain-relevant numeric dataset available"
            }
        }

    df = results["dataset"]

    # If question implies relationship analysis
    if "relationship" in question or "correlat" in question or "impact" in question:
        corr = correlation_test(df)

        if not corr:
            return {
                "experiment_analysis": {
                    "status": "failed",
                    "reason": "Insufficient numeric features for correlation"
                }
            }

        return {
            "experiment_analysis": corr
        }

    # Otherwise: exploratory stats
    return {
        "experiment_analysis": {
            "status": "exploratory",
            "summary_stats": df.describe().to_dict()
        }
    }
