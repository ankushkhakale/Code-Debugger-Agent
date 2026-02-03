import gradio as gr
import requests

#Deepseek ApI URL
OLLAMA_URL = "http://localhost:11434/api/generate"

def debug_code(code_snippet, language ="Python"):
    prompt = f"Analyze and debug the following {language} code:\n\n{code_snippet}\n\n Identify any errors and provide a corrected version of the code along with explanations."
    payload = {
        "model": "deepseek-r1",
        "prompt": prompt,
        "stream": False,
    }
    response = requests.post(OLLAMA_URL, json=payload)
    if response.status_code == 200:
        return response.json().get("response", "No debugging suggestions available.")
    else:
        return f"Error:{response.text}"
    
# #Test code debugger
# if __name__ == "__main__":
#     test_code = "def add_numbers(a,b): return a+b\n print(add_numbers(5))"
#     print(debug_code(test_code))

#Gradio Interface
interface = gr.Interface(
    fn =debug_code,
    inputs=[
        gr.Textbox(lines=10, label="Code Snippet"),
        gr.Dropdown(choices=["Python", "JavaScript", "Java", "C++", "Ruby"], label="Programming Language", value="Python")
    ],
    outputs=gr.Textbox(label="AI Debugger Output"),
    title="AI Code Debugger",
    description="Paste your code snippet and select the programming language to get debugging suggestions from the AI.",
)