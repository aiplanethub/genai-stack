# 📦 Chromadb

### Chromadb

This database can give you a quick headstart with the persist option. If you dont specify any arguments a default persistent storage will be used.&#x20;



**Supported Arguments:**

```
host: Optional[str] = None
port: Optional[int] = None
persist_path: Optional[str] = None
search_method: Optional[SearchMethod] = SearchMethod.SIMILARITY_SEARCH
search_options: Optional[dict] = Field(default_factory=dict)
```

**Supported Search Methods:**

* similarity\_search
  * Search Options:
    * **k** : The top k elements for searching&#x20;
* max\_marginal\_relevance\_search
  * Search Options
    * **k**: Number of Documents to return. Defaults to 4.&#x20;
    * **fetch\_k**: Number of Documents to fetch to pass to MMR algorithm.&#x20;
    * **lambda\_mult**: Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

### Usage

A Vectordb definitely needs a embedding function and you connect these two components through a stack.&#x20;

```python
from langchain.docstore.document import Document as LangDocument

from genai_stack.vectordb.chromadb import ChromaDB
from genai_stack.vectordb.weaviate_db import Weaviate
from genai_stack.embedding.utils import get_default_embedding
from genai_stack.stack.stack import Stack


embedding = get_default_embedding()
# Will use default persistent settings for a quick start
chromadb = ChromaDB.from_kwargs()
chroma_stack = Stack(model=None, embedding=embedding, vectordb=chromadb)

# Add your documents
chroma_stack.vectordb.add_documents(
    documents=[
        LangDocument(
            page_content="Some page content explaining something", metadata={"some_metadata": "some_metadata"}
        )
    ]
)
        
# Search for content in your vectordb
chroma_stack.vectordb.search("page")
```

You can also use different search\_methods and search options when trying out more complicated usecases

```python
chromadb = ChromaDB.from_kwargs(
    search_method="max_marginal_relevance_search", 
    search_options={"k": 2, "fetch_k": 10, "lambda_mult": 0.3}
)
```
