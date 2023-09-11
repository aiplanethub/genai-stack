# 📖 Advanced Usage

## General Configuration Structure

The ETL configuration is organized into two primary sections: `source` and `vectordb`.

#### Source Configuration

```json
"source": {
    "name": "source_component_name",
    "fields": {
        "parameter_name": "parameter_value",
        ...
    }
}
```

In this section:

* `"name"`: Specifies the name of the data extraction component to be used.
* `"fields"`: Contains key-value pairs representing the specific parameters required by the data extraction component.

#### Vectordb Configuration

The `vectordb` section defines the vector database where the processed data will be loaded.

```json
"vectordb": {
    "name": "vectordb_name",
    "class_name": "entity_class",
    "fields": {
        "parameter_name": "parameter_value",
        ...
    }
}
```

In this section:

* `"name"`: Specifies the name of the vector database.
* `"class_name"`: Specifies the entity class or type associated with the loaded data.
* `"fields"`: Contains key-value pairs representing the specific parameters needed to connect to the vector database.

**Note:** On further information on how to specify vectordbs please refer the Vector Database doc.

### Usage

### Using Python Dictionary Configuration

You can represent your configuration as a Python dictionary and pass it directly to the `LangLoaderEtl.from_kwargs()` method. This provides a more programmatic and dynamic way of configuring your ETL process.

#### Example Python Dictionary Configuration

Below is an example of how you can define your ETL configuration as a Python dictionary:

```
python
```

```python
config = {
    "source": {
        "name": "CSVLoader",
        "fields": {
            "file_path": "/path/to/data.csv"
        }
    },
    "vectordb": {
        "name": "weaviate",
        "class_name": None,
        "fields": {
            "url": "http://localhost:8002/"
        }
    }
}
```

#### Using Python Dictionary Configuration

Once you have defined your configuration as a Python dictionary, you can use it with the `LangLoaderEtl.from_kwargs()` method:

```
python
```

```python
etl = LangLoaderEtl.from_kwargs(config)
etl.run()
```

### Loading Configuration from JSON File

If you have your configuration defined in a JSON file, you can use the `LangLoaderEtl.from_config()` method to load it. Here's how:

```
python
```

```python
json_file_path = "path/to/your/config.json"
etl = LangLoaderEtl.from_config(json_file_path)
etl.run()
```

### Benefits of Using Python Dictionary Configuration

* **Dynamic Configuration**: Python dictionaries allow you to dynamically generate configurations based on variables and logic.
* **Integration with Code**: You can easily integrate the configuration within your code, making it easier to manage and maintain.

The ETL process begins with data extraction from the specified source using the defined data extraction component. The extracted data may undergo transformation as required. The transformed data is then loaded into the vector database for efficient storage and retrieval using the parameters specified in the `vectordb` section.

For specific details on available data extraction components, their parameters, and the vector database configuration, refer to the respective documentation provided for each component.

***

And now, here's the example JSON configuration you provided integrated into the documentation:

<pre class="language-json"><code class="lang-json"><strong>{
</strong>    "source": {
        "name": "CSVLoader",
        "fields": {
            "file_path": "users.csv"
        }
    },
    "vectordb": {
        "name": "weaviate",
        "class_name": null,
        "fields": {
            "url": "http://localhost:8002/"
        }
    }
}
</code></pre>

Please note that the actual details and parameters within the JSON configuration might vary based on the specific components and vector database being used. Adjust the documentation accordingly to match the functionalities and attributes of those components.

