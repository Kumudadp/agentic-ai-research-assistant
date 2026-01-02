from dotenv import load_dotenv
load_dotenv()  # safe redundancy

from langchain_groq import ChatGroq
import os

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise RuntimeError(
        "❌ GROQ_API_KEY not found. "
        "Check .env file or environment variables."
    )

llm = ChatGroq(
    api_key=api_key,
    model="llama-3.1-8b-instant",
    temperature=0.3
)
