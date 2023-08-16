# 📙 Colab/Kaggle/Notebook

#### Note: Make sure the LLM Stack is installed.&#x20;

#### Running in a Colab/Jupyter Notebook/Python Shell

1.  Create a json file with the following contents:

    One can easily create a json file for the existing LLMs. Currently available models:

    * [GPT4all](../../../assets/gpt4all.json)
    * [GPT3](../../../assets/gpt3.json)

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

    **Here,**

    * **model** is the key llmstack uses to extact the details of model to run.
    * **name** should have a value that you will want to run. To check list of available prebuilt model, run the command `llmstack list-models` from the terminal in the environment where it is installed.
    * **fields** Holds a nested json required for passing to the model as arguements(if any). Since we want to use _ggml-gpt4all-j-v1.3-groovy_ gpt4all model, we added the value for the model field as _ggml-gpt4all-j-v1.3-groovy_. If we want to use _orca-mini-3b.ggmlv3.q4\_0_, then we can set it as the value.

    **NOTE:** The nested json for fields depends on the model.
2.  Import the required model(Here we will use gpt4all model) and initalize it and predict it.

    ```
    from llm_stack.model import Gpt4AllModel
    m = Gpt4AllModel(config="llm_stack_config.json") # config should have the path to the config.json file that was created above.
    print(m.predict(query="Python program to add two numbers"))
    ```

    ````
    # Response from the above commands

    Here's a simple example of how you can use the `add` function in Python. This code will print out the sum of 2 and 3, which is 5. The output looks like this:
    ```python
    2 + 3 = 5
    ```
    ````
