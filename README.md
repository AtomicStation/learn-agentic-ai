# RAG Chatbot using LangChain and LangGraph

Creating a chatbot using open source components.

Stack:
- Framework: LangChain, LangGraph, LangSmith
- LLM: Ollama (llama3.1)
- Vector Store: Chroma
- UI: Streamlit
- Memory: SQLite
- Embeddings: bge-small-en or all-MiniLM-L6-v2

## Approach
Development will iterate through:
1. LLM
2. Persistence (chat history/memory)
3. Vector Store (retrieval)
4. UI

## Set up
1. Use a virtual environment
2. Install requirements.txt
3. Create .env file similar to .env-example file