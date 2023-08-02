import typing

from llm_stack.vectordb.chromadb import ChromaDB
from llm_stack.retriever.langchain import LangChainRetriever


def get_default_vectordb():
    return ChromaDB.from_kwargs(class_name="llmstack")


def get_default_retriever(vectordb: typing.Any = None):
    if not vectordb:
        vectordb = get_default_vectordb()
    print("Vectordb", vectordb)
    return LangChainRetriever.from_kwargs(vectordb=vectordb)
