from langgraph.graph import StateGraph, END
from graph_state import ResearchState

from agents.domain_scout import domain_scout_agent
from agents.question_generator import question_generator_agent
from agents.data_alchemist import data_alchemist_agent
from agents.experiment_designer import experiment_designer_agent
from agents.critic import critic_agent
from agents.uncertainty import uncertainty_agent
from tools.paper_writer import generate_paper

def paper_node(state):
    return {"paper_markdown": generate_paper(state)}

builder = StateGraph(ResearchState)

builder.add_node("domain", domain_scout_agent)
builder.add_node("question", question_generator_agent)
builder.add_node("data", data_alchemist_agent)
builder.add_node("experiment", experiment_designer_agent)
builder.add_node("critic", critic_agent)
builder.add_node("uncertainty", uncertainty_agent)
builder.add_node("paper", paper_node)

builder.set_entry_point("domain")

builder.add_edge("domain", "question")
builder.add_edge("question", "data")
builder.add_edge("data", "experiment")
builder.add_edge("experiment", "critic")
builder.add_edge("critic", "uncertainty")
builder.add_edge("uncertainty", "paper")
builder.add_edge("paper", END)

graph = builder.compile()
