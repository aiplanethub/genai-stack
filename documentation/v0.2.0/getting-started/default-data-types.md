# 📘 Default Data Types

By default, the LLM stack supports the following data types

### Common Imports

```python
from genai_stack.etl.langchain import LangchainETL
from genai_stack.stack.stack import Stack
from genai_stack.vectordb.chromadb import ChromaDB
from genai_stack.etl.utils import get_config_from_source_kwargs
from genai_stack.embedding.utils import get_default_embeddings
```

### CSV

To use CSV as a source, use the data type (the first argument to the `add_source()` method) as `csv`. Eg:

```python
from genai_stack.model import OpenAIGpt35Model

model = OpenAIGpt35Model.from_kwargs(
    parameters={"openai_api_key": "sk-xxxx"} # Update with your OpenAI Key
) 

# Create ETL
etl = LangchainETL.from_kwargs(
    **get_config_from_source_kwargs("csv", "/your/path/to/csv")
)

# Connect the ETL, Embedding and Vectordb component using Stack
stack = Stack(model=model, embedding=get_default_embeddings(), etl=etl, vectordb=ChromaDB.from_kwargs())

etl.run()

model.predict("Your question related to csv")
```

### PDF

To use pdf as a source, use the data type as `pdf`. Eg:

```python
from genai_stack.model import OpenAIGpt35Model

model = OpenAIGpt35Model.from_kwargs(
    parameters={"openai_api_key": "sk-xxxx"} # Update with your OpenAI Key
) 

# Create ETL
etl = LangchainETL.from_kwargs(
    **get_config_from_source_kwargs("pdf", "/your/path/to/pdf")
)

# Connect the ETL, Embedding and Vectordb component using Stack
stack = Stack(model=model, embedding=get_default_embeddings(), etl=etl, vectordb=ChromaDB.from_kwargs())

etl.run()

model.predict("Your question related to pdf")
```

### Web

To use the web as a source, use the data type as `web`.&#x20;

```python
from genai_stack.model import OpenAIGpt35Model

model = OpenAIGpt35Model.from_kwargs(
    parameters={"openai_api_key": "sk-xxxx"} # Update with your OpenAI Key
) 

# Create ETL
etl = LangchainETL.from_kwargs(
    **get_config_from_source_kwargs("web", "valid_web_url")
)

# Connect the ETL, Embedding and Vectordb component using Stack
stack = Stack(model=model, embedding=get_default_embeddings(), etl=etl, vectordb=ChromaDB.from_kwargs())

etl.run()

model.predict("Your question related to web page")
```

### JSON

To use JSON as a source, use the data type as `json`. Eg:

```python
from genai_stack.model import OpenAIGpt35Model

# Create model
model = OpenAIGpt35Model.from_kwargs(
    parameters={"openai_api_key": "sk-xxxx"} # Update with your OpenAI Key
) 

# Create ETL
etl = LangchainETL.from_kwargs(
    **get_config_from_source_kwargs("json", "/your/path/to/json")
)

# Connect the ETL, Embedding and Vectordb component using Stack
stack = Stack(model=model, embedding=get_default_embeddings(), etl=etl, vectordb=ChromaDB.from_kwargs())

etl.run()

model.predict("Your question related to json")
```

### Markdown

To use markdown as a source, use the data type as `markdown`. Eg:

```python
from genai_stack.model import OpenAIGpt35Model

model = OpenAIGpt35Model.from_kwargs(
    parameters={"openai_api_key": "sk-xxxx"} # Update with your OpenAI Key
) 

# Create ETL
etl = LangchainETL.from_kwargs(
    **get_config_from_source_kwargs("markdown", "/your/path/to/markdown or valid url")
)

# Connect the ETL, Embedding and Vectordb component using Stack
stack = Stack(model=model, embedding=get_default_embeddings(), etl=etl, vectordb=ChromaDB.from_kwargs())

etl.run()

model.predict("Your question related to markdown")
```
