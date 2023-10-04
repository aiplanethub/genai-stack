# OpenAI

### How to configure and use it?

#### Supported Parameters

-   `openai_api_key` (str) - Set an OpenAI key for running the OpenAI Model. (required)
-   `model_name` (str) - Set which model of the OpenAI model you want to use.\
    Defaults to `gpt-3.5-turbo-16k`
-   `temperature` (float) - The sampling temperature for text generation. Defaults to 0.
-   `model_kwargs` (Dict\[str, Any]): Additional model parameters. (optional)
-   `openai_api_base` (Optional\[str]): The base URL path for API requests (optional).
-   `openai_organization` (Optional\[str]): The organization identifier (optional).
-   `openai_proxy` (Optional\[str]): Proxy configuration for OpenAI (optional).
-   `request_timeout` (Optional\[Union\[float, Tuple\[float, float]]]): Timeout for API requests (optional).
-   `max_retries` (int): Maximum number of retries for text generation. Defaults to 6. (optional)
-   `streaming` (bool): Whether to stream results. Defaults to `False`
-   `n` (int): Number of chat completions to generate for each prompt. Defaults to 1.
-   `max_tokens` (Optional\[int]): Maximum number of tokens in the generated response (optional).
-   `tiktoken_model_name` (Optional\[str]): Model name for token counting (optional).

#### Running in a Colab/Kaggle/Python scripts(s)

```python
from genai_stack.model import OpenAIGpt35Model
from genai_stack.stack.stack import Stack

llm = OpenAIGpt35Model.from_kwargs(
    parameters={"openai_api_key": "sk-xxxx"} # Update with your OpenAI Key
)
Stack(model=llm) # Initialize stack
model_response = llm.predict("How long AI has been around.")
print(model_response["output"])
```

1. Import the model from `genai_stack.model`
2. Instantiate the class with `openai_api_key`
3. Call `.predict()` method and pass the query you want the model to answer to.
4. Print the response. As the response is a dictionary, get the `output` only.
    - The response on predict() from the model includes `output`.
