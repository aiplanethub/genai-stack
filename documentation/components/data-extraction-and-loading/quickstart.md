# 🔥 Quickstart

We support some 5 loaders out of the box from Langchain ETL they are&#x20;

LangChain provides a set of default document loaders for extracting data from various sources. This document outlines the available default data source types, how to configure them using the provided code, and example usage for each type.

### Default Data Source Types

LangChain supports the following default data source types:

* **CSV**: Comma-separated values file.
* **PDF**: Portable Document Format file.
* **WEB**: Web-based content.
* **JSON**: JSON-formatted file.
* **MARKDOWN**: Markdown-formatted file.

### Configuration and Usage

The provided code includes a class named `FileDataSources`, which defines constants for each default data source type. It also includes a dictionary named `FILE_DATA_SOURCES_MAP`, which maps each data source type to its corresponding loader and default parameter name.

The function `get_config_from_source_kwargs` is provided to generate a configuration based on the data source type and provided source information.

#### Example Usage

Here's how you can use the provided code to configure and use each default data source type:

```
from genai_stack.etl.lang_loader import LangLoaderEtl
from genai_stack.etl.utils import get_config_from_source_kwargs
```

1. **CSV Source Example**:

```python
etl = LangLoaderEtl.from_kwargs(get_config_from_source_kwargs(FileDataSources.CSV, "/path/to/data.csv"))
etl.run()
```

2. **PDF Source Example**:

```python
etl = LangLoaderEtl.from_kwargs(get_config_from_source_kwargs(FileDataSources.PDF, "/path/to/document.pdf"))
etl.run()
```

3. **Web Source Example**:

```python
etl = LangLoaderEtl.from_kwargs(get_config_from_source_kwargs(FileDataSources.WEB, {"web_path": "https://example.com"}))
etl.run()
```

4. **JSON Source Example**:

```python
etl = LangLoaderEtl.from_kwargs(get_config_from_source_kwargs(FileDataSources.JSON, "/path/to/data.json"))
etl.run()
```

5. **Markdown Source Example**:

```python
etl = LangLoaderEtl.from_kwargs(get_config_from_source_kwargs(FileDataSources.MARKDOWN, "/path/to/content.md"))
etl.run()
```

Please note that the examples assume the existence of the `LangLoaderEtl` class and its associated methods, as well as the specific loaders mentioned in the provided code. You may need to adjust the code examples according to your implementation details and the specific functionalities of the loaders.
