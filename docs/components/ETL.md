# ETL: Extract transform and load

## Data Connector

Data Connector is the main component of LLM stack. Data connectors enable the seamless aggregation of data from multiple sources into one place, typically a data warehouse so that analysis of data can take place with the whole picture in mind.

In our approach, we have implemented a seamless connection between custom data and Word embeddings, accomplished through a Data Loader. This Data Loader efficiently transfers the combined data into a Vector database, optimizing storage and retrieval for further analysis and processing.

Refer the below image for our ETL workflow:

![image](https://github.com/aiplanethub/llmstack/assets/132284203/6049767a-d904-45a6-bb0e-e32a33249261)

The building blocks of the Data loaders are:
**Source data** e.g., CSV file, JSON file, SQL and other databases.
**Pre-trained embeddings** e.g., HuggingFace Embeddings, Sentence transformers and Open AI Embeddings.
**Data loader**: Langchain loader and Llama Hub loader. 
**Destination data** are the Vector Databases e.g., Weaviate, Qdrant and Milvus. 

Currently we support only Weaviate as the destination Vector database. But in the next update we will get to see Qdrant and Milvus implementations. 

Here is custom config.json for the Data loaders. 

```json
{
    "source": {
        "name": "CSVLoader",
        "fields": {
            "file_path": "users.csv"
        }
    },
    "destination": {
        "name": "weaviate",
        "class_name": null,
        "fields": {
            "url": "http://localhost:8002/"
        },
        "embedding": {
            "name": "HuggingFaceEmbeddings",
            "fields": {
                "model_name": "sentence-transformers/all-mpnet-base-v2",
                "model_kwargs": { "device": "cpu" }
            }
        }
    }
}
```
The ``config.json`` file provides customization options, allowing users to specify their data source, which, in this example, could be a ``CSV`` file. Depending on the chosen source, a custom loader needs to be selected to parse the data from that specific format.

Following the parsing step, the data is then converted into ``Vector embeddings``, also known as Word Embeddings. Our system offers support for multiple types of embeddings, including ``HuggingFace Embeddings``, ``Sentence Transformers``, and ``OpenAI embeddings``. It's important to note that adding an embedding object is optional, as some users may already have pre-processed embeddings or prefer to perform this step separately.

The destination for the processed data must be a Vector database. For your convenience, you can utilize the local URL already defined. However, if you prefer to use ``Weaviate Cloud services``, you can update the URL accordingly to match your specific workspace name at the ``Weaviate Cloud`` platform, following the format: "<workspace_name>.weaviate.network". 
