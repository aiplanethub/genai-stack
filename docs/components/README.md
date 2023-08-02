# LLM Stack

## Motivation

The revolution of Large Language Models has sparked a monumental revolution in the field of AI,  enabling us into a future of boundless possibilities. The global market for AI in enterprise and business is projected to skyrocket to an astonishing $2.8 trillion by the year 2030, ushering in an era of unprecedented growth. As more and more enterprises recognize the transformative potential of AI, they eagerly embrace its power, reshaping industries, and unlocking new frontiers of innovation. This revolution in return brings the risk of Data Privacy. 

Yet, with every disruptive innovation, the uncharted territory presents both thrilling opportunities and puzzling unmet needs. The adoption of AI also conceals unknown risks, daring us to venture forth boldly while ensuring we remain vigilant to identify and mitigate potential pitfalls. The challenge of integrating AI tools seamlessly into existing infrastructures poses a test of adaptability and ingenuity. And, as the digital landscape expands, safeguarding data security becomes more critical. 

## About

At AI Planet, we are changing the narrative by Democratizing AI. We believe this will empower and allow companies of all sizes to innovate, and harness the power of AI without compromising on data privacy and security. We provide secure and private AI on your enterprise IT infrastructure, ensuring seamless integration with your existing systems and processes.

## Installation

Install from a specific branch

```bash
pip install git+https://github.com/aiplanethub/llmstack.git@0.1.0
```

Install from the default branch

```bash
pip install git+https://github.com/aiplanethub/llmstack.git 
```
## How to run LLM Stack in terminal?

Once the installation is completed, you are good to go. Now follow the following steps to run the llmstack model:

### Step-1: Change the directory and create virtual environment

Note: Creating a virtual environment is not necessary but we recommend it. 

```bash
$ cd llmstack
$ virtualenv env
$ source env/bin/activate
```

### Step-2: Install the required libraries. 

```bash
$ pip install .
```

### Step-3: Run the LLM model

```bash
$ llmstack start
```

### Step- 4: Test the model

#### Using Python Script

```python
>>> import requests
>>> response = requests.post("http://localhost:8082/predict/",data="Python program to add two numbers.")
>>> print(response.text)
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
