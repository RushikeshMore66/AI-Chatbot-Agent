from langgraph.graph import StateGraph
from agent.state import AgentState
from agent.nodes import planner_node, analyze_node, executor_node

builder = StateGraph(AgentState)

builder.add_node("planner", planner_node)
builder.add_node("analyze", analyze_node)
builder.add_node("executor", executor_node)

builder.set_entry_point("planner")
builder.add_edge("planner", "analyze")
builder.add_edge("analyze", "executor")
builder.add_edge("executor", "__end__")

graph = builder.compile()