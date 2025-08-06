# RAG Chatbot using LangChain and LangGraph

Creating a chatbot using open source components. Repository has been expanded to go through various components and tutorials on how to use LangGraph.

## Repository Map
### 📁 img/
Contains image files used in notebooks and this README.
### 📁 notebooks/
Contains notebooks going through various tutorials and lessons on how to test and apply certain topics.

|Filename|Summary|completed|
| --- | --- | --- |
|agentic_ag_example.ipynb| |✅|
|lanchain_101| |❌|
|langgraph_memory| |❌|
|lg_customized_state| |❌|
|lg_timetravel| |❌|

### 📁 scripts/
Python scripts for interacting with applications through the terminal. Offers real time interaction with the LLMs and agents.

|Filename|Summary|completed|
|---|---|---|
|chatbot_memory| |❌|
|graph_interrupt| |❌|

### Other files
- **.env-example** - Template for setting up the .env file
- **.gitignore** - List of files that are ignored when pushing local to remote repos
- **README.md** - this file!
- **requirements.txt** - List of Python packages required for using the code found in this repo

## Agentic RAG Chatbot
### Stack:
- Framework: LangChain, LangGraph, LangSmith
- LLM: llama3.1:8B and qwen2.5:32b via Ollama
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
3. Create `.env` file similar to `.env-example` file
4. Use the correct kernal for each notebook (Python 3.12 is ideal)