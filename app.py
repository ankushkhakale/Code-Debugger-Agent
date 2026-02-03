from fastapi import FastAPI
import requests

app = fastAPI()
OLLAMA_URL = "http://localhost:11434/api/generate"