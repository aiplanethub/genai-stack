# 📦 Chromadb

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

**Python Usage:**

```
from llm_stack.vectordb.chromadb import ChromaDB

config = {"class_name": "MyIndexName"}
vectordb = ChromaDB.from_kwargs(config)
vectordb.search("Your question")

# Output 
# <Documents closest to your question>
```
