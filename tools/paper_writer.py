from llm.groq_client import llm


def format_data_sources(data_sources):
    if not data_sources:
        return "No external data sources were successfully integrated."

    lines = []
    for src in data_sources:
        source = src.get("source", "Unknown source")
        description = src.get("description", "")
        records = src.get("records", "N/A")
        fields = src.get("fields", [])

        line = f"- **{source}**"
        if description:
            line += f": {description}"
        if records != "N/A":
            line += f" (records analyzed: {records})"
        if fields:
            line += f"; fields: {', '.join(fields)}"

        lines.append(line)

    return "\n".join(lines)


def generate_paper(state):
    # -------- SAFE EXTRACTION FROM STATE --------
    domain = state.selected_domain["domain"]
    question = state.selected_question["question"]
    data_sources = state.data_sources or []
    experiment_analysis = state.experiment_results
    critique = state.critique
    confidence = state.confidence_score
    abstain = state.abstain

    # -------- DATA SECTIONS --------
    data_section = format_data_sources(data_sources)

    experiment_section = (
        str(experiment_analysis)
        if experiment_analysis
        else "No statistically valid experiments were completed."
    )

    critique_section = (
        f"Decision: **{critique['decision'].upper()}**\n\n" +
        "\n".join([f"- {r}" for r in critique["reasons"]])
    )

    uncertainty_section = f"Confidence Score: **{confidence}**"

    # -------- USE LLM AS SCIENTIFIC WRITER --------
    writing_prompt = f"""
You are an academic research writer.

Write a concise but serious mini research paper using ONLY the information below.
Do NOT invent data or claims.

DOMAIN:
{domain}

RESEARCH QUESTION:
{question}

DATA SOURCES:
{data_section}

EXPERIMENT RESULTS:
{experiment_section}

CRITIC FEEDBACK:
{critique_section}

CONFIDENCE SCORE:
{confidence}

ABSTAIN:
{abstain}

Write the following sections:
- Title
- Abstract
- Introduction
- Methodology
- Results
- Limitations & Future Work
- Conclusion

Use formal academic tone.
"""

    paper_text = llm.invoke(writing_prompt).content

    return paper_text.strip()
