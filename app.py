import sys
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(ROOT_DIR)

import streamlit as st
from graph import graph
from graph_state import ResearchState

from dotenv import load_dotenv
load_dotenv()   # 🔑 MUST BE FIRST

import streamlit as st
import plotly.express as px

from graph import graph
from graph_state import ResearchState
from utils.live_logger import stream_log

st.set_page_config(
    page_title="Autonomous Agentic Research Assistant",
    layout="wide"
)

st.title("🧠 Autonomous Agentic AI Research Assistant")
st.caption("Zero human input • Multi-agent • Self-critical • Research-grade")

st.markdown("---")

# ---- Run Button ----
if st.button("🚀 Start Research"):
    log_box = st.container()
    output_box = st.container()

    state = ResearchState()

    with st.spinner("Agents are working autonomously…"):

        stream_log(log_box, "🧭 Domain Scout Agent is scanning emerging domains…")
        state = graph.invoke(state)

        stream_log(log_box, "❓ Question Generator Agent is synthesizing novel research questions…")
        stream_log(log_box, "🧪 Data Alchemist Agent is gathering and cleaning heterogeneous data…")
        stream_log(log_box, "📐 Experiment Designer Agent is running statistical experiments…")
        stream_log(log_box, "🧨 Critic Agent is attacking assumptions and results…")
       
    
    st.success("✅ Autonomous Research Completed")

    # ---- OUTPUTS ----
    with output_box:
        st.markdown("## 📄 Generated Mini Research Paper")
        state = ResearchState()

        updates = graph.invoke(state)

        state = ResearchState(**{
            **state.model_dump(),
            **updates
        })

        st.markdown(state.paper_markdown)



        st.markdown("---")
        st.markdown("## 📊 Experimental Visualization")

        if "dataset" in state.experiment_results:
            df = state.experiment_results["dataset"]
            # ---- SAFE, SCHEMA-AWARE VISUALIZATION ----
            numeric_cols = df.select_dtypes(include="number").columns.tolist()

            if len(numeric_cols) >= 1:
                fig = px.line(
                    df,
                    y=numeric_cols,
                    title="Exploratory Data Trends (Numeric Features)"
                )
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.warning("No numeric columns available for visualization.")


        st.markdown("---")
       
