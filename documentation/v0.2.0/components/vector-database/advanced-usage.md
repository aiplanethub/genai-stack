# 📖 Advanced Usage

**Search Options:**

You can use different search options for different types of retrieval methods in any vectordb component given by genai stack.&#x20;

\==> Weaviate db

```python
from genai_stack.vectordb.weaviate_db import Weaviate

weavaite_db = Weaviate.from_kwargs(
    url="http://localhost:8080/",
    index_name="Testing",
    text_key="test",
    search_method="max_marginal_relevance_search",
    search_options={"k": 2, "fetch_k": 10, "lambda_mult": 0.3},
)
```

\==> Chromadb&#x20;

```python
from genai_stack.vectordb.chromadb import ChromaDB

chromadb = ChromaDB.from_kwargs(
    search_method="max_marginal_relevance_search", 
    search_options={"k": 2, "fetch_k": 10, "lambda_mult": 0.3}
)
```
