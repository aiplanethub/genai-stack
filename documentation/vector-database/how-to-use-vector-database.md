# How to use Vector Database?

## Quickstart

For quickstart, you can rely on the default embedding option. By default we use "**HuggingFaceEmbedding**" This eliminates the need to configure embeddings, making the process effortless.

To utilize the vectordb configuration with the default embedding:

\=> From Python kwargs

```python
from llm_stack.vectordb.chroma import ChromaDB
from llm_stack.retriever.langchain import LangChainRetriever
vectordb =  ChromaDB.from_kwargs(class_name = "llmstack")
retriever = LangChainRetriever.from_kwargs(vectordb = vectordb)
retriever.retrieve("<My question>")

# Output 
# <Source documents nearest to you question>
```

### Vectordb Configuration Structure

The vectordb configuration consists of several key components:

<pre class="language-json"><code class="lang-json"><strong>"vectordb": {
</strong>    "name": "vectordb_name",
    "class_name": "entity_class",
    "embedding": {
        "name": "embedding_component_name",
        "fields": {
            "parameter_name": "parameter_value",
            ...
        }
    }
}
</code></pre>

In this configuration:

* `"name"`: Specifies the name of the vectordb.
* `"class_name"`: Specifies the class or type associated with the data stored in the vectordb.
* `"embedding"` **(Optional):** Contains details about the default embedding component, "HuggingFaceEmbeddings," which is used by default.
  * `"name"`: Specifies the name of the embedding component.
  * `"fields"`: Includes default parameters for the embedding component.

## Supported Vector Databases

Currently we are supporting two vector databases:&#x20;

* Chromadb&#x20;
* Weaviate&#x20;

### Chromadb

This is the default database used when no vectordb is specified . We create a temp directory and persist the embeddings there using the PersistentClient of Chromadb by default.&#x20;

This is for experimentation purposes when the user wants a quick headstart and wants to experiment with things quickly.&#x20;

**Compulsory arguments:**

* class\_name => The name of the index under which documents are stored

Here are some sample configurations:&#x20;

\=> Chromadb with embedding specification

```
"vectordb": {
    "name": "chromadb",
    "class_name": "llm_stack",
    "embedding": {
        "name": "HuggingFaceEmbeddings",
        "fields": {
            "model_name": "sentence-transformers/all-mpnet-base-v2",
            "model_kwargs": { "device": "cpu" }
        }
    }
}
```

\==> Chromadb without embedding specification. Without any embedding specification we use the default embedding which is HuggingFaceEmbeddings

```
"vectordb": {
    "name": "chromadb",
    "class_name": "llm_stack"
}
```

### Weaviate

In case of weaviate you would have to install weaviate with docker-compose and then use that component in the LLM Stack.

**Compulsory Arguments:**

* class\_name => The name of the index under which documents are stored
* fields:&#x20;
  * url => Url of the weaviate node
  * text\_key => The column against which to do the vector embedding search&#x20;
  *   auth\_config: (Optional)

      * api\_key => api\_key of the weaviate cluster if you are using [weaviate cloud](https://console.weaviate.cloud) .



Prerequisites:

* [docker](https://www.docker.com/)
* [docker-compose](https://docs.docker.com/compose/install/)

Here the docker-compose configurations:&#x20;

* This is a sample docker-compose file&#x20;

```
version: '3.4'
services:
  weaviate:
    image: semitechnologies/weaviate:1.20.5
    restart: on-failure:0
    ports:
     - "8080:8080"
    environment:
      QUERY_DEFAULTS_LIMIT: 20
      AUTHENTICATION_ANONYMOUS_ACCESS_ENABLED: 'true'
      PERSISTENCE_DATA_PATH: '/var/lib/weaviate'
      DEFAULT_VECTORIZER_MODULE: text2vec-transformers
      ENABLE_MODULES: text2vec-transformers
      TRANSFORMERS_INFERENCE_API: http://t2v-transformers:8080
      CLUSTER_HOSTNAME: 'node1'
    volumes:
      - weaviate_data:/var/lib/weaviate
  t2v-transformers:
    image: semitechnologies/transformers-inference:sentence-transformers-multi-qa-MiniLM-L6-cos-v1
    environment:
      ENABLE_CUDA: 0
volumes:
  weaviate_data:
```

This docker compose file uses sentence transformers for embedding for more embeddings and other options [refer this doc.](https://weaviate.io/developers/weaviate/modules/retriever-vectorizer-modules)&#x20;

LLM Stack Configurations for Weaviate:

\=> Sample vectordb configuration for weaviate

```
"vectordb": {
    "name": "weaviate",
    "class_name": "LegalDocs",
    "fields": {
        "url": "http://localhost:9999/",
        "text_key": "clause_text"
    }
}
```

**Note:**  Weaviate expects class\_name in PascalCase otherwise it might lead to weird index not found errors.&#x20;

