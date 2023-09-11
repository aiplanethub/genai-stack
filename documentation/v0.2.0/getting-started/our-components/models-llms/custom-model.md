# Custom Model

A custom model can be created with a few steps.

1. Import a `BaseModel`, `BaseModelConfig`, `BaseModelConfigModel`class from `genai-stack.model.base`.
2. Create a config model that will have all the parameters that the model expects. Use `BaseModelConfigModel` as the base model.
3. Create a config class having `data_model` as attribute & use `BaseModelConfig` as base model
4. Create a class with the desired name(class name) and inherit the `BaseModel`class.
5. Add `config_class` As an attribute, its value is the config class that you created in the 3rd step. With this, you can now access the parameters that you added in 2nd step in class methods as `self.config.<parameter_name>`&#x20;
6. Implement three methods:
   * `_post_init()` - Call `load` method as `self.model = self.load()` .
   *   `load()` - Load the model. This method is run at once on class instantiation in `_post_init` method.

       Set a class attribute, which can be later accessed in the predict() method. This way a lot of time can be saved during prediction which avoids model loading during prediction. Make sure to return the model so that we can access it in other methods as we're setting the `self.model`attribute in `_post_init` method.
   * `predict()`- Accept a parameter named `prompt`, which should hold the input to the model.\
     Make a prediction and return the generated prediction as `dict` having `output` a key that holds the prediction value.

#### Example

The below code creates a GPT Neo model with GenAI Stack.

```python
from genai_stack.model.base import BaseModel, BaseModelConfig, BaseModelConfigModel
from transformers import pipeline

class GptNeoModelConfigModel(BaseModelConfigModel):
    """
    Data Model for the configs
    """
    pass
    
class GptNeoModelConfig(BaseModelConfig):
    data_model = GptNeoModelConfigModel

class GptNeoModel(BaseModel):
    config_class = GptNeoModelConfig

    def _post_init(self, *args, **kwargs):
        self.model = self.load()
        
    def load(self, model_path=None):
        model = pipeline("text-generation", model="EleutherAI/gpt-neo-2.7B")
        return model

    def predict(self, prompt: str):
        response = self.model(prompt, max_length=50, do_sample=True, temperature=0.9)
        return {"output": response[0]["generated_text"]}
```
