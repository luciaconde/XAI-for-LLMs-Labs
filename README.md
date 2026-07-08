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
| 3 | [lab3-rag-scope-detector](./lab3-rag-scope-detector/) | Local RAG system + ML scope detector | ~20 min |
| 4 | [lab4-cot-prompts](./lab4-cot-prompts/) | Prompting transparency with Chain-of-Thought | ~15 min |

---

## Prerequisites

### Python environment

```bash
pip install -r requirements.txt
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
