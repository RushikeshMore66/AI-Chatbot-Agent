from typing import TypedDict, List, Optional

class AgentState(TypedDict):
    user_input: str
    plan: Optional[List[dict]]
    results: Optional[List[str]]