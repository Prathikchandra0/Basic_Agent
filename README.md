# ⚡ Dynamic Tool-Calling AI Agent

<p align="center">

**An LLM-powered agent that dynamically selects and executes the right tool based on the user's request.**

<br>

<img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Groq-API-F55036?style=for-the-badge"/>
<img src="https://img.shields.io/badge/OpenAI-SDK-412991?style=for-the-badge&logo=openai&logoColor=white"/>
<img src="https://img.shields.io/badge/Agentic%20AI-Tool%20Calling-8A2BE2?style=for-the-badge"/>

</p>

---

## 🧠 What Is This?

This project demonstrates the **core mechanism behind tool-calling AI agents**.

Instead of hardcoding which Python function should run, the LLM analyzes the user's request, selects the appropriate tool, generates the required arguments, and the Python program dynamically executes the selected function.


# ✨ Features

* 🤖 LLM-powered tool selection
* 🔧 Multiple custom Python tools
* ⚡ Dynamic function execution
* 📦 JSON Schema-based tool definitions
* 🧩 Automatic argument parsing
* 🌦️ Weather lookup tool
* 🧮 Mathematical calculation tool
* 🔌 Groq API integration
* 🐍 OpenAI-compatible Python SDK
* 🔐 Environment-variable based API key management
* 🏗️ Extensible tool registry architecture

---

# 🛠️ Available Tools

## 🌦️ `get_weather`

Returns weather information for supported cities.

Example:

```text
User:
What is the weather in Hyderabad?
```

The LLM can generate:

```json
{
  "city": "Hyderabad"
}
```

The agent dynamically executes:

```python
get_weather(city="Hyderabad")
```

---

## 🧮 `Calculator`

Evaluates mathematical expressions.

Example:

```text
User:
95 + 5
```

The LLM generates:

```json
{
  "expression": "95 + 5"
}
```

The agent dynamically executes:

```python
Calculator(expression="95 + 5")
```

Result:

```text
100
```

---

# 🧩 Architecture

The project uses two important layers.

### 1. Tool Schemas

The `tools` variable describes available tools to the LLM.

```python
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current weather data of a city",
            ...
        }
    }
]
```

The LLM uses this information to understand:

> Which tools are available and what arguments they require.

---

### 2. Tool Registry

The Python application maintains a mapping between tool names and actual functions.

```python
tool_functions = {
    "get_weather": get_weather,
    "Calculator": Calculator
}
```

This is what makes the execution dynamic.

Instead of writing:

```python
if tool_name == "get_weather":
    get_weather(...)
elif tool_name == "Calculator":
    Calculator(...)
```

the program simply does:

```python
function = tool_functions[tool_name]
result = function(**arguments)
```

This allows new tools to be added without rewriting the execution logic.

---

# 🔄 Agent Flow

```text
                    ┌─────────────────┐
                    │      USER       │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │       LLM       │
                    │                 │
                    │ Analyze Request │
                    └────────┬────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │    Tool Selection   │
                  └──────────┬──────────┘
                             │
                 ┌───────────┴───────────┐
                 │                       │
                 ▼                       ▼
          get_weather()            Calculator()
                 │                       │
                 └───────────┬───────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │  Tool Registry  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Execute Function│
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │      Result     │
                    └─────────────────┘
```

---

# 📁 Project Structure

```text
agentic-ai/
│
├── jsonregistering.py
├── .env
├── .gitignore
└── README.md
```

### `jsonregistering.py`

Main application containing:

* LLM configuration
* Tool definitions
* Tool schemas
* Tool registry
* Tool execution
* Response handling

### `.env`

Stores sensitive API credentials.

```env
groq_key=YOUR_GROQ_API_KEY
```

### `.gitignore`

Prevents sensitive files from being committed.

```gitignore
.env
__pycache__/
*.pyc
```

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd <YOUR_REPOSITORY_NAME>
```

## 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

---

## 3. Install dependencies

```bash
pip install openai python-dotenv
```

---

## 4. Configure the API key

Create a `.env` file:

```env
groq_key=YOUR_GROQ_API_KEY
```

**Never commit your `.env` file to GitHub.**

---

# 🚀 Running the Project

Run:

```bash
python jsonregistering.py
```

Example output:

```text
get_weather(city) - Get the current weather data of a city
Calculator(expression) - Evaluate the math expression

finish reason : tool_calls

Tool : Calculator
Arguments : {"expression":"95 + 5"}

Result : 100
```

---

# 🧠 Core Concept

The most important concept in this project is **dynamic tool execution**.

The LLM returns the name of the function it wants to use:

```python
tool_name = tc.function.name
```

The arguments are extracted from the tool call:

```python
arguments = json.loads(tc.function.arguments)
```

The corresponding Python function is retrieved:

```python
function = tool_functions[tool_name]
```

And finally executed:

```python
result = function(**arguments)
```

This transforms a static collection of functions into a basic **tool-using AI agent architecture**.

---

# 🔥 Why This Matters

A traditional program might look like:

```text
Input
 ↓
if weather:
    weather()
else:
    calculator()
```

The developer must decide which function to execute.

With tool calling:

```text
Input
 ↓
LLM
 ↓
LLM decides which tool is appropriate
 ↓
Python dynamically executes it
```

This is one of the fundamental building blocks of **Agentic AI systems**.

---

# ➕ Adding a New Tool

Suppose you want to add:

```python
def get_stock_price(symbol: str):
    ...
```

Add its JSON schema to `tools` and register the function:

```python
tool_functions = {
    "get_weather": get_weather,
    "Calculator": Calculator,
    "get_stock_price": get_stock_price
}
```

The execution engine remains unchanged:

```python
function = tool_functions[tool_name]
result = function(**arguments)
```

That's the key advantage of the registry approach.

---

# 🧪 Example Requests

| User Request                        | Tool Selected |
| ----------------------------------- | ------------- |
| `95 + 5`                            | `Calculator`  |
| `25 * 8`                            | `Calculator`  |
| `What is the weather in Hyderabad?` | `get_weather` |
| `Tell me the weather in Delhi`      | `get_weather` |

---

# ⚠️ Important Security Note

The calculator currently uses Python's `eval()`.

Although the input is restricted using an allowed-character check, `eval()` should **not** be treated as a fully secure expression evaluator for production applications.

For a production-grade agent, replace it with a dedicated mathematical expression parser or a safer evaluation approach.

---

# 🗺️ Roadmap

This project is intentionally starting with the fundamentals.

### Current

* [x] LLM integration
* [x] Function definitions
* [x] JSON tool schemas
* [x] Multiple tools
* [x] Dynamic tool selection
* [x] Dynamic function execution
* [x] JSON argument parsing

### Next

* [ ] Multiple tool calls
* [ ] Send tool results back to the LLM
* [ ] Agent execution loop
* [ ] Automatic final response generation
* [ ] Error handling and retries
* [ ] More tools
* [ ] Web search
* [ ] Database tools
* [ ] Memory
* [ ] Tool execution logging
* [ ] Production-safe calculator
* [ ] Streaming responses

---

# 🌌 The Bigger Picture

This project represents the basic transition from:

```text
LLM
```

to:

```text
LLM + Tools
```

and eventually:

```text
LLM
 +
Tools
 +
Memory
 +
Loop
 +
Decision Making
 =
Agentic AI
```

The goal is not simply to make an LLM answer questions.

The goal is to allow the LLM to **decide what action should be taken and use external capabilities to accomplish the task.**

---

# 👨‍💻 Author

**Prathik Chandra Vuppala**

Computer Science Engineering Student
Exploring **Agentic AI • LLMs • Tool Calling • Software Engineering**

---

<p align="center">

### ⚡ Built to understand how AI agents actually work.

**LLM → Decide → Select Tool → Execute → Return Result**

</p>
