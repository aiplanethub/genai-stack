# 📦 Weaviate

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

