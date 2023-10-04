# Hugging Face&#x20;

## How to configure & use it?

#### Supported parameters

-   `model` (Optional\[str]): The name or identifier of the Hugging Face model to use. This parameter is optional, and its default value is `"nomic-ai/gpt4all-j"`.
-   `model_kwargs` (Optional\[Dict]): Keyword arguments passed to the Hugging Face model (optional).
-   `pipeline_kwargs` (Optional\[dict]): Keyword arguments passed to the Hugging Face pipeline (optional).
-   `task` (str): The task associated with the model. Valid options include `'text2text-generation'`, `'text-generation'`, and `'summarization'`.

**Running in a Colab/Kaggle/Python scripts(s)**\`\`\`python

```python
from genai_stack.model import HuggingFaceModel
from genai_stack.stack.stack import Stack

llm = HuggingFaceModel.from_kwargs()
Stack(model=llm) # Initialize stack
model_response = llm.predict("How many countries are there in the world?")
print(model_response["output"])
```

-   Import the model from `genai_stack.model`
-   Instantiate the class with parameters you want to customize
