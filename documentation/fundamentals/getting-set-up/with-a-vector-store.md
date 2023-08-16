# 📝 With a Vector Store

In this release, we support for [Weaviate](https://weaviate.io/developers/weaviate) vector store only. Here, we will create a **ChatWithPdf** python application.

#### 🚀 Pre-Requisites

To enhance the LLM Stack's capabilities, you can integrate it with a vector store (Weaviate). Follow these steps:

Before proceeding, ensure you have the following tools installed:

1. [Docker](https://www.docker.com/)
2. [Docker compose](https://docs.docker.com/compose/install/)

#### ![rocket](https://github.githubassets.com/images/icons/emoji/unicode/1f680.png) Installation

We have a read-to-use docker compose file, which we will use for setup of Weaviate vector store here. Referring to the original documentation is preferrable.

**1. Create a `.env` file with the below contents**

````
```bash
PORT=8080
OPENAI_APIKEY=sk-xxx
```
````

Replace sk-xxx with your own `OPENAI_API_KEY`.

* PORT: This variable specifies the port number that your application will use to listen for incoming connections. Applications running on your system communicate through specific ports, much like doors in a building.
* OPENAI\_APIKEY: This variable likely holds your OpenAI API key. An API key is a unique identifier that authenticates your application when interacting with OpenAI's services. It's used to ensure secure and authorized access.

**2. Create a `docker-compose.yaml` file with the below contents and run the command `docker compose up -d`**

The `docker-compose.yaml` file defines a multi-container Docker application. It's used to run your entire application stack, including Weaviate and other necessary services.

````
```yaml
version: "3.4"
services:
weaviate:
    image: semitechnologies/weaviate:1.20.1
    ports:
        - ${PORT}:8080
    restart: always
    environment:
    QUERY_DEFAULTS_LIMIT: 25
    AUTHENTICATION_ANONYMOUS_ACCESS_ENABLED: "true"
    PERSISTENCE_DATA_PATH: "/var/lib/weaviate"
    DEFAULT_VECTORIZER_MODULE: text2vec-openai
    ENABLE_MODULES: text2vec-openai
    OPENAI_APIKEY: ${OPENAI_APIKEY}
    AZURE_APIKEY: ${AZURE_APIKEY}
    CLUSTER_HOSTNAME: "node1"
    volumes:
        - weaviate_data:/var/lib/weaviate

volumes:
weaviate_data:
```
````

**3. Create a `etl.json` and `model.json` files with the following contents.**

The `etl.json` file specifies how data is extracted, transformed, and loaded into your application's vector store (Weaviate).

* ETL: ETL stands for Extract, Transform, Load. It's a process used to gather data from various sources, transform it to fit your needs, and then load it into a database or storage system.
* Source: This section defines the source of data for the ETL process. In your case, you're using a loader named PyPDFLoader to load data from a PDF file.
*   Destination: This section defines where the transformed data will be loaded. The data is loaded into Weaviate, using the class chatpdf and associating it with specific fields.

    **etl.json:**

    ```
    {
        "etl": "langchain",
        "source": {
            "name": "PyPDFLoader",
            "fields": {
                "file_path": "<absolute path to the pdf file>"
            }
        },
        "destination": {
            "name": "weaviate",
            "class_name": "chatpdf",
            "fields": {
                "url": "http://localhost:8002/",
                "text_key": "pdf_content"
            }
        }
    }
    ```

    3.1.1. _etl_ in the above json file is the key used to select a the type of etl loader to use. Currently we support langchain and llamahub loaders.

    3.1.2. _class\_name_ a namespace for the data to store in.

    3.1.3. Key _source_ holds a json to know about the source to load the data from.

    _name_: should the Loaderclass from the required loader you have added above(key `etl`)

    _fields_: should be a nested dictionary with the fields required for the loader.

    _url_: in fields, this should have the value to the weavaite url.

    _text\_key_: A column name in the vector db to store the data in the namespace(class\_name).

    **model.json:**

The `model.json` file configures the components of your LLM stack, including the language model, retriever, and vector database (Weaviate).

````
```json
{
    "model": {
        "name": "gpt3.5",
        "fields": {
            "openai_api_key": "sk-xxxx"
        }
    },
    "retriever": {
        "name": "langchain"
    },
    "vectordb": {
        "name": "weaviate",
        "class_name": "chatpdf",
        "fields": {
            "url": "http://localhost:8002/",
            "text_key": "text"
        }
    }
}
```

Here,

3.2.1. _model_ should hold the value for which model to use.

3.2.2. _retriever_ should hold the value to as to which retriver to use.

_name_: name of the retriever to use. Currently only langchain is supported.

3.2.3. _classname_: Should be similar to what was given in the etl.json

3.2.4. _vectordb_ holds the values to as to which vector db to use. Currently we suport weaviate only and more will be added in the later releases.

_url_: Should be same as the one provided in etl.json.

_text_key_: Should be same as the one provided in etl.json.

**NOTE:** Refer to [components docs](https://github.com/aiplanethub/llmstack/blob/main/docs/components) to know more about the components of llmstack.
````

**4. Run the etl process with command below, which would run the etl process.**

These are the final steps to run your configured ETL process and start the LLM model along with the components you've set up.

**ETL Run**: By running the ETL process (`llmstack etl --config_file etl.json`), you're initiating the extraction, transformation, and loading of data from your defined source to the destination in the vector database.

````
```bash
llmstack etl --config_file etl.json
```
````

**5. Run the model with the command below**

**Start Model**: The final step is to start the LLM model along with its configured components using `llmstack start --config_file ./model.json`.

````
```bash
llmstack start --config_file ./model.json
````
