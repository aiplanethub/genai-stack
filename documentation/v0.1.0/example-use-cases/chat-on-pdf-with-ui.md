# 📜 Chat on PDF with UI

## How to run the server

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
        "class_name": "genai_stack"
    }
}

```

Run the ETL command:

```
genai-stack etl --config_file etl.json
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
        "class_name": "genai_stack"
    }
}
```

Run the model command

```
genai-stack start --config_file model.json
```

This would start a uvicorn

```
INFO:     Started server process [137717]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8082 (Press CTRL+C to quit)
```

**Important Note:**  The vectordb section should be the same for the etl.json and model.json.&#x20;

**Explanation:** During the ETL process all the data are extracted and stored into the vectordb as embeddings on which we can perform semantic search. So when we are using the model on top of contextual data we need to specify the source of the contextual data.&#x20;

The source of contextual data in our case is the vectordb into which the ETL contents were loaded into . So that's why the vectordb content should be the same for both the model.json and etl.json

## **How to run the UI**

This package is for the chat interface of the LLM stack.

> > **Installation steps**
>
> 1. Clone the repository

```
git clone https://github.com/aiplanethub/genai-stack.git
```

> 2. Create a new virtualenv and activate it(Optional).

```
python -m venv ./genai-stack-ui
source ./genai-stack-ui/bin/activate
```

> 3. Install the requirements

```
pip install -r ui/requirements.txt
```

> 4. Run the streamlit app

```
streamlit run ui/app/main.py
```
