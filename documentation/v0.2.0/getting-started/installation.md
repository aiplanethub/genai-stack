# 🪛 Installation

### Setup environment

#### Create environment

```
python3 -m venv env
```

#### Activate environment

For Mac & Linux

```
source env/bin/activate
```

For Windows(Powershell)

```
env\Scripts\Activate.ps1
```

**Note:** For more information about the Python environment please visit the docs [here](https://docs.python.org/3/library/venv.html#creating-virtual-environments).

### Installation&#x20;

* #### Installation from pypi

  ##### Install latest version

    ```bash
    pip install genai_stack
    ```


  ##### Install a particular version

    ```bash
    pip install genai_stack==0.2.5
    ```

* #### Install from github

    ```
    pip install git+https://github.com/aiplanethub/genai-stack.git
    ```

That's it your local setup is ready. Let's go ahead & test it.

### How to run LLM?

Once the installation is complete you're good to go.

**Note**: Here we will be running just an LLM model without any vector stores. We will cover vector stores in the vector store section.

#### Run in a local environment

Currently, we support the following models:

* [GPT4all](../../assets/gpt4all.json)
* [GPT3](../../assets/gpt3.json)

Import the required model(Here we will use the gpt4all model) and initialize it and predict it.

```python
from genai_stack.model import Gpt4AllModel

llm = Gpt4AllModel.from_kwargs()
model_response = llm.predict("How many countries are there in the world?")
print(model_response["result"])
```

If you directly used Python shell you will get the output if you're using a file to execute the file.

```
python3 <file_name.py>
```

```
# Response from the above command
There are currently 195 recognized independent states in the world.
```

Now you know how to use the GenAI Stack locally.
