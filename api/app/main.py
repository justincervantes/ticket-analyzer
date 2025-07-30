from fastapi import FastAPI
import os
import requests
import json

app = FastAPI()
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://ollama:11434/api/generate")

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "Hello, world!"}

@app.get("/ask")
def ask(question: str = "hello", model: str = "gemma:2b"):
    payload = {"model": model, "prompt": question}
    with requests.post(OLLAMA_URL, json=payload, stream=True) as r:
        if not r.ok:
            return {"error": r.text}

        # Ollama streams multiple JSON objects
        output_text = ""
        for line in r.iter_lines():
            if line:
                try:
                    data = json.loads(line.decode("utf-8"))
                    output_text += data.get("response", "")
                except json.JSONDecodeError:
                    pass

        return {"question": question, "model": model, "response": output_text}