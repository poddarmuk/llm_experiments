"""Interactive Ollama ChatBot with streaming responses and conversation memory."""

import os
import sys
from typing import List, Dict
from dotenv import load_dotenv
import ollama


def run_chatbot(model: str = "llama3.2") -> None:
    load_dotenv()
    host = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    client = ollama.Client(host=host)

    print("=" * 60)
    print(f"🤖 Ollama Interactive ChatBot")
    print(f"Model: {model} | Host: {host}")
    print("Commands: type 'exit', 'quit', or 'q' to end. Type 'clear' to reset chat.")
    print("=" * 60)

    messages: List[Dict[str, str]] = [
        {"role": "system", "content": "You are a helpful, concise AI assistant."}
    ]

    while True:
        try:
            user_input = input("\nYou: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break

        if not user_input:
            continue

        if user_input.lower() in ("exit", "quit", "q"):
            print("Goodbye!")
            break

        if user_input.lower() == "clear":
            messages = [
                {"role": "system", "content": "You are a helpful, concise AI assistant."}
            ]
            print("🧹 Conversation history cleared.")
            continue

        messages.append({"role": "user", "content": user_input})
        print(f"\nAssistant: ", end="", flush=True)

        try:
            assistant_response = ""
            stream = client.chat(model=model, messages=messages, stream=True)
            for chunk in stream:
                content = chunk.get("message", {}).get("content", "")
                assistant_response += content
                print(content, end="", flush=True)
            print()

            messages.append({"role": "assistant", "content": assistant_response})
        except Exception as e:
            print(f"\n❌ Error contacting Ollama: {e}")
            print("Make sure Ollama is running (`ollama serve`).")


def main() -> None:
    # Allow passing model name as first argument: uv run chatbot mistral
    model_name = sys.argv[1] if len(sys.argv) > 1 else "llama3.2"
    run_chatbot(model=model_name)


if __name__ == "__main__":
    main()
