# 📖 Advanced Usage

Embedding functions are rarely used alone.&#x20;

Its used in two way&#x20;

* In **ETL** and Vectordb to convert all the raw data extracted by the ETL into embeddings to be stored in the Vectordb. It also helps in converting the query to embeddings.&#x20;
* In **Retrieval** it converts the user query into an embedding to search against the other data in the vectordb index

### Usage

**Imports:**&#x20;

```python
from genai_stack.etl.langchain import LangchainETL
from genai_stack.stack.stack import Stack
from genai_stack.vectordb.chromadb import ChromaDB
from genai_stack.etl.utils import get_config_from_source_kwargs
from genai_stack.embedding.utils import get_default_embeddings
```

**Configuration:**

```json
config = {
    "name": "HuggingFaceEmbeddings",
    "fields": {
        "model_name": "sentence-transformers/all-mpnet-base-v2",
        "model_kwargs": {"device": "cpu"},
        "encode_kwargs": {"normalize_embeddings": False},
    }
}
```

#### Using with ETL

Once you have defined your configuration as a Python dictionary, you can use it with the `LangchainEmbedding.from_kwargs()` method:

```python
embeddings = LangchainETL.from_kwargs(**config)

etl = LangchainETL.from_config(get_config_from_source_kwargs("pdf", "path/to/pdf"))

# Connect the ETL, Embedding and Vectordb component using Stack
stack = Stack(model=None, embedding=get_default_embeddings(), etl=etl, vectordb=ChromaDB.from_kwargs())

etl.run()
```

**Using with retriever**

```python
# Initialise all your components
etl = LangchainETL.from_kwargs(name="CSVLoader", fields={"file_path": "addresses.csv"})
embedding = LangchainEmbedding.from_kwargs(**config)
chromadb = ChromaDB.from_kwargs()
llm = OpenAIGpt35Model.from_kwargs(parameters={"openai_api_key": "<OPENAI-API-KEY>"})
prompt_engine = PromptEngine.from_kwargs(should_validate=False)
retriever = LangChainRetriever.from_kwargs()
memory = ConversationBufferMemory.from_kwargs()

# Initialise your stack by connecting the components end-to-end
stack = Stack(
    etl=etl,
    embedding=embedding,
    vectordb=chromadb,
    model=llm,
    prompt_engine=prompt_engine,
    retriever=retriever,
    memory=memory
)

# Query to get RAG based results
response = retriever.retrieve("Where does John live?")


```

