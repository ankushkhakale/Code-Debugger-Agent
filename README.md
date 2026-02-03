# AI Code Debugger Agent

An intelligent code debugging tool powered by DeepSeek AI. Paste a code snippet, select a language, and get concise bug analysis with corrected code and explanations.

## Highlights

- **Multi-language Support**: Python, JavaScript, Java, C++, Ruby
- **AI-Powered Debugging**: DeepSeek R1 model via local Ollama API
- **Simple Web UI**: Gradio interface for quick use
- **Actionable Output**: Fixes + explanation in one response

## Project Layout

- **code debugger.py**: Gradio UI app (interactive debugger)
- **app.py**: FastAPI backend (API-only mode)
- **README.md**: Documentation

## Requirements

- Python 3.8+
- Ollama installed and running locally
- Model: `deepseek-r1`
- Python packages:
  - gradio
  - requests
  - fastapi
  - uvicorn

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd Code-Debugger-Agent
```

2. Create a virtual environment:
```bash
python -m venv .venv
.\.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux
```

3. Install dependencies:
```bash
pip install gradio requests fastapi uvicorn
```

4. Install and start Ollama with DeepSeek:
```bash
ollama pull deepseek-r1
ollama serve
```

## Usage

### Option A: Gradio Web App

Run the UI application:
```bash
python "code debugger.py"
```

Open in your browser:
**http://127.0.0.1:7860**

### Option B: FastAPI API Server

Run the API:
```bash
uvicorn app:app --reload
```

API endpoint:
**POST http://127.0.0.1:8000/debug_code/**

Example request:
```json
{
  "code_snippet": "def add(a,b): return a+b\nprint(add(1))"
}
```

## Configuration

Update the Ollama endpoint if needed:

```python
OLLAMA_URL = "http://localhost:11434/api/generate"
```

## How It Works

1. User submits a code snippet and language.
2. The app builds a debug prompt.
3. The prompt is sent to the local Ollama API.
4. DeepSeek analyzes and returns fixes with explanations.
