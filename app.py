from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from  langchain_openai import OpenAI

import os
from dotenv import load_dotenv
load_dotenv()

SECRET_KEY = os.getenv("OPENAI_API_KEY")

# # LLM Model

llm = OpenAI(openai_api_key=SECRET_KEY)
response = llm.invoke("Who is the CEO of SAP?")
print(response)



# Chat Model
# chat = ChatOpenAI(openai_api_key=SECRET_KEY)
# # chat.invoke("Who is the CEO of SAP?")
# message = [
#     SystemMessage(content="You are standup commidian"),
#     HumanMessage(content="who is the indian cricket team captain?")
# ]

# response = chat.invoke(message)
# print(response)