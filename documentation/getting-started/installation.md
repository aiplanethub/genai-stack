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

```
pip install git+https://github.com/aiplanethub/llmstack.git
```

That's it your local setup is ready. Let's go ahead & test it.

### How to run LLM?

Once the installation is complete you're good to go.

**Note**: Here we will be running just an LLM model without any vector stores. We will cover vector stores in the vector store section.

#### Run in a local environment

1. Create a JSON file with the following contents:

Create a JSON file with the following contents:

```
{
    "model": {
        "name": "gpt4all",
        "fields": {
            "model": "ggml-gpt4all-j-v1.3-groovy"
        }
    }
}
```

In the above code block,

* **Model** is the key LLM stack uses to extract the details of the model to run.
* The **name** should have a value that you will want to run. To check the list of available prebuilt models, run the command `llmstack list-models` from the terminal in the environment where it is installed.
* **fields** hold a nested JSON required for passing to the model as arguments (if any). Since we want to use the _ggml-gpt4all-j-v1.3-groovy_ gpt4all model, we added the value for the model field as _ggml-gpt4all-j-v1.3-groovy_.

**Note**: The nested JSON for fields depends on the model.

Currently, we support the following models:

* [GPT4all](../../assets/gpt4all.json)
* [GPT3](../../assets/gpt3.json)

2. Import the required model(Here we will use the gpt4all model) and initialize it and predict it.

```
from llm_stack.model import Gpt4AllModel
m = Gpt4AllModel(config="llm_stack_config.json") # config should have the path to the config.json file that was created above.
print(m.predict(query="Python program to add two numbers"))
```

If you directly used Python shell you will get the output if you're using a file to execute the file.

```
python3 <file_name.py>
```

````
# Response from the above command

Here's a simple example of how you can use the `add` function in Python. This code will print out the sum of 2 and 3, which is 5. The output looks like this:
```python
2 + 3 = 5
```
````

Now you know how to use the LLM Stack locally.
