from dotenv import load_dotenv
from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, add_messages, END
from langchain_core.messages import AIMessage, HumanMessage
from langgraph.graph import MessagesState
from langchain.chat_models import init_chat_model

load_dotenv("../.env", override=True)
llm = init_chat_model("ollama:qwen2.5:32b", temperature=0)

class BasicChatState(TypedDict):
    messages: Annotated[list, add_messages]

def chatbot(state:BasicChatState):
    return {
        "messages": [llm.invoke(state["messages"])]
    }

graph = StateGraph(BasicChatState)

graph.add_node("chatbot", chatbot)
graph.set_entry_point("chatbot")
graph.add_edge("chatbot", END)

app = graph.compile()

# For running in terminal
while True:
    user_input = input("User: ")
    if user_input == "exit":
        break
    else:
        response = app.invoke({
            "messages": [HumanMessage(content=user_input)]
            })
        print("Bot:", response["messages"][-1].content)