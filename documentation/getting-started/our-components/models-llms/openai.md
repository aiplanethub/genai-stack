# OpenAI

This is a wrapper around `ChatOpenAI` class from Langchain.&#x20;

The model can be connected to  a Vector Store and run predictions based on it to avoid halucinations to some extent.

### How to configure and use it?

#### Pre-Requisite(s)

* `openai_api_key` (required) - Set an OpenAI key for running the OpenAI Model
* `model_name` (optional) - Set which model of the OpenAI model you want to use. \
  Defaults to `gpt-3.5-turbo-16k`&#x20;

#### Running in a Colab/Kaggle/Python scripts(s)

```python
from llm_stack.model import OpenAIGpt35Model

llm  = OpenAIGpt35Model.from_kwargs(fields={"openai_api_key": "sk-xxxx"})  # Update with your OpenAI Key
model_response = llm.predict("How long AI has been around.")
print(model_response["result"])
```

1. Import the model from llmstack
2. Instantiate the class with `openai_api_key`
3. call `.predict()` method and pass the query you want the model to answer to.
4. Print the response. As the response is a dictionary, get the result only.
   * The response on predict() from the model includes _result_ and _source\_documents_.

#### Running the model in a webserver

If you want to run the model in a webserver and interact with it with HTTP requests, the model provides a way to run it.

1. As a Python script

We use FastAPI + Uvicorn to run a model in a webserver.

Set the response class. Default response class is `fastapi.responses.Response`. It can be customized as done in the below code snippet.

```python
from llm_stack.model import OpenAIGpt35Model
from fastapi.responses import JSONResponse

llm  = OpenAIGpt35Model.from_kwargs(fields={"openai_api_key": "sk-xxxx"})
llm.run_http_server(response_class=JSONResponse)
```

A uvicorn server should start as below.

```bash
INFO:     Started server process [137717]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8082 (Press CTRL+C to quit)
```

Making HTTP requests. \
URL - [http://localhost:8082/predict/](http://localhost:8082/predict/)

```python
import requests
response = requests.post("http://localhost:8082/predict/",data="How long AI has been around.")
print(response.text)
```

2. As a CLI

Create a `model.json` file with the following contents:

{% code fullWidth="false" %}
```json
{
    "model": {       
        "name": "gpt3.5",
        "fields": {
            "openai_api_key": "sk-***"
        }

    }
}
```
{% endcode %}

Run the below CLI&#x20;

```bash
llmstack start --config_file model.json
```

```bash
██╗     ██╗     ███╗   ███╗    ███████╗████████╗ █████╗  ██████╗██╗  ██╗
██║     ██║     ████╗ ████║    ██╔════╝╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝
██║     ██║     ██╔████╔██║    ███████╗   ██║   ███████║██║     █████╔╝
██║     ██║     ██║╚██╔╝██║    ╚════██║   ██║   ██╔══██║██║     ██╔═██╗
███████╗███████╗██║ ╚═╝ ██║    ███████║   ██║   ██║  ██║╚██████╗██║  ██╗
╚══════╝╚══════╝╚═╝     ╚═╝    ╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝

INFO:     Started server process [641734]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8082 (Press CTRL+C to quit)
```
