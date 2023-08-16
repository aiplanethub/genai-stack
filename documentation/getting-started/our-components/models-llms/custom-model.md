# Custom Model

A custom model can be created with few steps.

1. Import a `BaseModel`class from llmstack.
2. Create a class with desired name(class name) and inherit the `BaseModel`class.
3. Implement two methods:
   *   `load()` - Load  the model. This method is run at once on class instantiation.

       Set a class attribute, which can be later accessed in the predict() method. This way a lot of time can be saved during prediction which avoids model loading during prediction.
   * `predict()`- Accept a parameter named `query`, which should hold the input to the model.\
     Make prediction and return the generated prediction.

#### Example

Below code creates a GPT Neo model with LLM Stack.

```python
from llm_stack.model.base import BaseModel
from transformers import pipeline

class GptNeoModel(BaseModel):
    def load(self, model_path=None):
        # Set `pipeline` by creating a class attribute model i.e, self.model
        self.model = pipeline("text-generation", model="EleutherAI/gpt-neo-2.7B")

    def predict(self, query):
        response = self.model(query, max_length=50, do_sample=True, temperature=0.9)
        return response[0]["generated_text"]
```
