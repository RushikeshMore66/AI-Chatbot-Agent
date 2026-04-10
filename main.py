from matplotlib.pyplot import cla
from fastapi import FastAPI, Request
from agent.graph import graph
from pydantic import BaseModel
import sys
import os
app = FastAPI()

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ChatRequest(BaseModel):
    message: str


@app.post("/chat")
async def chat(req: ChatRequest):
    result = graph.invoke({
        "user_input": req.message
    })

    return {
        "results": result.get("results")
    }


@app.post("/whatsapp")
async def whatsapp(req: Request):
    form = await req.form()
    msg = form.get("Body")

    result = graph.invoke({
        "user_input": msg
    })

    return {
        "reply": " | ".join(result.get("results", []))
    }