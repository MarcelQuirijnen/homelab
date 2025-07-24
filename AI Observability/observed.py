from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from langchain_core.tracers.context import tracing_v2_enabled

setContext = ChatPromptTemplate.from_messages([
    ("system", "You are an expert typescript developer."),
    ("user", "{question}")
])

openAIModel = ChatOpenAI(model="gpt-4o")

# the question can be traced through langsmith UI (langchain.com) - see screendumps
question = "Describe a typical typescript concept that does not work in javascript. Show with an example."
with tracing_v2_enabled():
    openAIModel.invoke(question)
