🧠 Autonomous Agentic AI Research Assistant

A fully autonomous, multi-agent AI research system that discovers emerging scientific domains, formulates original research questions, gathers real public data, performs experiments, critiques its own results, quantifies uncertainty, and produces a structured mini research paper — with zero human input after startup.

This project was developed as part of an Agentic AI Research Challenge, emphasizing true agency, multi-agent collaboration, self-criticism, and responsible uncertainty handling.

🚀 Key Capabilities

🔍 Autonomous Domain Discovery (post-2024 emerging domains)

❓ Original Research Question Generation

🌐 Real Data Acquisition from Public Sources

🧪 Lightweight but Real Experimental Analysis

🧨 Self-Critique & Iterative Reasoning

🎯 Confidence & Uncertainty Quantification

📝 Automated Mini Research Paper Generation

📊 Interactive Visualizations

📦 Dockerized & Cloud Deployable

🧩 System Architecture (High Level)

The system is orchestrated using LangGraph, enabling explicit agent collaboration via a shared state.

Core Agents:

Domain Scout Agent – Discovers emerging research domains using real-time web signals

Question Generator Agent – Produces novel, non-trivial research questions

Data Alchemist Agent – Collects and cleans real public datasets (ArXiv + web signals)

Experiment Designer Agent – Performs exploratory and statistical experiments

Critic Agent – Attacks assumptions, methodology, and evidence

Uncertainty Agent – Computes confidence score and abstains when needed

Paper Writer Agent – Generates a structured research paper using verified evidence only

🛠️ Tech Stack
Core Frameworks

Python 3.10+

LangGraph – Multi-agent orchestration

Streamlit – Interactive UI & live demo

Pydantic – Typed state management

AI & Data

Groq (Llama-3.1-8B) – LLM backbone (free tier)

ArXiv API – Public academic data

Web Signals – Trend discovery

Data & Visualization

Pandas – Data processing

Plotly – Interactive charts

Deployment

Docker

Railway (Free Tier)

🧠 Design Principles

❌ No hardcoded domains or datasets

❌ No single-agent or RAG-only pipelines

❌ No fabricated results

✅ Evidence-driven reasoning

✅ Explicit agent responsibilities

✅ Confidence-aware conclusions

📂 Project Structure
agentic-ai-research-assistant/
│
├── app.py                     # Streamlit UI entry point
├── graph.py                   # LangGraph orchestration
├── graph_state.py             # Shared research state
│
├── agents/
│   ├── domain_scout.py
│   ├── question_generator.py
│   ├── data_alchemist.py
│   ├── experiment_designer.py
│   ├── critic.py
│   └── confidence_agent.py
│
├── tools/
│   ├── stats.py
│   └── paper_writer.py
│
├── llm/
│   └── groq_client.py
│
├── requirements.txt
├── Dockerfile
└── README.md

▶️ How It Works (End-to-End Flow)

User clicks “Start Research”

Domain Scout discovers emerging domains

Question Generator formulates original research questions

Data Alchemist fetches real public data

Experiment Designer runs exploratory experiments

Critic evaluates validity and limitations

Paper Writer generates final mini research paper

Results + visualizations are displayed live

⚠️ Responsible AI Behavior

If confidence < 0.6, the system abstains from strong conclusions

All claims are tied to real evidence

Limitations & future work are explicitly stated

🌐 Live Demo

Once deployed, the system runs end-to-end with no human input required after pressing Start Research.

📌 Notes

This system prioritizes reasoning, transparency, and safety over flashy claims.

Experiments are intentionally simple but honest, reflecting real-world constraints.

📄 License

This project is for educational and evaluation purposes.

▶️ EXECUTION STEPS

🔹 1. Clone the Repository
git clone https://github.com/<your-username>/agentic-ai-research-assistant.git
cd agentic-ai-research-assistant

🔹 2. Create Virtual Environment (Recommended)
python -m venv .venv
source .venv/bin/activate     # Linux / Mac
.venv\Scripts\activate        # Windows

🔹 3. Install Dependencies
pip install -r requirements.txt

🔹 4. Set Environment Variables

Create a .env file or export variables directly:

GROQ_API_KEY=your_groq_api_key_here

🔹 5. Run the Application (Local)
streamlit run app.py


Open browser at:

http://localhost:8501


Click “Start Research” and observe autonomous execution.

🔹 6. Run with Docker (Optional)
Build Image
docker build -t agentic-ai-research .

Run Container
docker run -p 8501:8501 --env GROQ_API_KEY=your_key agentic-ai-research

🔹 7. Deploy to Railway

Push code to GitHub

Create a Railway project

Connect GitHub repo

Add environment variable:

GROQ_API_KEY


Deploy 🚀

Railway automatically builds and runs the Docker container.

✅ Expected Output

Emerging domain discovery

Original research questions

Real data analysis

Experimental visualizations

Mini research paper (Markdown)

Confidence score + abstain logic
