"""Ollama ChatBot UI using Gradio."""

import os
import sys
from typing import Generator
from dotenv import load_dotenv
import gradio as gr
import ollama

load_dotenv()
OLLAMA_HOST = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
client = ollama.Client(host=OLLAMA_HOST)


def make_chat_fn(model_name: str = "llama3.2"):
    def predict(message: str, history: list) -> Generator[str, None, None]:
        messages = [
            {"role": "system", "content": "You are a helpful, friendly AI assistant."}
        ]

        # Handle Gradio history format (supports both tuples and dict list formats)
        for turn in history:
            if isinstance(turn, dict):
                messages.append(
                    {"role": turn.get("role", "user"), "content": str(turn.get("content", ""))}
                )
            elif isinstance(turn, (list, tuple)) and len(turn) == 2:
                messages.append({"role": "user", "content": str(turn[0])})
                messages.append({"role": "assistant", "content": str(turn[1])})

        messages.append({"role": "user", "content": message})

        response = ""
        try:
            stream = client.chat(model=model_name, messages=messages, stream=True)
            for chunk in stream:
                content = chunk.get("message", {}).get("content") or ""
                if content:
                    response += content
                    yield response
        except Exception as e:
            yield f"⚠️ Error contacting Ollama: {e}\nEnsure Ollama is running (`ollama serve`)."

    return predict


def build_app(model_name: str = "llama3.2") -> gr.ChatInterface:
    return gr.ChatInterface(
        fn=make_chat_fn(model_name),
        title=f"🦙 Ollama Local ChatBot ({model_name})",
        description=f"Interactive local ChatBot powered by Ollama & Gradio (Connected to `{OLLAMA_HOST}`)",
    )


def main() -> None:
    model_name = sys.argv[1] if len(sys.argv) > 1 else "llama3.2"
    app = build_app(model_name)
    print(f"Starting Gradio ChatBot with model: {model_name} at http://localhost:7860")
    app.launch(server_port=7860, inbrowser=False)


if __name__ == "__main__":
    main()
