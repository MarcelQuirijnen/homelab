from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

setContext = ChatPromptTemplate.from_messages([
    ("system", "You are an expert typescript developer."),
    ("user", "{question}")
])

openAIModel = ChatOpenAI(model="gpt-4o")
parser = StrOutputParser()
notObserved = setContext | openAIModel | parser

question = "What are type annotations?"
response = notObserved.invoke({"question": question})
print(response)
