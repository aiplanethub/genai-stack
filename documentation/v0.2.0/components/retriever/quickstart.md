# 🔥 Quickstart

Currently we have support only for **LangChain Retriever**.

LangChainRetriever doesn't require any specific configuration from user

```py
from genai_stack.retriever import LangChainRetriever

retriever = LangChainRetriever(config={})

response = retriever.retrieve(query)
```

**Important Note**: A Retriever component is never used alone because it is depended on prompt engine, model and atleast any one of these two components vectordb or memory.

You can look more into prompt engine component to know why do you have to provide atleast any one of the component vectordb or memory. In short, The prompt engine component decides which prompt template to be used based on the availability of components.

Here is a small example of retriever along with its dependent components.

```py
from genai_stack.stack.stack import Stack
from genai_stack.prompt_engine.engine import PromptEngine
from genai_stack.model import OpenAIGpt35Model
from genai_stack.memory import ConversationBufferMemory
from genai_stack.retriever import LangChainRetriever

promptengine = PromptEngine.from_kwargs(should_validate = False)
model = OpenAIGpt35Model.from_kwargs(parameters={"openai_api_key": openai_api_key})
memory = ConversationBufferMemory(config={})
retriever = LangChainRetriever(config={})
Stack(model=model, prompt_engine=promptengine, retriever=retriever, memory=memory)

response = retriever.retrieve("Your query")
```
