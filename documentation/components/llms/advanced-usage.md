# 📖 Advanced Usage

This showcases on how to use the model along with vectordb and retrieval to make the model converse on top of contextual data

There are two ways we can implement this:

* Python&#x20;
* CLI&#x20;

## Python Implementation:

\==> With default supported ETLs

```python
from llm_stack.model import OpenAIGpt35Model

model = OpenAIGpt35Model.from_kwargs(
 fields={"openai_api_key": "Paste your Open AI key"}
)

# This does the ETL underneath but supports only the default 5 data types
model.add_source("csv", "valid_csv_path_or_url") 

model.predict("<Some question whose answer is could be found in the csv>")
```

For more context on default ETLs check the doc [here](../../getting-started/default-data-types.md).&#x20;

\==> With your own custom ETL, Retriever and Vectordb

```python
from llm_stack.model import OpenAIGpt35Model
from llm_stack.etl import LangLoaderEtl 
from llm_stack.retriever import LangChainRetriever
from llm_stack.vectordb.chromadb import ChromaDB

config = {
  "source": {
        "name": "PyPDFLoader",
        "fields": {
            "file_path": "/your/pdf/path"
        }
    },
}

# Initialise vectordb 
vectordb = ChromaDB.from_kwargs(class_name = "llmstack")

# ETL Process
etl = LangLoaderEtl.from_kwargs(vectordb=vectordb, **config)
etl.run()

# Setup the model and retriever 
retriever = LangChainRetriever.from_kwargs(vectordb = vectordb)
model = OpenAIGpt35Model.from_kwargs(
 retriever = retriever, fields={"openai_api_key": "Paste your Open AI key"}
)

model.predict("<Some question whose answer is could be found in the pdf>")
```

For more context refer to each component's documentation

## CLI  Implementation

You can write a etl.json for the etl process and model.json to perform inference on the extracted data

**etl.json**

```json
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

Run the ETL command:

```
llmstack etl --config_file etl.json
```

**model.json**

```json
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

Run the model command

```
llmstack start --config_file model.json
```

**Important Note:**  The vectordb section should be the same for the etl.json and model.json.&#x20;

**Explanation:** During the ETL process all the data are extracted and stored into the vectordb as embeddings on which we can perform semantic search. So when we are using the model on top of contextual data we need to specify the source of the contextual data.&#x20;

The source of contextual data in our case is the vectordb into which the ETL contents were loaded into . So that's why the vectordb content should be the same for both the model.json and etl.json
