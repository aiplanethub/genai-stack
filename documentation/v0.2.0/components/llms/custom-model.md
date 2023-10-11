# Custom Model

Let's create a custom model using a Hugging Face pipeline model for text generation. In this example, we'll use the model from Hugging Face. Please ensure you have the Transformers library installed to run this example.

1. Import Required Modules:

    Import the necessary modules from GenAI Stack and the Transformers library for Hugging Face models.
    
    ```python
    from genai_stack.model.base import BaseModel, BaseModelConfig, BaseModelConfigModel
    from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer
    from pydantic import Field
    ```

2. Create a Config Model:

Create a configuration model to hold the model's configuration parameters. In this example, Gpt2CustomModelConfigModel serves as the base model for our custom configuration.

```python
class HuggingFaceModelConfigModel(BaseModelConfigModel):
    model_name: str = "meta-llama/Llama-2-70b-chat-hf"
    # You can use Field() from pydantic to add any other configuration options you need here.
```

This class is used to define the configuration for your model. In this case, you set the default model name to "meta-llama/Llama-2-70b-chat-hf," but you can add more fields for other configuration options specific to your model.

3. Define a Config Class:

Create a configuration class with a data_model attribute, using BaseModelConfig as the base model.

```python
class HuggingFaceModelConfig(BaseModelConfig):
    data_model = HuggingFaceModelConfigModel
```
This configuration class ties your configuration class (HuggingFaceModelConfigModel) to the base configuration class (BaseModelConfig). It helps manage the configuration of your model.

4. Create the Custom Model Class:

Define the custom model class, inheriting from BaseModel. Set the config_class attribute to link it to the config class created in step 3. Implement the following methods:

* The `load()` method uses the Hugging Face pipeline to load the specified text-generation model, using the model name provided in the configuration. This method is called only once during the class intialization. It should return 
* The `predict()` method takes a prompt as input and generates a response using the loaded Hugging Face model. It returns the generated text as output.

```python
class HuggingFaceModel(BaseModel):
    config_class = HuggingFaceModelConfig

    def load(self):
        self.tokenizer = AutoTokenizer.from_pretrained(self.config.model_name)
        self.model = AutoModelForCausalLM.from_pretrained(self.config.model_name)

    def predict(self, prompt: str):
        input_ids = self.tokenizer.encode(prompt, return_tensors="pt")
        output = self.model.generate(input_ids, max_length=100, num_return_sequences=1)
        response = self.tokenizer.decode(output[0], skip_special_tokens=True)
        return {"output": response}
```
We decode the model's generated output using the tokenizer to obtain the response.


5. Example:

```python
from genai_stack.model import HuggingFaceModel
from genai_stack.stack.stack import Stack

# Override the model by passing the model_name as a dictionary to from_kwargs()
hugging_face_model = HuggingFaceModel.from_kwargs({"model_name": "meta-llama/Llama-2-13b-chat-hf"})
Stack(model=hugging_face_model)  # Initialize stack
model_response = hugging_face_model.predict("How many countries are there in the world?")
print(model_response["output"])
```

By following these steps, you can create a custom model using a Hugging Face model for text generation. You can modify the model name, tokenizer, and generation parameters to suit your specific use case.
