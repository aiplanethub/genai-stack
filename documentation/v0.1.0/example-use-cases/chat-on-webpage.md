# ⚡ Chat on Webpage

## Python Implementation

Since we have a Web page default data loader we can use it directly from [here](../getting-started/default-data-types.md#pdf).&#x20;

```python
from genai_stack.model import OpenAIGpt35Model

model = OpenAIGpt35Model.from_kwargs(
 fields={"openai_api_key": "Paste your Open AI key"}
)
model.add_source("web", "valid_web_url")
model.predict("<Any question on top of the webpage>")
```

## CLI Implementation

etl.json

```
{
    "etl": "langchain",
    "source": {
        "name": "WebBaseLoader",
        "fields": {
            "web_path": "valid_web_url"
        }
    },
    "vectordb": {
        "name": "chromadb",
        "class_name": "genai_stack"
    }
}
```

Run the ETL command

```
genai-stack etl --config_file etl.json
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
        "class_name": "genai_stack"
    }
}
```

Run the model server

```
genai-stack start --config_file model.json
```

You can make predictions on this model server:

```python
import requests

url = "http://127.0.0.1:8082/predict"
res = requests.post(url, data={"query": "<Any question on top of the web page>"})
print(res.content)
```
