import json
from llm.groq_client import llm

def question_generator_agent(state):
    domain = state.selected_domain["domain"]

    # ---------- STEP 1: DOMAIN GROUNDING ----------
    grounding_prompt = f"""
You are a domain expert.

TASK:
Given the scientific domain:
"{domain}"

1. List the core concepts
2. Typical research methods
3. Common evaluation metrics

OUTPUT STRICT JSON ONLY:

{{
  "concepts": ["string"],
  "methods": ["string"],
  "metrics": ["string"]
}}
"""

    grounding_raw = llm.invoke(grounding_prompt).content

    try:
        grounding = json.loads(grounding_raw)
    except Exception:
        # Self-repair fallback
        grounding = {
            "concepts": ["agent coordination", "emergent behavior"],
            "methods": ["simulation-based analysis"],
            "metrics": ["robustness", "scalability"]
        }

    concepts = grounding["concepts"]
    methods = grounding["methods"]
    metrics = grounding["metrics"]

    # ---------- STEP 2: QUESTION SYNTHESIS ----------
    question_prompt = f"""
You are a research ideation agent.

DOMAIN:
{domain}

You MUST:
- Use ONLY these concepts: {concepts}
- Use ONLY these methods: {methods}
- Use ONLY these metrics: {metrics}
- Do NOT introduce concepts from other domains

Generate 5 original, non-trivial research questions
that are experimentally testable within this domain.

OUTPUT STRICT JSON ONLY:

{{
  "questions": [
    {{
      "question": "string",
      "novelty": 0.0,
      "feasibility": 0.0
    }}
  ]
}}
"""

    raw = llm.invoke(question_prompt).content

    try:
        parsed = json.loads(raw)
        questions = parsed["questions"]
    except Exception:
        questions = []

    # ---------- SELF-REPAIR ----------
    if not questions:
        questions = [{
            "question": f"How do coordination constraints among autonomous agents affect emergent robustness in {domain}?",
            "novelty": 0.65,
            "feasibility": 0.6
        }]

    # Rank questions
    questions.sort(
        key=lambda q: q["novelty"] * q["feasibility"],
        reverse=True
    )

    return {
        "domain_grounding": grounding,
        "research_questions": questions,
        "selected_question": questions[0]
    }
