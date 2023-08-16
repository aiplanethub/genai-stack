# 🪅 Model/LLM

Model is the component that determines which LLM to run. This component is mainly for running LLM models under a http server and access through an API endpoint. Model is for loading the model and its necessary preprocess and postprocess functions to parse the retrieval context and the user prompt properly and give to the model for inference. The response classes can also be customized according to the model’s requirements. LLM Stack supports things like raw Response (strings or bytes) or JsonResponse. Default is JsonResponse.

If a custom model needs to be built, then it can be done by import the base model:

```py
from llm_stack.model import BaseModel

class RandomCustomModel(BaseModel):
    def load(self, model_path: str = None):
        self.model = model.load(model_path)

    def predict(self, query):
        response = self.model.translate(query)
        return {"predictions": response}
```

The model can also configured using `config.json` file:

```json
{
	"model": {
		"name": "gpt3.5",
		"fields": {
			"openai_api_key": "sk-xxxxxxx"
		}
	}, 
	"retriever": {
		"name": "langchain"
	}, 
	"vectordb": {
		"name": "weaviate",
		"class_name": "LegalDocs",
		"fields": {
			"url": "http://localhost:8002/",
			"text_key": "clause_text"
		}
	}
}
```

You can use any LLM model, we provide `gpt4all` as default.
