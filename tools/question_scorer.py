def score_question(question: str, concepts: list):
    novelty = 0.5
    feasibility = 0.5

    # More concept intersections → more novel
    for c in concepts:
        if c in question.lower():
            novelty += 0.1

    # Penalize overly broad questions
    if "everything" in question or "all" in question:
        feasibility -= 0.2

    return {
        "novelty": round(min(novelty, 1.0), 2),
        "feasibility": round(min(feasibility, 1.0), 2)
    }
