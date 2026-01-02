from pydantic import BaseModel
from typing import List, Dict, Optional, Any

class ResearchState(BaseModel):
    # ... other fields ...



    iteration: int = 0
    max_iterations: int = 5

    domains: List[Dict[str, Any]] = []
    selected_domain: Optional[Dict[str, Any]] = None

    research_questions: List[Dict[str, Any]] = []
    selected_question: Optional[Dict[str, Any]] = None

    data_sources: List[Dict[str, Any]] = []
    experiment_results: Optional[Dict[str, Any]] = None

    critique: Optional[Dict[str, Any]] = None
    confidence_score: float | None = None
    uncertainty_notes: List[str] = []
    abstain: bool = True




    paper_markdown: Optional[str] = None
