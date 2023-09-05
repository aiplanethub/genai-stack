---
description: Run an LLM model with few simple steps
---

# 🦄 LLMs

Model is the component that determines which LLM to run. This component is mainly for running LLM models under a http server and access through an API endpoint. Model is for loading the model and its necessary preprocess and postprocess functions to parse the retrieval context and the user prompt properly and give to the model for inference. The response classes can also be customized according to the model’s requirements. GenAI Stack supports things like raw Response (strings or bytes) or JsonResponse. Default is JsonResponse.

LLMStack pre-includes few models for trying out some popular models available out there.

More models will be added in the later releases. We welcome contributions if a model has to be included.

### Supported Models:

1. [OpenAI](openai.md)
2. [GPt4All](gpt4all.md)

### Custom Models

Instructions on how to create a custom model can be found [here](custom-model.md).

