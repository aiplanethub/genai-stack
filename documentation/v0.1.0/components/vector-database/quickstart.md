# 🔥 Quickstart

For quickstart, you can rely on the default embedding option. By default we use "**HuggingFaceEmbedding**" This eliminates the need to configure embeddings, making the process effortless.

To utilize the vectordb configuration with the default embedding:

\=> **Vectordb usage with Retriever**

```python
from genai_stack.vectordb.chroma import ChromaDB
from genai_stack.retriever.langchain import LangChainRetriever
vectordb =  ChromaDB.from_kwargs(class_name = "genai-stack")
retriever = LangChainRetriever.from_kwargs(vectordb = vectordb)
retriever.retrieve("<My question>")

# Output 
# <Source documents nearest to you question>
```

**=> Vectordb usage with ETL**

```python
from genai_stack.vectordb.chroma import ChromaDB
from genai_stack.etl.lang_loader import LangLoaderEtl
from genai_stack.etl.utils import get_config_from_source_kwargs

vectordb =  ChromaDB.from_kwargs(class_name = "genai-stack")
etl = LangLoaderEtl.from_kwargs(vectordb = vectordb, get_config_from_source_kwargs("pdf", "/path/to/pdf"))
etl.run()
```

**Important Note:** A vector db is never used alone its used along with either ETL or Retrieval which gives a good usecase to use the vectordb.&#x20;
