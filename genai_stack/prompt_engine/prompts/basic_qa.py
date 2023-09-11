from langchain import PromptTemplate

template = """
Use the following pieces of context to answer the question enclosed within  3 backticks at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.
Please provide an answer which is factually correct and based on the information retrieved from the vector store.
Please also mention any quotes supporting the answer if any present in the context supplied within two double quotes "" .
{context}

QUESTION:```{query}```
ANSWER:
"""

BASIC_QA = PromptTemplate(template=template, input_variables=["context", "query"])
