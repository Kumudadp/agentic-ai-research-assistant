def formulate_hypothesis(question: str):
    return {
        "null": f"There is no statistically significant relationship relevant to: {question}",
        "alternative": f"There exists a statistically significant relationship relevant to: {question}"
    }
