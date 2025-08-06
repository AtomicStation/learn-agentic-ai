from typing import Annotated
from dotenv import load_dotenv
from langchain_tavily import TavilySearch
from langchain_core.tools import tool
from langchain.chat_models import init_chat_model
from langchain_core.messages import AIMessage, HumanMessage
from typing_extensions import TypedDict

from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition

from langgraph.types import Command, interrupt

import getpass
import os

load_dotenv("../.env", override=True)

if not os.environ.get("TAVILY_API_KEY"):
    # os.environ["TAVILY_API_KEY"] = getpass.getpass("Enter your Tavily API key: ")
    os.environ["TAVILY_API_KEY"] = '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'


llm = init_chat_model("ollama:qwen2.5:32b", temperature=0)

class State(TypedDict):
    messages: Annotated[list, add_messages]

graph_builder = StateGraph(State)

@tool
def human_assistance(query: str) -> str:
    """Request assistance from a human."""
    human_response = interrupt({"query": query})
    return human_response["data"]

tool = TavilySearch(max_results=2)
tools = [tool, human_assistance]
llm_with_tools = llm.bind_tools(tools)

def chatbot(state: State):
    message = llm_with_tools.invoke(state["messages"])
    # Because we will be interrupting during tool execution,
    # we disable parallel tool calling to avoid repeating any
    # tool invocations when we resume.
    assert len(message.tool_calls) <= 1
    return {"messages": [message]}

graph_builder.add_node("chatbot", chatbot)

tool_node = ToolNode(tools=tools)
graph_builder.add_node("tools", tool_node)

graph_builder.add_conditional_edges(
    "chatbot",
    tools_condition,
)
graph_builder.add_edge("tools", "chatbot")
graph_builder.add_edge(START, "chatbot")

memory = MemorySaver()
config = {"configurable": {"thread_id": "1"}}

graph = graph_builder.compile(checkpointer=memory)

# For running in terminal
while True:
    user_input = input("User: ")
    if user_input == "exit":
        break
    else:
        response = graph.stream({
            "messages": [HumanMessage(content=user_input)]
            },
            config=config,
            stream_mode="values",
        )
        print("Bot:", response["messages"][-1].content)