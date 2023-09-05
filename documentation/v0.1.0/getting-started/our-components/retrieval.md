# 📤 Retrieval

<figure><img src="../../.gitbook/assets/Screenshot from 2023-08-09 17-01-52.png" alt=""><figcaption></figcaption></figure>

The Retrieval class acts as a wrapper that plays a critical role in the post-processing of data retrieved from the Vector database. Once the similarity search is performed in the VectorDB and the relevant results are obtained, the Retrieval class steps in to handle this data and parse it into a context that can be easily consumed by the model.

In the context of Natural Language Processing (NLP) or other machine learning tasks, the retrieved data may consist of embeddings representing text or other forms of structured data. The Retrieval class is responsible for converting these embeddings into a format that the downstream model can understand and process effectively.

This parsing process involves tasks such as converting embeddings into text, numerical values, or any other suitable representations. The parsed data is organized into a context that contains relevant information, which can then be passed as input to the model for further analysis, classification, generation, or any other specific task.

```py
class BaseRetriever(ConfigLoader):
   module_name = "BaseRetriever"
   config_key = RETRIEVER_CONFIG_KEY

   def __init__(self, config: str, vectordb: BaseVectordb = None):
       super().__init__(self.module_name, config)
       self.parse_config(self.config_key, self.required_fields)
       self.vectordb = vectordb

   def retrieve(self, query: Any):
       raise NotImplementedError()

   def get_langchain_retriever(self):
       return self.vectordb.get_langchain_client().as_retriever()

   def get_langchain_memory_retriever(self):
       return self.vectordb.get_langchain_memory_client().as_retriever()
```

**Retriever for Source Data**: The first retriever is created based on the configuration specified in the config file. This retriever is responsible for querying and retrieving data from the Vector database that stores the source data. As mentioned earlier, the Vector database contains the vectorized representations of various data points, such as text embeddings or other structured data. The purpose of this retriever is to perform similarity searches based on user prompts or queries and retrieve relevant data from the source database.

**Retriever for Memory**: The second retriever is specifically designed to store chat history for the ConversationModel. In a conversational context, this retriever maintains a memory of past interactions, including user queries and system responses. The chat history is stored as embeddings or other suitable representations in the Vector database.

Having both retrievers in place enables the system to efficiently handle user queries, retrieve relevant data from the source database, and maintain a conversational context through the memory-based retriever.
