# LLM Experiments

Personal experiments and explorations with Large Language Models (LLMs), prompt engineering, agents, and tooling.

---

## 📁 Project Structure

```text
llm_experiments/
├── .env.example              # Template for API keys and secrets
├── .gitignore                # Git ignore rules for Python, venv, and secrets
├── pyproject.toml            # PEP 621 dependencies & project configuration
├── README.md                 # Project documentation
├── src/
│   └── llm_experiments/     # Main package code
│       ├── __init__.py
│       ├── chatbot.py        # Interactive streaming Ollama chatbot
│       └── main.py
└── tests/                    # Unit tests
    ├── __init__.py
    └── test_basic.py
```

---

## 🚀 Getting Started

### 1. Environment Setup

Copy `.env.example` to `.env` and fill in your API keys (e.g. OpenAI, Anthropic, Gemini):

```bash
cp .env.example .env
```

> **Note:** `.env` is included in `.gitignore` to prevent leaking your private API keys on GitHub.

---

### 2. Installing Dependencies

You can use either **`uv`** (recommended: extremely fast) or standard **`python -m venv` / `pip`**.

#### Option A: Using `uv` (Recommended)

> For full prerequisites (Git, uv, Ollama, OpenAI & Anthropic API keys), see the [Installation & Setup Guide](guides/installation.md).

`uv` automatically manages virtual environments and installs dependencies quickly:

```bash
# Sync all dependencies and create virtual environment (.venv)
uv sync

# Or sync including dev tools (pytest, ruff, mypy):
uv sync --extra dev

# Run the project entrypoint:
uv run llm-experiments

# Launch the terminal Ollama chatbot:
uv run chatbot
# Or with a specific local model: uv run chatbot deepseek-r1:1.5b

# Launch the Gradio web ChatBot (opens on http://localhost:7860):
uv run gradio-bot
```

To add new dependencies with `uv`:
```bash
# Add a runtime package (e.g., langchain, openai)
uv add openai langchain

# Add a development tool
uv add --dev ipykernel
```

---

#### Option B: Using Standard Python (`venv` + `pip`)

If you prefer standard Python tooling:

```bash
# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install project in editable mode with dev dependencies
pip install -e ".[dev]"

# Run the entrypoint
python -m llm_experiments.main
```

To add dependencies with `pip`:
- Add the package name directly to `dependencies` in `pyproject.toml`.
- Run `pip install -e .` again.

---

## 🧪 Running Tests & Quality Checks

With `uv`:
```bash
uv run pytest
uv run ruff check .
```

With active `venv`:
```bash
pytest
ruff check .
```

---

## 📝 License

MIT
