# LLM Stack

An End to End LLM Framework

## Motivation

The revolution of Large Language Models has sparked a monumental revolution in the field of AI, enabling us into a future of boundless possibilities. The global market for AI in enterprise and business is projected to skyrocket to an astonishing $2.8 trillion by the year 2030, ushering in an era of unprecedented growth. As more and more enterprises recognize the transformative potential of AI, they eagerly embrace its power, reshaping industries, and unlocking new frontiers of innovation. This revolution in return brings the risk of Data Privacy.

Yet, with every disruptive innovation, the uncharted territory presents both thrilling opportunities and puzzling unmet needs. The adoption of AI also conceals unknown risks, daring us to venture forth boldly while ensuring we remain vigilant to identify and mitigate potential pitfalls. The challenge of integrating AI tools seamlessly into existing infrastructures poses a test of adaptability and ingenuity. And, as the digital landscape expands, safeguarding data security becomes more critical.

## About

At AI Planet, we are changing the narrative by Democratizing AI. We believe this will empower and allow companies of all sizes to innovate, and harness the power of AI without compromising on data privacy and security. We provide secure and private AI on your enterprise IT infrastructure, ensuring seamless integration with your existing systems and processes.

## Setup environment

### Create python environment

```bash
python3 -m venv env
```

### Activate environment

**For mac & Linux**

```bash
source env/bin/activate
```

**For windows (PowerShell)**

```bash
env\Scripts\Activate.ps1
```

**Note**: For more information about python environmet please visit the docs [here](https://docs.python.org/3/library/venv.html#creating-virtual-environments).

## Installation

```bash
pip install git+https://github.com/aiplanethub/llmstack.git
```

## How to run an LLM?

Once the installation is completed, you are good to go.

Note: Here we will be running just an LLM Model without any vector stores. We will cover it later below.

### 🚀 Running in a Colab/Jupyter Notebook/Python Shell

1. Create a json file with the following contents:

    One can easily create a json file for the existing LLMs. Currently available models:

    - [GPT4all](https://github.com/aiplanethub/llmstack/blob/main/assets/gpt4all.json)
    - [GPT3](https://github.com/aiplanethub/llmstack/blob/main/assets/gpt3.json)

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

    - **model** is the key llmstack uses to extact the details of model to run.

    - **name** should have a value that you will want to run. To check list of available prebuilt model, run the command `llmstack list-models` from the terminal in the environment where it is installed.

    - **fields** Holds a nested json required for passing to the model as arguements(if any).
      Since we want to use _ggml-gpt4all-j-v1.3-groovy_ gpt4all model, we added the value for the model field as _ggml-gpt4all-j-v1.3-groovy_. If we want to use _orca-mini-3b.ggmlv3.q4_0_, then we can set it as the value.

    **NOTE:** The nested json for fields depends on the model.

2. Import the required model(Here we will use gpt4all model) and initalize it and predict it.

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

### 🚀 Running the model in terminal with a http server

1. Run the LLM model

    ```bash
    llmstack start --config_file llm_stack_config.json
    ```

2. Now you should see a response like below.

    ```bash
    ██╗     ██╗     ███╗   ███╗    ███████╗████████╗ █████╗  ██████╗██╗  ██╗
    ██║     ██║     ████╗ ████║    ██╔════╝╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝
    ██║     ██║     ██╔████╔██║    ███████╗   ██║   ███████║██║     █████╔╝
    ██║     ██║     ██║╚██╔╝██║    ╚════██║   ██║   ██╔══██║██║     ██╔═██╗
    ███████╗███████╗██║ ╚═╝ ██║    ███████║   ██║   ██║  ██║╚██████╗██║  ██╗
    ╚══════╝╚══════╝╚═╝     ╚═╝    ╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝

    Failed to get VectorDB
    Failed to get Retriever
    INFO:     Started server process [641734]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.
    INFO:     Uvicorn running on http://127.0.0.1:8082 (Press CTRL+C to quit)
    ```

    Let the server run. Now open a new terminal or a code editor and enter the below python script.

3. Test the model using the below Python Script where we will make http request to the model predict endpoint.
    ```python
    import requests
    response = requests.post("http://localhost:8082/predict/",data="Python program to add two numbers.")
    print(response.text)
    ```

## How to run LLM Stack with a Vector Store?

In this release, we support for [Weaviate](https://weaviate.io/developers/weaviate) vector store only.
Here, we will create a **ChatWithPdf** python application.

### 🚀 Pre-Requisites

Apart from the llmstack package and git, following tools has to be installed:

1. [docker](https://www.docker.com/)
2. [docker compose](https://docs.docker.com/compose/install/)

### 🚀 Installation

We have a read-to-use docker compose file, which we will use for setup of Weaviate vector store here. Referring to the original documentation is preferrable.

1.  Create a `.env` file with the below contents

    ```bash
    PORT=8080
    OPENAI_APIKEY=sk-xxx
    ```

2.  Create a `docker-compose.yaml` file with the below contents and run the command `docker compose up -d`

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

3.  Create a `etl.json` and `model.json` files with the following contents.

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

### 🚀 Using UI

This package is for the chat interface of the LLM stack.

> > **Installation steps**
>
> 1. Clone the repository

    git clone https://github.com/aiplanethub/llmstack.git

> 2. Create a new virtualenv and activate it(Optional).

    python -m venv ./llmstack-ui
    source ./llmstack-ui/bin/activate

> 3. Install the requirements

    pip install -r ui/requirements.txt

> 4. Run the streamlit app

    streamlit run ui/app/main.py

## Components:

LLM Stack has two main components level abstraction:

### ETL

![image](https://github.com/aiplanethub/llmstack/assets/132284203/6049767a-d904-45a6-bb0e-e32a33249261)

### Retrival/Model

![image](https://github.com/jaintarunAI/llmstack/assets/132284203/7406dfa0-5290-4c39-be8c-599d3627cab1)

Check the components for detailed explaination on the components:

-   [ETL](https://github.com/aiplanethub/llmstack/blob/main/docs/components/ETL.md)
-   [VectorDB](https://github.com/aiplanethub/llmstack/blob/main/docs/components/VectorDB.md)
-   [Retrieval](https://github.com/aiplanethub/llmstack/blob/main/docs/components/Retreiver.md)
-   [Model](https://github.com/aiplanethub/llmstack/blob/main/docs/components/Model.md)
