# 🦙 LLama Hub

## General Configuration Structure

The ETL configuration is of two main parameters in `source`  "name" and "fields".

The ETL cannot be run alone you have to connect it with the embedding and vectordb to transform the extracted content into searchable embeddings and store it in a reliable format.&#x20;

#### Source Configuration

```json
config = {
  "source": {
    "name": "source_component_name",
    "fields": {
        "parameter_name": "parameter_value",
        ...
    }
  } 
}
```

In this section:

* `"name"`: Specifies the name of the data extraction component to be used.
* `"fields"`: Contains key-value pairs representing the specific parameters required by the data extraction component.&#x20;

More details on the configuration can be found at the official llamahub site here: [https://llamahub.ai/](https://llamahub.ai/)

### Usage

```python
from genai_stack.etl.langchain import LangchainETL
from genai_stack.stack.stack import Stack
from genai_stack.vectordb.chromadb import ChromaDB
from genai_stack.etl.utils import get_config_from_source_kwargs
from genai_stack.embedding.utils import get_default_embeddings
```

### Using Python Dictionary Configuration

You can represent your configuration as a Python dictionary and pass it directly to the `LLamaHubEtl.from_kwargs()` method. This provides a more programmatic and dynamic way of configuring your ETL process.

#### Example Python Dictionary Configuration

Below is an example of how you can define your ETL configuration as a Python dictionary:

```
python
```

```python
config = {
    "name": "PagedCSVReader",
    "fields": {
        "file": "/path/to/data.csv"
    }
}
```

#### Using Python Dictionary Configuration

Once you have defined your configuration as a Python dictionary, you can use it with the LLamaHubEtl`.from_kwargs()` method:

```python
etl = LLamaHubEtl.from_kwargs(config)

# Connect the ETL, Embedding and Vectordb component using Stack
stack = Stack(model=None, embedding=get_default_embeddings(), etl=etl, vectordb=ChromaDB.from_kwargs())

etl.run()
```

### Loading Configuration from JSON File

If you have your configuration defined in a JSON file, you can use the `LLamaHubEtl.from_config()` method to load it. Here's how:

```python
json_file_path = "path/to/your/config.json"
etl = LLamaHubEtl.from_config(json_file_path)

# Connect the ETL, Embedding and Vectordb component using Stack
stack = Stack(model=None, embedding=get_default_embeddings(), etl=etl, vectordb=ChromaDB.from_kwargs())

etl.run()
```

### Benefits of Using Python Dictionary Configuration

* **Dynamic Configuration**: Python dictionaries allow you to dynamically generate configurations based on variables and logic.
* **Integration with Code**: You can easily integrate the configuration within your code, making it easier to manage and maintain.

The ETL process begins with data extraction from the specified source using the defined data extraction component. The extracted data may undergo transformation as required. The transformed data is then loaded into the vector database for efficient storage and retrieval using the parameters specified in the `vectordb` section.

For specific details on available data extraction components, their parameters, and the vector database configuration, refer to the respective documentation provided for each component.

***

And now, here's the example JSON configuration you provided integrated into the documentation:

```json
{
    "name": "PagedCSVReader",
    "fields": {
        "file": "/path/to/data.csv"
    }
}
```

Please note that the actual details and parameters within the JSON configuration might vary based on the specific components and vector database being used. Adjust the documentation accordingly to match the functionalities and attributes of those components.
