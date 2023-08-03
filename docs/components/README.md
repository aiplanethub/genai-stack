# LLM Stack

## Motivation

The revolution of Large Language Models has sparked a monumental revolution in the field of AI, enabling us into a future of boundless possibilities. The global market for AI in enterprise and business is projected to skyrocket to an astonishing $2.8 trillion by the year 2030, ushering in an era of unprecedented growth. As more and more enterprises recognize the transformative potential of AI, they eagerly embrace its power, reshaping industries, and unlocking new frontiers of innovation. This revolution in return brings the risk of Data Privacy.

Yet, with every disruptive innovation, the uncharted territory presents both thrilling opportunities and puzzling unmet needs. The adoption of AI also conceals unknown risks, daring us to venture forth boldly while ensuring we remain vigilant to identify and mitigate potential pitfalls. The challenge of integrating AI tools seamlessly into existing infrastructures poses a test of adaptability and ingenuity. And, as the digital landscape expands, safeguarding data security becomes more critical.

## About

At AI Planet, we are changing the narrative by Democratizing AI. We believe this will empower and allow companies of all sizes to innovate, and harness the power of AI without compromising on data privacy and security. We provide secure and private AI on your enterprise IT infrastructure, ensuring seamless integration with your existing systems and processes.

## Installation

```bash
pip install git+https://github.com/aiplanethub/llmstack.git
```

Note: Creating a virtual environment is not necessary but we recommend it.

## How to run an LLM(without vector store)?

Once the installation is completed, you are good to go.

### Running in a Colab/Jupyter Notebook/Python Shell

1. Create a json file with the following contents:

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

    Here,

    2.1. **model'** is the key llmstack uses to extact the details of model to run.

    2.2. **name** key should have a value that you will want to run. To check list of available prebuilt model, run the command `llmstack list-models` from the terminal in the environment where it is installed.

    2.3. **fields** Holds a nester json required for passing to the model as arguements(if any).
    Since we want to _ggml-gpt4all-j-v1.3-groovy_ gpt4all model, we added the value for the model field as _ggml-gpt4all-j-v1.3-groovy_. If we want to use _orca-mini-3b.ggmlv3.q4_0_, then we can set it as the value.
    The nested json for fields depends on the model.

2. Import the required model(Here we will use gpt4all model) and initalize it and predict it.

    ```python
    from llm_stack.model import Gpt4AllModel
    m = Gpt4AllModel(config="llm_stack_config.json")# config should have the path to the config.json file that was created above.
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

2. Test the model using Python Script where we will make http request to the model predict endpoint.
    ```python
    import requests
    response = requests.post("http://localhost:8082/predict/",data="Python program to add two numbers.")
    print(response.text)
    ```

#### Using UI

This package is for the chat interface of the LLM stack.

**Installation steps**

1. Clone the repository

    ```
    git clone https://github.com/aiplanethub/llmstack.git
    ```

2. Create a new virtualenv and activate it.

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

## How to run LLM Stack in Google Colab or Jupyter Notebook?

In this guide, we demonstrate how to run any LLM model using LLM Stack on Google Colab or Jupyter notebook.

```py
!pip install git+https://github.com/aiplanethub/llmstack.git
!pip install gpt4all
!pip install fastapi langchain openai


from llm_stack.model import BaseModel
from gpt4all import GPT4All
from typing import Any


class GPT4ALLM(BaseModel):
   def load(self, model_path: str = None):
       self.model = GPT4All("ggml-gpt4all-j-v1.3-groovy")


   def predict(self, query: Any):
       #prompt = [{"role": "user", "content": query}]
       output = self.model.generate(query)
       return(output)


custom_model = GPT4ALLM()
response = custom_model.predict("What is the capital of India?")
print(response)
```
