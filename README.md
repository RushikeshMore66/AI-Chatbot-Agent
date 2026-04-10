# 🧠 AI Personal Operations Agent (Local AI OS)

> A powerful **personal AI agent system** designed to manage *your daily digital life* — emails, WhatsApp, calendar, and system tasks — like a **local Jarvis**.

---

## 🚀 Vision

This project is not built for business automation.

It is designed as a **personal AI operating layer** that:

* Understands your intent
* Plans actions intelligently
* Executes tasks across your tools

Think of it as:

> 🧠 Your personal AI brain controlling your digital world

---

## ⚡ Core Capabilities

### 🗣️ Natural Language Control

* Talk to your system like a human
* Example:

  * “Send email to client about delay”
  * “Schedule meeting tomorrow at 5”
  * “Reply on WhatsApp”

---

### 🧩 Multi-Step AI Planning (LangGraph)

* Breaks complex tasks into steps
* Executes sequential workflows
* Example:

  * Understand request → Plan → Execute tools → Return result

---

### 🤖 Gemini LLM Integration

* Uses Google Gemini models for reasoning
* Fast and efficient decision making

---

### 🔗 Tool Integrations (Personal Only)

* 📧 Email (Gmail / SMTP)
* 💬 WhatsApp (via webhook / Twilio)
* 📅 Google Calendar
* 🖥️ Local system tasks (future)

---

### 🧠 Memory System

* Stores context of your conversations
* Improves over time

---

## 🏗️ Tech Stack

* **Backend**: FastAPI
* **AI Orchestration**: LangChain + LangGraph
* **LLM**: Gemini (Google Generative AI)
* **Server**: Uvicorn
* **Environment**: Python 3.11

---

## 📂 Project Structure

```
AI-Operation-Agent/
│
├── main.py                 # FastAPI entry point
├── agent/
│   ├── graph.py           # LangGraph workflow
│   ├── nodes.py           # Planner + executor nodes
│   ├── tools.py           # Tool functions (email, whatsapp, etc.)
│
├── .env                   # API keys (not committed)
├── requirements.txt
└── README.md
```

---

## 🔑 Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/ai-operation-agent.git
cd ai-operation-agent
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Add Environment Variables

Create `.env` file:

```env
GOOGLE_API_KEY=your_gemini_api_key
```

---

### 5️⃣ Run Server

```bash
uvicorn main:app --reload
```

---

## 🧪 API Usage

### Chat Endpoint

```bash
POST /chat
```

#### Request:

```json
{
  "message": "Schedule a meeting tomorrow at 5 PM"
}
```

---

### WhatsApp Webhook

```bash
POST /whatsapp
```

* Receives messages
* Processes via AI agent
* Returns response

---

## 🔮 Future Roadmap

* 🎙️ Voice assistant (Jarvis-style)
* 🖥️ Full local system control
* 🧠 Persistent long-term memory
* 📊 Personal dashboard UI
* 🔌 More integrations (Notion, Files, Browser)

---

## ⚠️ Important Note

This system is:

✅ Personal-use focused
❌ Not designed for enterprise automation
❌ Not optimized for multi-user environments

---

## 🧠 Philosophy

> AI should not replace humans.
> It should **amplify personal capability**.

This project aims to build:

* Faster execution
* Better decision support
* Seamless human-AI interaction

---

## 🤝 Contribution

This is a personal experimental project, but contributions are welcome for:

* New tools
* Better workflows
* Performance improvements

---

## 📜 License

MIT License

---

## 🔥 Final Thought

> This is not just a chatbot.
> This is the **foundation of your personal AI operating system**.

---
