# 🦜 Langchain

## General Configuration Structure

The Embedding configuration is of two main parameters in `source`  "name" and "fields".

#### Source Configuration

```json
config = {
    "name": "source_component_name",
    "fields": {
        "parameter_name": "parameter_value",
        ...
    }
}
```

In this section:

* `"name"`: Specifies the name of the embedding component to be used.
* `"fields"`: Contains key-value pairs representing the specific parameters required by the embedding component.

### Usage

```python
from genai_stack.embedding.langchain import LangchainEmbedding
from genai_stack.embedding.utils import get_default_embeddings
```

### Using Python Dictionary Configuration

You can represent your configuration as a Python dictionary and pass it directly to the `LangchainEmbedding.from_kwargs()` method. This provides a more programmatic and dynamic way of configuring your ETL process.

#### Example Python Dictionary Configuration

Below is an example of how you can define your ETL configuration as a Python dictionary:

```
python
```

```python
config = {
    "name": "HuggingFaceEmbeddings",
    "fields": {
        "model_name": "sentence-transformers/all-mpnet-base-v2",
        "model_kwargs": {"device": "cpu"},
        "encode_kwargs": {"normalize_embeddings": False},
    }
}
```

#### Using Python Dictionary Configuration

Once you have defined your configuration as a Python dictionary, you can use it with the `LangchainEmbedding.from_kwargs()` method:

```python
embeddings = LangchainETL.from_kwargs(**config)
embdding.embed_text("Text to embed")
```

### Loading Configuration from JSON File

If you have your configuration defined in a JSON file, you can use the `Langchain.from_config()` method to load it. Here's how:

```python
json_file_path = "path/to/your/config.json"
embeddings = LangchainETL.from_kwargs(**config)
embdding.embed_text("Text to embed")
```

### Benefits of Using Python Dictionary Configuration

* **Dynamic Configuration**: Python dictionaries allow you to dynamically generate configurations based on variables and logic.
* **Integration with Code**: You can easily integrate the configuration within your code, making it easier to manage and maintain.

***

And now, here's the example JSON configuration you provided integrated into the documentation:

```json
{
    "name": "HuggingFaceEmbeddings",
    "fields": {
        "model_name": "sentence-transformers/all-mpnet-base-v2",
        "model_kwargs": {"device": "cpu"},
        "encode_kwargs": {"normalize_embeddings": False},
    }
}
```

Please note that the actual details and parameters within the JSON configuration might vary based on the specific components and vector database being used. Adjust the documentation accordingly to match the functionalities and attributes of those components.
