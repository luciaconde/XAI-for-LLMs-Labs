# From Hallucination to Justification: Hands-On Explainability for LLMs

**Workshop duration (including presentation):** ~2 hours  
**Level:** basic-intermediate Python, familiarity with machine learning is helpful

---

## Workshop overview

This workshop explores **explainability and interpretability** in the context of machine learning and Large Language Models (LLMs). You will move from classic XAI techniques on traditional (black-box) models, through inherently interpretable models, to transparency concerns specific to LLMs: grounded scoped retrieval systems and reasoning transparency through prompting techniques.

---

## Lab structure

| # | Lab | Topic | Time |
|---|-----|-------|------|
| 1 | [lab1-classic-xai](./lab1-classic-xai/) | Classic XAI (SHAP, LIME) on black-box models | ~20 min |
| 2 | [lab2-interpretable-models](./lab2-interpretable-models/) | Interpretable models (transparency by design) | ~15 min |
| 3 | [lab3-rag-scope-detector](./lab3-rag-scope-detector/) | Local RAG system + source attribution, inline citations, and ML scope detector | ~20 min |
| 4 | [lab4-cot-prompts](./lab4-cot-prompts/) | Prompting transparency with Chain-of-Thought | ~15 min |

---

## Prerequisites

### 1. Install Python

You need **Python 3.10 or later**. If you're not sure whether you have it, open a terminal and run:

```bash
python --version
```

If you see `Python 3.10.x` or higher, you're good. Otherwise, install it:

**Windows:**  
Download the installer from [python.org/downloads](https://www.python.org/downloads/) and run it.  
> **Important:** On the first screen of the installer, check **"Add Python to PATH"** before clicking Install. If you miss this, Python commands won't be found in the terminal.

**Mac:**  
The easiest way is via [Homebrew](https://brew.sh/). If you don't have Homebrew yet, install it first:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
Then install Python:
```bash
brew install python
```
Alternatively, download the macOS installer from [python.org/downloads](https://www.python.org/downloads/).

#### Common installation issues

| Problem | Fix |
|---------|-----|
| `python` not found after installing on Windows | You didn't check "Add Python to PATH" — reinstall and check that box, or add Python manually to your PATH environment variable |
| `python` runs the Windows Store on Windows | Open **Settings → Apps → Advanced app execution aliases** and disable the Python aliases there |
| Mac uses system Python 2.x (`python --version` shows 2.x) | Use `python3` instead of `python` in all commands below |
| `pip` not found | Run `python -m pip install --upgrade pip` (or `python3 -m pip ...` on Mac) |

---

### 2. Set up the Python environment

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

**Mac:**
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

> After activation you should see `(.venv)` at the start of your terminal prompt. You need to re-run the `activate` command each time you open a new terminal.

#### Common setup issues

| Problem | Fix |
|---------|-----|
| `python -m venv` fails with "No module named venv" | Run `sudo apt install python3-venv` (Linux) or reinstall Python (Windows/Mac) |
| `.venv\Scripts\activate` gives a permissions error on Windows PowerShell | Run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` once, then retry |
| `pip install -r requirements.txt` fails with dependency conflicts | Make sure you are inside the virtual environment (you should see `(.venv)` in your prompt) |
| Packages install but can't be imported | You may have multiple Python versions; ensure you activated the `.venv` for this project |

---

### 3. Set up Ollama (for Labs 3 and 4)

For Labs 3 and 4, you need to have Ollama installed and the `qwen3:0.6b` model pulled:

To install it on Windows:
```bash
irm https://ollama.com/install.ps1 | iex
```

On Mac:
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

To pull the model (522 MB) and run it:
```bash
ollama pull qwen3:0.6b
ollama run qwen3:0.6b
```

Check that it has been correctly pulled by listing your installed models:
```bash
ollama list
```

---

## Key concepts

| Term | Definition |
|------|-----------|
| **XAI** | Explainable AI (techniques to explain model predictions post-hoc) |
| **IAI** | Interpretable AI (models that are inherently transparent e.g. linear regression, decision tree) |
| **LIME** | Local Interpretable Model-agnostic Explanations (XAI technique) |
| **SHAP** | SHapley Additive exPlanations (feature attribution XAI technique based on game theory) |
| **RAG** | Retrieval-Augmented Generation (grounding LLM answers in documents retrieved by their relevance to the user query) |
| **Scope detector** | A classifier that decides whether a query is within the system's knowledge domain |
| **CoT** | Chain-of-Thought prompting (asking the model to reason step by step e.g. by providing extra guidance or few-shot examples) |
| **ToT** | Tree of Thoughts (extended CoT technique for exploring multiple retractable reasoning branches) |
