# 💬 Chat on PDF

## Python Implementation

### Importing Components

```py
from genai_stack.stack.stack import Stack
from genai_stack.etl.langchain import LangchainETL
from genai_stack.embedding.langchain import LangchainEmbedding
from genai_stack.vectordb.chromadb import ChromaDB
from genai_stack.prompt_engine.engine import PromptEngine
from genai_stack.model.gpt3_5 import OpenAIGpt35Model
from genai_stack.retriever.langchain import LangChainRetriever
from genai_stack.memory.langchain import ConversationBufferMemory
```

## Initializing Stack Components

### ETL

#### etl.json

```json
{
    "name": "PyPDFLoader",
    "fields": {
        "file_path": "/path/to/sample.pdf"
    }
}
```

```py
etl = LangchainETL.from_config_file(config_file_path="/path/to/etl.json")
```

### Embeddings

#### embeddings.json

```json
{
    "name": "HuggingFaceEmbeddings",
    "fields": {
        "model_name": "sentence-transformers/all-mpnet-base-v2",
        "model_kwargs": { "device": "cpu" },
        "encode_kwargs": { "normalize_embeddings": false }
    }
}
```

```py
embedding = LangchainEmbedding.from_config_file(config_file_path="/path/to/embeddings.json")
```

### VectorDB

```py
chromadb = ChromaDB.from_kwargs()
```

### Model

```py
llm = OpenAIGpt35Model.from_kwargs(parameters={"openai_api_key": "your-api-key"})
```

### Prompt Engine

#### prompt_engine.json

```json
{
    "should_validate": false
}
```

```py
prompt_engine = PromptEngine.from_config_file(config_file_path="/path/to/prompt_engine.json")
```

### Retriever

```py
retriever = LangChainRetriever.from_kwargs()
```

### Memory

```py
memory = ConversationBufferMemory.from_kwargs()
```

## Initializing Stack

### Stack

```py
Stack(
    etl=etl,
    embedding=embedding,
    vectordb=chromadb,
    model=llm,
    prompt_engine=prompt_engine,
    retriever=retriever,
    memory=memory
)
```

## Performing ETL operations

`run()` will execute Extract, Transform and Load operations.

```py
etl.run()
```

## Now you can start asking your queries.

```py
response = retriever.retrieve("your query")
print(response)
```
