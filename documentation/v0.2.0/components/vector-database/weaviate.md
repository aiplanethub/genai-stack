# 📦 Weaviate

### Weaviate:

We recommend this database when you have a more large usecase. You would have to deploy weaviate separately and connect it to our stack to use the running weaviate instance.

We recommend running weaviate without any vectorizer module so that the embedding component is utilized for creating embeddings from your documents.&#x20;

### Installation

Prerequisites:

* [docker](https://www.docker.com/)
* [docker-compose](https://docs.docker.com/compose/install/)

Here the docker-compose configurations:

* This is a sample docker-compose file for installing weaviate without any vectorizer modules.&#x20;

```
version: "3.4"
services:
  weaviate:
    image: semitechnologies/weaviate:1.20.1
    ports:
      - 8080:8080
    restart: on-failure:0
    environment:
      QUERY_DEFAULTS_LIMIT: 25
      AUTHENTICATION_ANONYMOUS_ACCESS_ENABLED: "true"
      PERSISTENCE_DATA_PATH: "/var/lib/weaviate"
      DEFAULT_VECTORIZER_MODULE: "none"
      CLUSTER_HOSTNAME: "node1"
    volumes:
      - weaviate_db:/var/lib/weaviate

volumes:
  weaviate_db:
```

This docker compose file uses sentence transformers for embedding for more embeddings and other options [refer this doc.](https://weaviate.io/developers/weaviate/modules/retriever-vectorizer-modules)

**Supported Arguments:**

```
url: str
text_key: str
index_name: str
auth_client_secret: Optional[AuthCredentials] = None
timeout_config: Optional[tuple] = (10, 60)
additional_headers: Optional[dict] = None
startup_period: Optional[int] = 5
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
weaviatedb = Weaviate.from_kwargs(url="http://localhost:8080/", index_name="Testing", text_key="test")
chroma_stack = Stack(model=None, embedding=embedding, vectordb=weaviatedb)

# Add your documents
weaviate_stack.vectordb.add_documents(
            documents=[
                LangDocument(
                    page_content="Some page content explaining something", metadata={"some_metadata": "some_metadata"}
                )
            ]
        )
        
# Search for your documents
result = weaviate_stack.vectordb.search("page")
print(result)
```

You can also use different search\_methods and search options when trying out more complicated usecases

```python
weavaite_db = Weaviate.from_kwargs(
    url="http://localhost:8080/",
    index_name="Testing",
    text_key="test",
    search_method="max_marginal_relevance_search",
    search_options={"k": 2, "fetch_k": 10, "lambda_mult": 0.3},
)
```

**Note:** Weaviate expects class\_name in PascalCase otherwise it might lead to weird index not found errors.
