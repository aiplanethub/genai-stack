# 🔥 Quickstart

Cache requires a vector database to store the cache. Currently we have support for **Weaviate** and **ChromaDB**. Inorder
to use the cache, you have to provide the vector database component to the stack. The cache component is depended on
other components and it is not used alone.

```py
from genai_stack.llm_cache import LLMCache
from genai_stack.stack.stack import Stack

llm_cache = LLMCache.from_kwargs()

stack = Stack(llm_cache=llm_cache)
```

The llm cache component depends on other stack components and cannot be used alone in a stack. Here is a small example of
llm cache along with its dependent components. Memory and cache cannot co-exist. Memory is given more priority incase both
components are there in the stack.

```py
from genai_stack.stack.stack import Stack
from genai_stack.etl.langchain import LangchainETL
from genai_stack.embedding.langchain import LangchainEmbedding
from genai_stack.prompt_engine.engine import PromptEngine
from genai_stack.model.gpt3_5 import OpenAIGpt35Model
from genai_stack.retriever.langchain import LangChainRetriever
from genai_stack.vectordb import Weaviate
from genai_stack.llm_cache import LLMCache

etl = LangchainETL.from_kwargs(
    name="PyPDFLoader",
    fields={"file_path": "<YOUR_FILE_PATH>"}
)
embedding = LangchainEmbedding.from_kwargs(
    name="HuggingFaceEmbeddings",
    fields={
      "model_name": "sentence-transformers/all-mpnet-base-v2",
      "model_kwargs": {"device": "cpu"},
      "encode_kwargs": {"normalize_embeddings": False},
    }
)
weaviatedb = Weaviate.from_kwargs(
    url="http://localhost:8080/",
    index_name="Testing",
    text_key="test",
    # attributes are used by weaviate as the metadata
    attributes=["source", "page"]
)
llm = OpenAIGpt35Model.from_kwargs(
    parameters={
        "openai_api_key": "<YOUR_OPENAI_API_KEY>",
        "temperature": 0.9,
    }
)
prompt_engine = PromptEngine.from_kwargs(should_validate=False)
llm_cache = LLMCache.from_kwargs()
retriever = LangChainRetriever.from_kwargs()

Stack(
    etl=etl,
    embedding=embedding,
    vectordb=weaviatedb,
    model=llm,
    llm_cache=llm_cache,
    prompt_engine=prompt_engine,
    retriever=retriever,
    memory=None
)

# This will be cached and if the same query is asked again, it will be retrieved from the cache.
retriever.retrieve("What proportion of Medicare Part D enrollees used")

# The response will be retrieved from the cache since it is already cached.
retriever.retrieve("What proportion of Medicare Part D enrollees used")
```
