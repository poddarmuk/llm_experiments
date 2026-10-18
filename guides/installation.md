# Installation & Setup Guide

This guide covers everything you need to set up your environment for **llm_experiments**:
1. [Installing Git & Cloning the Repository](#1-installing-git--cloning-the-repository)
2. [Installing `uv` (Python Package Manager)](#2-installing-uv)
3. [Installing Ollama (Local LLMs)](#3-installing-ollama)
4. [Creating Cloud AI Accounts & API Keys (OpenAI & Anthropic)](#4-creating-cloud-ai-accounts--api-keys-openai--anthropic)

---

# 1. Installing Git & Cloning the Repository

Git is required to clone the codebase, track changes, and collaborate.

## 📥 Installing Git

### macOS
- **Option A (Xcode Command Line Tools - Recommended):**
  ```bash
  xcode-select --install
  ```
- **Option B (Homebrew):**
  ```bash
  brew install git
  ```

### Linux
- **Debian / Ubuntu:**
  ```bash
  sudo apt update && sudo apt install -y git
  ```
- **Fedora / RHEL:**
  ```bash
  sudo dnf install -y git
  ```
- **Arch Linux:**
  ```bash
  sudo pacman -S git
  ```

### Windows
- **Option A (WinGet):**
  ```powershell
  winget install --id Git.Git -e --source winget
  ```
- **Option B (Installer):**
  Download the official installer from [git-scm.com/download/win](https://git-scm.com/download/win).

---

## ⚙️ Initial Git Configuration

If this is your first time using Git on your machine, configure your identity:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

Verify your Git installation:
```bash
git --version
```

---

## 📂 Cloning this Repository

### Option A: Using HTTPS (Standard)
```bash
git clone https://github.com/poddarmuk/llm_experiments.git
cd llm_experiments
```

### Option B: Using SSH (If you have SSH keys configured)
```bash
git clone git@github.com:poddarmuk/llm_experiments.git
cd llm_experiments
```

### Switching & Verifying the Branch

Once inside the cloned folder, verify you are on the `main` branch:

```bash
# Check current branch
git status

# Ensure you have latest changes from origin
git pull origin main

# If you need to switch or checkout main explicitly
git checkout main
```

---

# 2. Installing `uv`

## 🚀 Quick Install

### macOS & Linux

The recommended method is the official standalone installer:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Alternatively, on macOS using **Homebrew**:

```bash
brew install uv
```

---

### Windows

Using **PowerShell**:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Or using **WinGet**:

```powershell
winget install --id=astral-sh.uv -e
```

---

### Alternative Package Managers

If you already have Python and `pip` or `pipx`:

```bash
# Using pipx (recommended if using Python-based tools)
pipx install uv

# Or using pip
pip install uv
```

Using **Cargo** (Rust):

```bash
cargo install --locked uv
```

---

## ✅ Verify Installation

Check that `uv` is installed and available in your `PATH`:

```bash
uv --version
```

Output should look like:
```text
uv 0.5.x (or newer)
```

> **Note:** If `uv` is not recognized after running the standalone installer script, restart your terminal or reload your shell profile:
> ```bash
> source ~/.zshrc   # or source ~/.bashrc
> ```

---

## 🔄 Updating `uv`

To update a standalone installation of `uv` to the latest version:

```bash
uv self update
```

*(If installed via Homebrew, use `brew upgrade uv`)*

---

## 💡 Shell Autocompletion (Optional)

Enable tab autocompletion in your shell:

### Zsh (macOS default)
```bash
echo 'eval "$(uv generate-shell-completion zsh)"' >> ~/.zshrc
source ~/.zshrc
```

### Bash
```bash
echo 'eval "$(uv generate-shell-completion bash)"' >> ~/.bashrc
source ~/.bashrc
```

### Fish
```bash
echo 'uv generate-shell-completion fish | source' >> ~/.config/fish/config.fish
```

---

## 🛠️ Using `uv` with this Project

Once installed, use these core commands in the project directory:

```bash
# 1. Install all dependencies and setup the virtual environment (.venv)
uv sync --extra dev

# 2. Run the application
uv run llm-experiments

# 3. Add new packages to the project
uv add <package-name>

# 4. Run tests
uv run pytest
```

---

# 3. Installing Ollama

[Ollama](https://ollama.com/) allows you to run open-source large language models (such as Llama 3, Mistral, Gemma 2, and DeepSeek) locally on your machine.

---

## 🚀 Installation

### macOS

- **Option A (Homebrew - Recommended):**
  ```bash
  brew install --cask ollama
  ```
- **Option B (Direct Download):**
  Download the official `.zip` installer from [ollama.com/download](https://ollama.com/download).

---

### Linux

Run the official install script:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

---

### Windows

- **Option A (WinGet):**
  ```powershell
  winget install Ollama.Ollama
  ```
- **Option B (Direct Download):**
  Download the installer (`OllamaSetup.exe`) from [ollama.com/download/windows](https://ollama.com/download/windows).

---

### Docker (Alternative)

If you prefer running Ollama in a Docker container:

```bash
# CPU only:
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama

# With Nvidia GPU support:
docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```

---

## ✅ Verify & Start the Ollama Service

1. Check that the CLI is installed:
   ```bash
   ollama --version
   ```

2. Start the Ollama server (if not already running as a desktop app or system service):
   ```bash
   ollama serve
   ```
   By default, the Ollama server listens on `http://localhost:11434`.

---

## 📦 Step 1: Download (Pull) a Model

Before you can run a chatbot or make API calls, you must download a model's weights to your local machine using `ollama pull`:

```bash
# Recommended starter model (fast, high quality, ~2.0 GB):
ollama pull llama3.2

# Other popular options:
ollama pull deepseek-r1:1.5b   # Lightweight reasoning model (~1.1 GB)
ollama pull mistral            # General reasoning & instructions (~4.1 GB)
ollama pull qwen2.5-coder:7b   # Code generation & assistance (~4.7 GB)
```

Verify that the model was downloaded successfully:
```bash
ollama list
```

---

## 💬 Step 2: Run Ollama as an Interactive ChatBot

There are three ways to chat with your local models:

### Option A: Built-in Terminal ChatBot (Instant)

Ollama includes a built-in terminal chat interface. Run:

```bash
ollama run llama3.2
```

This starts an interactive chat session immediately:
```text
>>> Send a message (/? for help)
>>> Hi, can you write a Python function to reverse a list?
```
- Type `/bye` or press `Ctrl + D` to exit.
- Type `/?` to view keyboard shortcuts and multi-line mode.

---

### Option B: Project Python Streaming ChatBot (`uv run chatbot`)

This repository comes with an interactive streaming chatbot built with Python and the Ollama SDK:

```bash
# Start the chatbot with the default model (llama3.2):
uv run chatbot

# Or specify a different model:
uv run chatbot deepseek-r1:1.5b
```

**Features:**
- Real-time token streaming responses.
- Maintains ongoing conversation context/history.
- Type `clear` to reset conversation context.
- Type `exit`, `quit`, or `q` to quit.

---

### Option C: Gradio Web UI ChatBot (`uv run gradio-bot` / Jupyter)

This repository includes a web-based ChatBot interface powered by **Gradio** and **Ollama**:

#### Run from the Terminal:
```bash
# Start Gradio ChatBot with default model (llama3.2):
uv run gradio-bot

# Or run with a different model:
uv run gradio-bot deepseek-r1:1.5b
```
Open your browser at **[http://localhost:7860](http://localhost:7860)**.

#### Run in Jupyter Notebook (`chatbot/ChatBotWithGradio.ipynb`):
Paste the following cell into your notebook:

```python
import gradio as gr
import ollama

def predict(message, history):
    messages = [{"role": "system", "content": "You are a helpful AI assistant."}]
    for turn in history:
        if isinstance(turn, dict):
            messages.append({"role": turn.get("role", "user"), "content": turn.get("content", "")})
        elif isinstance(turn, (list, tuple)) and len(turn) == 2:
            messages.append({"role": "user", "content": turn[0]})
            messages.append({"role": "assistant", "content": turn[1]})
    messages.append({"role": "user", "content": message})

    response = ""
    stream = ollama.chat(model="llama3.2", messages=messages, stream=True)
    for chunk in stream:
        response += chunk["message"]["content"]
        yield response

gr.ChatInterface(fn=predict, title="🦙 Ollama Gradio ChatBot").launch()
```

---

### Option D: Standalone Docker Web UI (Open WebUI)

If you prefer a ChatGPT-like web interface in your browser, launch [Open WebUI](https://github.com/open-webui/open-webui) via Docker:

```bash
docker run -d -p 3000:8080 \
  --add-host=host.docker.internal:host-gateway \
  -v open-webui:/app/backend/data \
  --name open-webui \
  --restart always \
  ghcr.io/open-webui/open-webui:main
```

Open your browser at [http://localhost:3000](http://localhost:3000) to chat with all your local models in a rich web UI.

---

## 🐍 Programmatic Usage in Python

### 1. Install the Python Client
The Ollama SDK is pre-configured in this repository's dependencies (`pyproject.toml`):

```bash
uv add ollama
```

### 2. Configure Environment Variables
Ensure `OLLAMA_BASE_URL` is set in your `.env`:

```env
OLLAMA_BASE_URL=http://localhost:11434
```

### 3. Basic Python Chat Example

```python
import ollama

response = ollama.chat(
    model="llama3.2",
    messages=[
        {"role": "user", "content": "Explain quantum computing in one sentence."}
    ],
)
print(response["message"]["content"])
```

### 4. Streaming Python Chat Example

```python
import ollama

stream = ollama.chat(
    model="llama3.2",
    messages=[{"role": "user", "content": "Tell me a short joke."}],
    stream=True,
)

for chunk in stream:
    print(chunk["message"]["content"], end="", flush=True)
print()
```

> **Tip:** Ollama also provides an OpenAI-compatible API endpoint at `http://localhost:11434/v1`, allowing you to use standard `openai` Python SDK clients with local models by setting `base_url="http://localhost:11434/v1"` and `api_key="ollama"`.

---

# 4. Creating Cloud AI Accounts & API Keys (OpenAI & Anthropic)

While Ollama runs models 100% locally on your machine, you can also compare local outputs with state-of-the-art commercial cloud LLMs like **OpenAI (ChatGPT / GPT-4o)** and **Anthropic (Claude 3.5 Sonnet / Haiku)**.

> [!IMPORTANT]
> **Developer API vs. Web Subscription:**
> A consumer web subscription such as **ChatGPT Plus** ($20/mo) or **Claude Pro** ($20/mo) **does NOT include API access**. 
> Developer APIs are billed separately based on actual token usage (pay-as-you-go). You must add prepaid balance (usually $5 minimum) to your developer account before your API keys will work.

---

## 4.1 OpenAI API Setup (ChatGPT & GPT-4o)

### Step 1: Create an Account
1. Visit the **[OpenAI Developer Platform](https://platform.openai.com/)**.
2. Click **Sign up** or **Log in** with your email, Google, or Microsoft account.

### Step 2: Add Credits / Billing
1. Navigate to **[Settings → Billing](https://platform.openai.com/settings/organization/billing)**.
2. Click **Add payment details** and deposit an initial prepaid credit (e.g. $5 – $10).
3. *(Recommended)* Set an **Auto-recharge** threshold or a monthly **Usage Limit** under **[Limits](https://platform.openai.com/settings/organization/limits)** to avoid accidental overages.

### Step 3: Generate an API Key
1. Go to the **[API Keys Dashboard](https://platform.openai.com/api-keys)**.
2. Click **Create new secret key**.
3. Configure the key:
   - **Name**: e.g., `llm-experiments-dev`
   - **Project**: Select `Default project` (or a dedicated project)
   - **Permissions**: `All` (or restricted if desired)
4. Click **Create secret key**.
5. **Copy the key immediately** (starts with `sk-proj-...` or `sk-...`). You cannot view it again once you close the popup!

### Step 4: Add to Your `.env` File
In your project root, make sure your `.env` file is created:
```bash
cp .env.example .env
```
Open `.env` and set your key:
```env
OPENAI_API_KEY=sk-proj-your_actual_key_here
```

### Step 5: Test with Python
Run a quick test in your terminal to verify connection:
```bash
uv run python -c "
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()
response = client.chat.completions.create(
    model='gpt-4o-mini',
    messages=[{'role': 'user', 'content': 'Hello, say testing 123!'}]
)
print('✅ OpenAI Connected:', response.choices[0].message.content)
"
```

---

## 4.2 Anthropic API Setup (Claude 3.5 Sonnet & Haiku)

### Step 1: Create an Account
1. Visit the **[Anthropic Console](https://console.anthropic.com/)**.
2. Click **Sign up** and register with your email or Google account.
3. Complete phone number verification if prompted (Anthropic uses this for fraud prevention).

### Step 2: Add Credits / Billing
1. Navigate to **[Plans & Billing](https://console.anthropic.com/settings/billing)**.
2. Click **Add Funds** and purchase an initial prepaid credit (minimum $5).
3. *(Recommended)* Configure spend limits under **Spend Limits** to monitor costs.

### Step 3: Generate an API Key
1. Go to the **[API Keys](https://console.anthropic.com/settings/keys)** section.
2. Click **Create Key**.
3. Name your key (e.g. `llm-experiments-dev`).
4. Click **Create Key** and copy your secret key (starts with `sk-ant-api03-...`). Store it securely!

### Step 4: Add to Your `.env` File
Open `.env` and configure:
```env
ANTHROPIC_API_KEY=sk-ant-api03-your_actual_key_here
```

### Step 5: Install & Test Anthropic with Python
1. Add the official `anthropic` SDK to your project:
   ```bash
   uv add anthropic
   ```
2. Verify the connection with a test call:
   ```bash
   uv run python -c "
   import os
   from dotenv import load_dotenv
   import anthropic

   load_dotenv()
   client = anthropic.Anthropic()
   message = client.messages.create(
       model='claude-3-5-haiku-20241022',
       max_tokens=50,
       messages=[{'role': 'user', 'content': 'Hello Claude, say testing 123!'}]
   )
   print('✅ Anthropic Connected:', message.content[0].text)
   "
   ```

---

## 4.3 🛡️ API Key Security & Best Practices

1. **Never commit API keys to Git**:
   - Double-check that `.env` is listed in your `.gitignore` file.
   - Never paste API keys directly into committed code, markdown files, or Jupyter Notebooks.
2. **Set Spend Limits**:
   - Both OpenAI and Anthropic allow setting monthly **hard caps** (API rejects further requests) and **soft caps** (email warnings). Configure these before starting experiments!
3. **Use `.env.example` as a Template**:
   - Keep `.env.example` checked into Git with placeholder values (`OPENAI_API_KEY=`, `ANTHROPIC_API_KEY=`) so other developers know what keys are needed without exposing secrets.
4. **Key Revocation & Rotation**:
   - If an API key is ever leaked or pushed to GitHub, immediately revoke it from the respective developer console and generate a fresh key.



