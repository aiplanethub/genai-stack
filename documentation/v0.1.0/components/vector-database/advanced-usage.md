# 📖 Advanced Usage

### Vectordb Configuration Structure

The vectordb configuration consists of several key components:

<pre class="language-json"><code class="lang-json"><strong>"vectordb": {
</strong>    "name": "vectordb_name",
    "class_name": "entity_class",
    "embedding": {
        "name": "embedding_component_name",
        "fields": {
            "parameter_name": "parameter_value",
            ...
        }
    }
}
</code></pre>

In this configuration:

* `"name"`: Specifies the name of the vectordb.
* `"class_name"`: Specifies the class or type associated with the data stored in the vectordb.
*   `"embedding"` **(Optional):** Contains details about the default embedding component, "HuggingFaceEmbeddings," which is used by default.

    * `"name"`: Specifies the name of the embedding component.
    * `"fields"`: Includes default parameters for the embedding component.&#x20;

