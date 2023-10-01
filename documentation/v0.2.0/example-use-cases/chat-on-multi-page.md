## Chat with Webpages

### Installation

```bash
!pip install git+https://github.com/aiplanethub/genai-stack.git
```

## Setup your API Key

```python
import os
from getpass import getpass

api_key = getpass("Enter OpenAI API Key:")
os.environ['OPENAI_API_KEY'] = api_key
```

## Import required modules

```python
from genai_stack.stack.stack import Stack
from genai_stack.etl.langchain import LangchainETL
from genai_stack.embedding.langchain import LangchainEmbedding
from genai_stack.vectordb.chromadb import ChromaDB
from genai_stack.prompt_engine.engine import PromptEngine
from genai_stack.model.gpt3_5 import OpenAIGpt35Model
from genai_stack.retriever.langchain import LangChainRetriever
from genai_stack.memory.langchain import ConversationBufferMemory
```

## ETL -  "Extract, Transform, and Load."

Add your data here. Check documentation for the required loaders

etl = LangchainETL.from_kwargs(name="WebBaseLoader",
                               fields={"web_path": [
                                "https://aiplanet.com",
                                "https://aimarketplace.co"
                               ]
                        }
)

## Create Embeddings to store in VectorDB

```python
config = {
    "model_name": "sentence-transformers/all-mpnet-base-v2",
    "model_kwargs": {"device": "cpu"},
    "encode_kwargs": {"normalize_embeddings": False},
}
embedding = LangchainEmbedding.from_kwargs(name="HuggingFaceEmbeddings", fields=config)
```

## Define the VectorDB and LLM - Large Language Model

```python
chromadb = ChromaDB.from_kwargs()
llm = OpenAIGpt35Model.from_kwargs(parameters={"openai_api_key": api_key})
```


## Add Retrieval and Stack all the components

```python
prompt_engine = PromptEngine.from_kwargs(should_validate=False)
retriever = LangChainRetriever.from_kwargs()
memory = ConversationBufferMemory.from_kwargs()
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

## Run your ETL

```python
etl.run()

prompt1 = "Why choose models from AI Marketplace?"
response = retriever.retrieve(prompt1)
print(response['output'])

prompt2 = "What is the total community members count at AI Planet?"
response = retriever.retrieve(prompt2)
print(response['output'])
```
