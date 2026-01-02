from dotenv import load_dotenv
load_dotenv()   # 🔑 MUST BE FIRST

from graph import graph
from graph_state import ResearchState

state = ResearchState()

for i in range(state.max_iterations):
    print(f"\n🔁 Iteration {i + 1}")

    # Run one autonomous graph pass
    updates = graph.invoke(state)

    # 🔑 Merge returned dict into ResearchState
    state = ResearchState(**{
        **state.model_dump(),
        **updates
    })

    # Early stop if critic accepts
    if state.critique and state.critique.get("decision") == "accept":
        print("✅ Accepted by Critic Agent")
        break

# Always write paper
with open("outputs/paper.md", "w", encoding="utf-8") as f:
    f.write(state.paper_markdown)

print("\n📄 Paper written to outputs/paper.md")
