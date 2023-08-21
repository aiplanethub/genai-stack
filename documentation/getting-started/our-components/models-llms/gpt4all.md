---
layout:
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

# GPT4All

### How to configure and use it? <a href="#how-to-configure-and-use-it" id="how-to-configure-and-use-it"></a>

**Pre-Requisite(s)**

* `model` (optional) - Set which model you want to use. Defaults to `orca-mini-3b.ggmlv3.q4_0`

**Running in a Colab/Kaggle/Python scripts(s)**

```python
from genai_stack.model import Gpt4AllModel

llm = Gpt4AllModel.from_kwargs()
model_response = llm.predict("How many countries are there in the world?")
print(model_response["result"])
```

**Running the model in a webserver**

If you want to run the model in a webserver and interact with it with HTTP requests, the model provides a way to run it.

1. As a Python script

```python
from fastapi.responses import JSONResponse
from genai_stack.model import Gpt4AllModel

llm = Gpt4AllModel.from_kwargs()
llm.run_http_server(response_class=JSONResponse)
```

A server should start as below

```bash
INFO:     Started server process [137717]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8082 (Press CTRL+C to quit)
```

Make HTTP requests. \
URL - [http://localhost:8082/predict/](http://localhost:8082/predict/)

```python
import requests
response = requests.post("http://localhost:8082/predict/", data="How many countries are there in the world?")
print(response.text)
```

2. As a CLI

Create a `model.json` file with the following contents:

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

Run the below command:

```bash
genai-stack start --config_file model.json
```

```bash
 ██████╗ ███████╗███╗   ██╗ █████╗ ██╗    ███████╗████████╗ █████╗  ██████╗██╗  ██╗    
██╔════╝ ██╔════╝████╗  ██║██╔══██╗██║    ██╔════╝╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝    
██║  ███╗█████╗  ██╔██╗ ██║███████║██║    ███████╗   ██║   ███████║██║     █████╔╝     
██║   ██║██╔══╝  ██║╚██╗██║██╔══██║██║    ╚════██║   ██║   ██╔══██║██║     ██╔═██╗     
╚██████╔╝███████╗██║ ╚████║██║  ██║██║    ███████║   ██║   ██║  ██║╚██████╗██║  ██╗    
 ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝    ╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
INFO:     Started server process [641734]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8082 (Press CTRL+C to quit)
```
