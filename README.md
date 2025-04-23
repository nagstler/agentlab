# AgentLab 🧠🤖

AgentLab is a practical, stage-by-stage learning project to **understand AI agents using LangChain**.

It is not a boilerplate repo — it’s a guided, hands-on path to demystify how agents actually work, what role LangChain plays, and how to build robust multi-tool AI systems from the ground up.

---

## 🧠 What is an AI Agent?

An AI Agent is not just a large language model (LLM). It is a system that:
- Can take input (a user question)
- Decide whether to respond directly or **act** via tools
- Use **memory** to persist information across turns
- Reason about **which tool** to use and when to stop

Think of it as:
> LLM + Planning + Tool Use + State Management

---

## 🧰 Why LangChain?

LangChain provides:
- A standard **AgentExecutor** that manages reasoning loops
- Easy-to-register **tools** (wrapped functions)
- Built-in support for **OpenAI tool calling**, vector stores, retrievers, memory modules, and more
- A modular architecture to build real-world agentic applications

---

## 🏗️ Agent Architecture in This Repo

Every agent here follows a consistent mental model:

```
[User Input] 
    ↓
[Prompt + Memory] 
    ↓
[LangChain Agent Executor]
    ↓
[LLM decides] —> Tool? → [Tool Call] → Back to Agent 
    ↓
[Final Answer]
```

Each stage adds one new capability:
- Tool injection
- Multi-tool reasoning
- Conversation memory
- Custom prompts & personas
- Function-calling with structured input

---

## 🔍 Who This Is For

This repo is for:
- Developers new to LangChain or agents
- AI builders wanting to learn how agents are wired
- Technical folks building POCs or agent-backed APIs
- Anyone who wants a practical, working mental model of how AI agents reason and act

---

## 🧪 What You’ll Find

- Each stage has its own `agent`, `tool`, and `runner`
- You can run each one independently
- Each step builds your understanding of how agents work in real applications

---

## 📦 Setup

Clone the repository and install dependencies:

```bash
git clone https://github.com/nagstler/agentlab
cd agentlab
cp .env.example .env   # Add your OpenAI API Key
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

To run any stage:

```bash
python run/run_agent_vX.py  # Replace X with stage number (0 to 5 so far)
```

---

## 🧭 Stage-by-Stage Breakdown

### ✅ Stage 0: Basic Agent (ReAct + OpenAI)

- Setup a basic project layout
- Use OpenAI's LLM with a built-in `llm-math` tool
- Understand LangChain’s ReAct-style reasoning loop
- Run a basic agent using `.invoke()`

Script: `run/run_agent_v0.py`

---

### 🔧 Stage 1: Custom Tool – `my_calc`

- Write a local calculator function
- Wrap it using LangChain's `Tool` class
- Replace built-in tools with your own
- Learn LangChain’s tool interface

Script: `run/run_agent_v1.py`

---

### 🧠 Stage 2: Multi-Tool Agent

- Add multiple tools (e.g. calculator + reverse text)
- Let the agent choose the appropriate tool at runtime
- See tool routing decisions in the output

Script: `run/run_agent_v2.py`

---

### 🧾 Stage 3: Add Memory

- Enable multi-turn conversations using `ConversationBufferMemory`
- Let the agent remember results across turns
- Simulate a conversational assistant

Script: `run/run_agent_v3.py`

---

### 🎯 Stage 4: Custom Prompt Template

- Customize the agent’s system prompt (introduce "Marvin" persona)
- Inject tone and behavior into the agent
- Influence tool use and response style with prompt tweaks

Script: `run/run_agent_v4.py`

---

### 🧩 Stage 5: Function-Calling Agent (Structured Tools)

- Use `StructuredTool` for typed input functions
- Build a function-calling agent using `gpt-4`
- Implement structured prompts with memory and tool routing
- Learn prompt design for `OpenAIFunctionsAgent`

Script: `run/run_agent_v5.py`

---

## ✅ What We’ve Learned So Far

- How LangChain agents work under the hood
- Building and wiring tools for agent use
- Controlling behavior with memory and prompts
- Using OpenAI’s function interface for structured reasoning

---

## 📌 Next Stages (WIP)

- Stage 6: ToolRetriever + Dynamic Tool Selection (via embeddings)
- Stage 7: Tracing and Debugging
- Stage 8: LangGraph Migration
- Stage 9: Serve via FastAPI
- Stage 10: Production and Evaluation

---

Each stage builds on the last. You can run any stage independently, modify the tools, or create your own variations.

This is a **learning repo**, not a production framework — built for clarity and deep understanding.