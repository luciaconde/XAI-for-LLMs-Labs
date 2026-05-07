# Minimal RAG simulation with naive keyword search
# No embeddings, no vectors - just the core concept

# Our "knowledge base" - a collection of facts
knowledge = [
    "Underwhelming Spatula is a kitchen tool that redefines expectations by fusing whimsy with functionality.",
    "Lisa Melton wrote Dubious Parenting Tips.",
    "The Almost-Perfect Investment Guide is 210 pages long.",
    "Quantum computing uses qubits instead of classical bits.",
    "The capital of France is Paris."
]

# Step 1: RETRIEVE - Find relevant documents using simple keyword matching
def naive_keyword_search(query, documents, top_k=2):
    query_words = query.lower().split()

    # Score each document by counting keyword matches
    scored = []
    for doc in documents:
        doc_words = doc.lower().split()
        matches = sum(1 for word in query_words if word in doc_words)
        scored.append({"doc": doc, "score": matches})

    # Sort by score (highest first) and return top K
    scored.sort(key=lambda x: x["score"], reverse=True)
    return [
        item["doc"]
        for item in scored[:top_k]
        if item["score"] > 0  # Only return documents with matches
    ]

# Step 2: GENERATE - Create answer using retrieved context (simulated)
def generate_answer(query, context):
    if not context:
        return "I don't have enough information to answer that question."

    # In a real RAG system, this would call an LLM with the context
    # For now, we just return the most relevant context
    return "Based on the available information:\n\n" + "\n\n".join(context)

# Step 3: RAG Pipeline - Combine retrieval and generation
def rag_pipeline(query):
    print(f"\n📝 Question: {query}")
    print("─────────────────────────────────────")

    # Retrieve relevant documents
    relevant_docs = naive_keyword_search(query, knowledge)
    print(f"\n🔍 Retrieved {len(relevant_docs)} relevant document(s)")

    # Generate answer using retrieved context
    answer = generate_answer(query, relevant_docs)
    print(f"\nAnswer:\n{answer}\n")

    return answer

# Example queries
print("=" * 50)
print("   MINIMAL RAG WITH NAIVE KEYWORD SEARCH")
print("=" * 50)

rag_pipeline("What is Underwhelming Spatula?")
rag_pipeline("Who wrote Dubious Parenting Tips?")
rag_pipeline("How many pages is the investment guide?")
rag_pipeline("Tell me about quantum computing")
rag_pipeline("What is the weather today?")  # No relevant context
