# Minimal RAG simulation with naive keyword search
# No embeddings, no vectors - just the core concept

import os
import requests

# Ollama configuration
OLLAMA_URL = "http://localhost:11434/api/chat"
OLLAMA_MODEL = "qwen3:0.6b"  # adjust to match your exact Ollama model name

# Load knowledge from .txt files in the 'knowledge' subfolder.
# Each file has the document title on the first line and the text on the remaining lines.
# Returns a dict where the key is the title and the value is the text.
def load_knowledge(folder):
    knowledge = {}
    for filename in sorted(os.listdir(folder)):
        if filename.endswith(".txt"):
            filepath = os.path.join(folder, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                lines = f.read().strip().splitlines()
                title = lines[0]
                text = "\n".join(lines[1:]).strip()
                knowledge[title] = text
    return knowledge

KNOWLEDGE_FOLDER = os.path.join(os.path.dirname(__file__), "knowledge")
knowledge = load_knowledge(KNOWLEDGE_FOLDER)

# Step 1: RETRIEVE - Find relevant documents using simple keyword matching
def naive_keyword_search(query, documents, top_k=2):
    query_words = [w for w in query.lower().split() if len(w) >= 4]

    # Score each document by counting keyword matches against the text (dict value)
    scored = []
    for title, text in documents.items():
        doc_words = [w for w in text.lower().split() if len(w) >= 4]
        matches = sum(1 for word in query_words if word in doc_words)
        scored.append({"title": title, "doc": text, "score": matches})

    # Sort by score (highest first) and return top K
    scored.sort(key=lambda x: x["score"], reverse=True)
    return [
        (item["title"], item["doc"])
        for item in scored[:top_k]
        if item["score"] > 0  # Only return documents with matches
    ]

# Step 2: GENERATE - Call the local LLM via Ollama with the query and retrieved context
def generate_answer(query, context):
    # if not context:
    #     return "I don't have enough information to answer that question."

    # Build a prompt that gives the LLM the retrieved context and the user's question
    context_text = "\n".join(f"- {doc}" for doc in context)
    prompt = (
        # f"Use only the context below to answer the question. "
        # f"If the answer is not in the context, say you don't know.\n\n"
        f"Context:\n{context_text}\n\n"
        f"Question: {query}"
    )

    # Call the Ollama chat API
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": OLLAMA_MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "stream": False,
        },
    )
    response.raise_for_status()

    return response.json()["message"]["content"]

# Step 3: RAG Pipeline - Combine retrieval and generation
def rag_pipeline(query):
    print(f"\n📝 Question: {query}")
    print("─────────────────────────────────────")

    # Retrieve relevant documents
    relevant_docs = naive_keyword_search(query, knowledge)
    titles = [title for title, _ in relevant_docs]
    docs = [doc for _, doc in relevant_docs]
    print(f"\n🔍 Retrieved {len(relevant_docs)} relevant document(s): {titles}")

    # Generate answer using retrieved context
    answer = generate_answer(query, docs)
    print(f"\nAnswer:\n{answer}\n")

    return answer

# Example queries
rag_pipeline("What is the current population of Berlin?")
rag_pipeline("What's the weather like in Norway during February?")
rag_pipeline("What languages do Dutch people speak?")
rag_pipeline("Tell me about quantum computing")
rag_pipeline("Tell me about the flying car technology")
rag_pipeline("What is the capital of Spain?")
rag_pipeline("What was the capital of Spain in 2016?")
rag_pipeline("How can I install Python in my Windows laptop?")  # Out of scope of our RAG's knowledge base
