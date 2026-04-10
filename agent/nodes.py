from os import system
from langchain_groq import ChatGroq
from agent.state import AgentState
from agent.memory import load_memory
from dotenv import load_dotenv
import os
import json

load_dotenv()

llm = ChatGroq(model="grok-4.1-fast",mistral="mistral-large-latest", 
                            api_key=os.getenv("GROK_API_KEY"),
                            temperature=0.2
)

def planner_node(state: AgentState):
    memory_context = load_memory()
    

    prompt = """
You are an AI Business Automation Agent.

conversation history:
{memory_context}

break the user request into steps.

Available actions:
- send_email
- update_crm
- notify
- reply

[
  {{"action": "", "data": {{}}}}
]

User: {state['user_input']}
"""
    response = llm.invoke(prompt)
    return {"plan": response.content}

def analyze_node(state: AgentState):
    plan_str = state.get("plan", "")
    
    try:
        plan = json.loads(plan_str)
    except:
        plan = [{"action": "reply", "data": {"message": plan_str}}]
    return {**state, "plan": plan}

from agent.tools import execute_tools

def executor_node(state: AgentState):
    results = []

    for step in state.get("plan", []):
        result = execute_tools(step)
        results.append(str(result))
    
    return {**state, "results": results}
    
