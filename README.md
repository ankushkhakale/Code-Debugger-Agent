# AI Code Debugger Agent

An intelligent code debugging tool powered by DeepSeek AI that analyzes code snippets and provides detailed debugging suggestions with corrected code.

## Features

- **Multi-language Support**: Debug code in Python, JavaScript, Java, C++, and Ruby
- **AI-Powered Analysis**: Uses DeepSeek R1 model for intelligent code analysis
- **Web Interface**: User-friendly Gradio interface for easy interaction
- **Error Identification**: Identifies bugs and provides corrected code
- **Detailed Explanations**: Offers comprehensive explanations for fixes

## Requirements

- Python 3.8+
- Ollama (running locally with DeepSeek R1 model)
- Required Python packages:
  - gradio
  - requests

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Code-Debugger-Agent
```

2. Create a virtual environment:
```bash
python -m venv .venv
.\.venv\Scripts\activate  # On Windows
source .venv/bin/activate  # On macOS/Linux
```

3. Install dependencies:
```bash
pip install gradio requests
```

4. Ensure Ollama is installed and running with DeepSeek model:
```bash
ollama pull deepseek-r1
ollama serve
```

## Usage

Run the application:
```bash
python "code debugger.py"
```

## Architecture

- **Backend**: Python with Requests library for API calls
- **Frontend**: Gradio web interface
- **AI Model**: DeepSeek R1 via Ollama API

## Troubleshooting

**"Site refused to connect"**:
- Ensure Ollama is running: `ollama serve`
- Verify DeepSeek model is installed: `ollama list`
- Check port 7860 is not in use

