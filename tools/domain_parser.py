import re

def extract_concepts(domain_text: str):
    tokens = re.findall(r"[a-zA-Z]+", domain_text.lower())

    stopwords = {
        "and","for","with","using","based","system",
        "analysis","model","learning","network"
    }

    concepts = [t for t in tokens if t not in stopwords and len(t) > 4]

    return list(set(concepts))[:6]
