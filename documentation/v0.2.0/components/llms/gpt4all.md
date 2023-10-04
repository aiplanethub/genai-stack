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

**Supported Parameters**

* `model` (str) - Set which model you want to use. Defaults to `orca-mini-3b.ggmlv3.q4_0`
* `model_path` (str) - Give a path where you want to load the model. Default to the current directory.
* `parameters` (Optional\[Gpt4AllParameters]) - An optional instance of the `Gpt4AllParameters` class that contains various configuration parameters for fine-tuning the behavior of the GPT-4All model. Below is the list of all the attributes of `parameters`
  * `backend` (Optional\[str]): The backend to use (optional).
  * `max_tokens` (int): The token context window.
  * `n_parts` (int): The number of parts to split the model into.
  * `seed` (int): The random seed to use.
  * `f16_kv` (bool): Whether to use half-precision for key/value cache.
  * `logits_all` (bool): Whether to return logits for all tokens.
  * `vocab_only` (bool): Whether to load only the vocabulary without weights.
  * `use_mlock` (bool): Force the system to keep the model in RAM.
  * `embedding` (bool): Use embedding mode only.
  * `n_threads` (Optional\[int]): Number of threads to use.
  * `n_predict` (Optional\[int]): The maximum number of tokens to generate.
  * `temp` (Optional\[float]): The temperature for sampling.
  * `top_p` (Optional\[float]): The top-p value for sampling.
  * `top_k` (Optional\[int]): The top-k value for sampling.
  * `echo` (Optional\[bool]): Whether to echo the prompt.
  * `stop` (Optional\[List\[str]]): A list of strings to stop generation when encountered.
  * `repeat_last_n` (Optional\[int]): Last n tokens to penalize.
  * `repeat_penalty` (Optional\[float]): The penalty to apply to repeated tokens.
  * `n_batch` (int): Batch size for prompt processing.
  * `streaming` (bool): Whether to stream the results or not.
  * `allow_download` (bool): Whether to download the model if it does not exist locally.
  * `client` (Any): A client object (optional).

**Running in a Colab/Kaggle/Python scripts(s)**

```python
from genai_stack.model import Gpt4AllModel
from genai_stack.stack.stack import Stack

llm = Gpt4AllModel.from_kwargs()
Stack(model=llm)  # Initialize stack
model_response = llm.predict("How many countries are there in the world?")
print(model_response["output"])
```

* Import the model from `genai_stack.model`
* Instantiate the class with parameters you want to customize
