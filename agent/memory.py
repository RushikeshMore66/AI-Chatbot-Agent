from langchain_core.messages import HumanMessage, AIMessage

chat_history = []

def save_memory(user, ai):
    chat_history.append(HumanMessage(content=user))
    chat_history.append(AIMessage(content=ai))

def load_memory():
    return chat_history
