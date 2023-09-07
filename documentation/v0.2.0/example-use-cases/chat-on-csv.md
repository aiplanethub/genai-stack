# 💬 Chat on CSV

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

```py
etl = LangchainETL.from_kwargs(name="CSVLoader", fields={"file_path": "/path/sample.csv"})
```

### Embeddings

```py
config = {
    "model_name": "sentence-transformers/all-mpnet-base-v2",
    "model_kwargs": {"device": "cpu"},
    "encode_kwargs": {"normalize_embeddings": False},
}
embedding = LangchainEmbedding.from_kwargs(name="HuggingFaceEmbeddings", fields=config)
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

```py
prompt_engine = PromptEngine.from_kwargs(should_validate=False)
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

`run()` will perform all the steps, Extract, Transform and Load.

```py
etl.run()
```

## Now you can start asking your queries.

```py
response = retriever.retrieve("your query")
print(response)
```
