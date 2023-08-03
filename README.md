# LLM Stack

This framework is designed to make AI accessible to everyone, including those with a beginner's background in programming. With the power of Large Language Models (LLMs), we aim to democratize AI, enabling companies of all sizes to innovate while maintaining data privacy and security. Let's get started with the basics:

## About

AI Planet is committed to democratizing AI. We provide a secure and private AI framework that seamlessly integrates with your existing IT infrastructure, enabling companies of all sizes to leverage AI's power without compromising data privacy and security.

## Installation

To get started, you need to install the LLM Stack using pip. Open your terminal or command prompt and run the following command:

```bash
pip install git+https://github.com/aiplanethub/llmstack.git
```

We recommend creating a virtual environment before installing the LLM Stack, but it's not mandatory.

## How to run an LLM(without vector store)?

After completing the installation, you are ready to use the LLM Stack. Below are the steps to run an LLM in a Colab/Jupyter Notebook/Python Shell:

### Running in a Colab/Jupyter Notebook/Python Shell

1.  Create a json file with the following contents:

    ```json
    {
        "model": {
            "name": "gpt4all",
            "fields": {
                "model": "ggml-gpt4all-j-v1.3-groovy"
            }
        }
    }
    ```

    **Here,**

    2.1. **model** is the key llmstack uses to extact the details of model to run.

    2.2. **name** should have a value that you will want to run. To check list of available prebuilt model, run the below command from the terminal in the environment where it is installed.

         llmstack list-models

    2.3. **fields** Holds a nested json required for passing to the model as arguements(if any).
    Since we want to use _ggml-gpt4all-j-v1.3-groovy_ gpt4all model, we added the value for the model field as _ggml-gpt4all-j-v1.3-groovy_. If we want to use _orca-mini-3b.ggmlv3.q4_0_, then we can set it as the value.

    **NOTE:** The nested json for fields depends on the model.

2.  Import the required model(Here we will use gpt4all model) and initalize it and predict it.

    ```python
    from llm_stack.model import Gpt4AllModel
    m = Gpt4AllModel(config="llm_stack_config.json") # config should have the path to the config.json file that was created above.
    print(m.predict(query="Python program to add two numbers"))
    ```

    ````python
    # Response from the above commands

    Here's a simple example of how you can use the `add` function in Python. This code will print out the sum of 2 and 3, which is 5. The output looks like this:
    ```python
    2 + 3 = 5
    ```
    ````

### Running the model in terminal with a http server

1. Run the LLM model

    ```bash
    pip install git+https://github.com/aiplanethub/llmstack.git
    ```

2. Test the model using the below Python Script where we will make http request to the model predict endpoint.
    ```python
    import requests
    response = requests.post("http://localhost:8082/predict/",data="Python program to add two numbers.")
    print(response.text)
    ```

## How to run LLM Stack with a Vector Store?

In this release, we support [Weaviate](https://weaviate.io/developers/weaviate) vector store only. More vector store support will be added in upcoming releases.

Here, we will create a **ChatWithPdf** python application as a example.

### Pre-Requisites

Apart from the llmstack package and git, following tools has to be installed:

1. [docker](https://www.docker.com/)
2. [docker compose](https://docs.docker.com/compose/install/)

### Installation

We have a ready-to-use docker compose file, which we will use for setup of Weaviate vector store here. Referring to the original documentation is preferrable.

1.  Create a _.env_ file with the below contents
    ```bash
    PORT=8080
    OPENAI_APIKEY=sk-xxx
    ```
2.  create a _docker-compose.yaml_ file with the below contents

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

3.  Create a _etl.json_ and _model.json_ files with the following contents.

    **etl.json:**

    ```json
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

    3.1.1. _etl_ in the above json file is the key used to select a the type of etl loader to use.
    Currently we support langchain and llamahub loaders.

    3.1.2. _class_name_ a namespace for the data to store in.

    3.1.3. Key _source_ holds a json to know about the source to load the data from.

    _name_: should the Loaderclass from the required loader you have added above(key `etl`)

    _fields_: should be a nested dictionary with the fields required for the loader.

    _url_: in fields, this should have the value to the weavaite url.

    _text_key_: A column name in the vector db to store the data in the namespace(class_name).

    **model.json:**

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

4.  Run the etl process with command below, which would run the etl process.

    ```bash
    llmstack etl --config_file etl.json
    ```

5.  Run the model with the command below,
    ```bash
    llmstack start --config_file ./model.json
    ```

#### Using UI

This package is for the chat interface of the LLM stack.

**Installation steps**

1. Clone the repository

    ```
    git clone https://github.com/aiplanethub/llmstack.git
    ```

2. Create a new virtualenv and activate it(Optional).

    ```
    python -m venv ./llmstack-ui
    source ./llmstack-ui/bin/activate
    ```

3. Install the requirements

    ```
    pip install -r ui/requirements.txt
    ```

4. Run the streamlit app

    ```
    streamlit run ui/app/main.py
    ```
