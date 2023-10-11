# Custom Model

Let's create a custom model using a Hugging Face pipeline model for text generation. In this example, we'll use the GPT-2 model from Hugging Face. Please ensure you have the Transformers library installed to run this example.

1. Import Required Modules:

    Import the necessary modules from GenAI Stack and the Transformers library for Hugging Face models.
    
    ```python
    from genai_stack.model.base import BaseModel, BaseModelConfig, BaseModelConfigModel
    from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer
    ```

2. Create a Config Model:

Create a configuration model to hold the model's configuration parameters. In this example, Gpt2CustomModelConfigModel serves as the base model for our custom configuration.

```python
class Gpt2CustomModelConfigModel(BaseModelConfigModel):
    """
    Data Model for the custom model's configuration
    """
    pass
```

3. Define a Config Class:

Create a configuration class with a data_model attribute, using BaseModelConfig as the base model.

```python
class Gpt2CustomModelConfig(BaseModelConfig):
    data_model = Gpt2CustomModelConfigModel
```
4. Create the Custom Model Class:

Define the custom model class, inheriting from BaseModel. Set the config_class attribute to link it to the config class created in step 3. Implement the following methods:

* _post_init(): This method is called during class initialization and loads the model.
* load(): This method loads the Hugging Face GPT-2 model and returns it.
* predict(): This method takes an input prompt and generates a prediction using the model.
* generate(): This method generates text based on the provided prompt and optional generation parameters.

```python
class Gpt2CustomModel(BaseModel):
    config_class = Gpt2CustomModelConfig

    def _post_init(self, *args, **kwargs):
        self.model = self.load()

    def load(self, model_path=None):
        model_name = "gpt2"  # You can change this to any other model name
        model = AutoModelForCausalLM.from_pretrained(model_name)
        return model

    def predict(self, prompt: str):
        response = self.generate(prompt)
        return {"output": response}

    def generate(self, prompt: str, max_length=50, temperature=0.7, top_k=50):
        inputs = self.tokenizer(prompt, return_tensors="pt", padding=True, truncation=True)
        input_ids = inputs["input_ids"]

        response = self.model.generate(
            input_ids,
            max_length=max_length,
            temperature=temperature,
            top_k=top_k,
            num_return_sequences=1,
        )

        generated_text = self.tokenizer.decode(response[0], skip_special_tokens=True)
        return generated_text

    @property
    def tokenizer(self):
        if not hasattr(self, "_tokenizer"):
            self._tokenizer = AutoTokenizer.from_pretrained("gpt2")  # Use the appropriate tokenizer for your model
        return self._tokenizer
```

5. Example:

Here's an example of using the custom GPT-2 model you've created:

Create an instance of the custom model.
Provide a prompt for the model to generate text.
Get the model's prediction and print the generated text.

```python
# Example of using the custom GPT-2 model
if __name__ == "__main__":
    custom_model = Gpt2CustomModel()
    prompt = "Once upon a time, in a land far, far away..."

    prediction = custom_model.predict(prompt)
    print(prediction["output"])
```


By following these steps, you can create a custom model using a Hugging Face GPT-2 model for text generation. You can modify the model name, tokenizer, and generation parameters to suit your specific use case.
