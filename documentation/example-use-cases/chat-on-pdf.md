# 💬 Chat on PDF

## Python Implementation

Since we have a PDF default data loader we can use it directly from [here](../getting-started/default-data-types.md#pdf).&#x20;

```python
from llm_stack.model import OpenAIGpt35Model

model = OpenAIGpt35Model.from_kwargs(
 fields={"openai_api_key": "Paste your Open AI key"}
)
model.add_source("pdf", "valid_pdf_path_or_url")
model.predict("<Any question on top of the pdf>")
```

## CLI Implementation

etl.json

```
{
    "etl": "langchain",
    "source": {
        "name": "PyPDFLoader",
        "fields": {
            "file_path": "/your/pdf/path"
        }
    },
    "vectordb": {
        "name": "chromadb",
        "class_name": "llm_stack"
    }
}
```

Run the ETL command

```
llmstack etl --config_file etl.json
```

model.json

```
{
    "model": {
        "name": "gpt4all"
    },
    "retriever": {
        "name": "langchain"
    },
    "vectordb": {
        "name": "chromadb",
        "class_name": "llm_stack"
    }
}
```

Run the model server

```
llmstack start --config_file model.json
```

You can make predictions on this model server:

```python
import requests

url = "http://127.0.0.1:8082/predict"
res = requests.post(url, data={"query": "<Any question on top of the pdf>"})
print(res.content)
```
