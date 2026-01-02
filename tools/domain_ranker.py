def rank_domains(signals):
    scored = {}

    for item in signals:
        key = item["signal"]

        if key not in scored:
            scored[key] = {
                "domain": key,
                "score": 0,
                "sources": set()
            }

        scored[key]["score"] += 1
        scored[key]["sources"].add(item["source"])

    ranked = list(scored.values())

    # Bonus for appearing in multiple sources
    for r in ranked:
        r["score"] += len(r["sources"])

    ranked.sort(key=lambda x: x["score"], reverse=True)

    return ranked[:5]
