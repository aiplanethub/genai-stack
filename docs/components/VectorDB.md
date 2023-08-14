# VectorDB

The vector database is a new type of database that is becoming popular in the world of ML and AI. Vector databases are different from traditional relational databases, like PostgreSQL, which was originally designed to store tabular data in rows and columns. They’re also decidedly different from newer NoSQL databases, such as MongoDB, which store data in JSON documents. 

Utilizing the Vector database offers significant advantages, simplifying the process of performing similarity searches in Word embeddings. Within the VectorDB, there exists a key method known as search. This function takes a string, which typically represents a prompt from the user, and leverages vector similarity search techniques to retrieve relevant data from the database.

```py
class BaseVectordb(ConfigLoader):
    module_name = "VectorDB"
    config_key = VECTORDB_CONFIG_KEY

    def __init__(self, config: dict) -> None:
        """
        A wrapper around the weaviate-client and langchain's weaviate class

        Args:
            config: Pass the parsed config file into this class
        """
        super().__init__(name=self.module_name, config=config)
        self.parse_config(self.config_key, self.required_fields)

    def search(self, query: str) -> List[Document]:
        raise NotImplementedError()
```
In our approach, VectorDB serves a dual purpose. Firstly, it facilitates efficient similarity searches, allowing us to find data points with embeddings that closely match the provided input. This functionality is crucial for tasks such as semantic similarity, recommendation systems, and clustering.

Secondly, the VectorDB acts as a reliable memory storage system. It securely stores the vectorized data, to store the chat history.

```py
def _setup_vectordb_memory(self, client: weaviate.Client):
    """
    Get or Create a vectordb index
    """
    try:
        client.schema.get(class_name=MEMORY_INDEX_NAME)
    except UnexpectedStatusCodeException:
        print("Creating memory index class in vector db")
        client.schema.create_class(
        {
            "class": MEMORY_INDEX_NAME,
            "properties": [
                {"name": MEMORY_TEXT_KEY, "dataType": ["text"]},
            ],
        }
    )
```

## ChromaDB integration

LLM stack furthermore supports ChromaDB VectorDB that helps to store embeddings in memory and search.

```python
class ChromaDB(BaseVectordb):
    required_fields = ["class_name"]

    def _get_persistent_path(self):
        return os.path.join(tempfile.gettempdir(), "llmstack")

    def create_client(self):
        return PersistentClient(
            path=self.vectordb_config_fields.get("persistent_file_path") or self._get_persistent_path()
        )

    def get_langchain_client(self):
        return LangchainChroma(
            collection_name=self.vectordb_config.get("class_name"),
            client=self.create_client(),
            embedding_function=self.get_embedding(),
        )

    def search(self, query: str) -> typing.List[Document]:
        langchain_faiss_client = self.get_langchain_client()
        return langchain_faiss_client.similarity_search(query)

    def get_langchain_memory_client(self):
        return LangchainChroma(
            collection_name=MEMORY_INDEX_NAME, client=self.create_client(), embedding_function=self.get_embedding()
        )
```

Currently LLM Stack supports only ChromaDB and Weaviate for the Vector Database. In the coming few days, we will also integrate Milvus and Qdrant. 

Once the similarity search is performed within the VectorDB, the retrieved data is passed on to the Retrieval class. The Retrieval class is responsible for further processing and presenting the results to the user.
