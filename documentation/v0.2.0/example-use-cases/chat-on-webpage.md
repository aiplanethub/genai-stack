# ⚡ Chat on Webpage

## Installation

```bash
pip install git+https://github.com/aiplanethub/genai-stack.git
```

Since we have a Web page default data loader we can use it directly from [here](../getting-started/default-data-types.md#pdf).&#x20;

## Import the required components:

Few of the major components include:
- ETL
- VectorDB
- Retriever
- LLM Model - GPT3.5 (OpenAI)
- Memory

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

## Setup OpenAI Key

```py
import os
from getpass import getpass

#once you run the code block, you are expected to enter your API Key
api_key = getpass()
os.environ['OPENAI_API_KEY'] = api_key
```

## ETL

Since we working with the Web page, the field name is **web_path** and loader name is **WebBaseLoader**

```py
your_web_page_url = "https://aimarketplace.co/"
etl = LangchainETL.from_kwargs(name="WebBaseLoader", fields={"web_path": your_web_page_url})
```
## Config embeddings and Model Name

We will use HuggingFaceEmbeddings along with Sentence Transformers

```py
config = {
    "model_name": "sentence-transformers/all-mpnet-base-v2",
    "model_kwargs": {"device": "cpu"},
    "encode_kwargs": {"normalize_embeddings": False},
}
embedding = LangchainEmbedding.from_kwargs(name="HuggingFaceEmbeddings", fields=config)
```

## VectorDB - ChromaDB

```py
chromadb = ChromaDB.from_kwargs()
```

## LLM - OpenAI GPT3.5

```py
llm = OpenAIGpt35Model.from_kwargs(parameters={"openai_api_key": api_key})
```

## Setup Prompt Engine, Retrieval and Memory

```py
prompt_engine = PromptEngine.from_kwargs(should_validate=False)
retriever = LangChainRetriever.from_kwargs()
memory = ConversationBufferMemory.from_kwargs()
```

## Stack up all the important components

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

run() will execute Extract, Transform and Load operations.

```py
etl.run()
```

## Play around with the predictions

Chat with the Web Page now, by replacing with your prompt

```py
prompt = "What are the benefits of AI Marketplace"
response = retriever.retrieve(prompt)
print(response['output'])
```

### Output

```bash
The benefits of AI Marketplace include:

1. Ready-to-Use Models: AI Marketplace offers pre-trained AI models that can accelerate innovation and simplify integration across diverse applications.

2. Data Security: AI Marketplace provides advanced data security solutions, ensuring the secure handling of your data.

3. Accelerated Time to Market: By leveraging AI models from the marketplace, you can experience faster time to market and stay ahead of the competition.

4. Large Collection of Models: AI Marketplace offers a diverse range of AI models for different industries and use cases.

5. Cost Saving: AI Marketplace provides efficient AI solutions with pre-built models, eliminating the need for a data science team. Additionally, it offers flexible scaling and pay-as-you-go pricing.

6. Business-focused Models: AI Marketplace offers powerful AI models that can optimize operations and drive growth for businesses.

These benefits are mentioned in the context: "Why choose AI Marketplace?"
```
