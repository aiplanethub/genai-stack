# 🔥 Quickstart

**ConversationBufferMemory**

A Conversation Buffer Memory component temporarily stores recent messages and interactions in a conversation. It acts as a short-term memory buffer, holding onto messages for a brief period to facilitate real-time conversations. This component help in maintaining a sense of continuity and context within the conversation.

Conversation Buffer Memory doesn't require any specific configuration from the user.

```py
from genai_stack.stack.stack import Stack
from genai_stack.model import OpenAIGpt35Model
from genai_stack.memory import ConversationBufferMemory

model = OpenAIGpt35Model.from_kwargs(parameters={"openai_api_key": "<ADD_OPENAI_KEY>"})
memory = ConversationBufferMemory.from_kwargs()

stack = Stack(
    model=model
    memory=memory
)

# Storing few conversation
memory.add_text(user_text="Hi my name is Jhon",model_text="Hello, Jhon! How can I assist you today?")
memory.add_text(user_text="Which is the smallest month of the year?",model_text="The smallest month of the year is February")
memory.add_text(user_text="What is my name?",model_text="Your name is Jhon.")

memory.get_chat_history()
```

**Important Note**: The ConversationBufferMemory uses the main memory of the system to store the conversations and it will be lost once the process gets terminated.

**VectorDBMemory**

VectorDBMemory supports both `ChromaDB` and `Weaviate`, which one is used to store the conversations is totally depends on the vectordb that is initialized and passed to the stack for storing the documents. by default `k=4`, so `get_chat_history()` returns last 4 conversations and you can also change this default value when initializing the `VectorDBMemory` component.

```py
from genai_stack.stack.stack import Stack
from genai_stack.model import OpenAIGpt35Model
from genai_stack.embedding.langchain import LangchainEmbedding
from genai_stack.vectordb import ChromaDB, Weaviate
from genai_stack.memory import VectorDBMemory

model = OpenAIGpt35Model.from_kwargs(parameters={"openai_api_key": "<ADD_OPENAI_KEY>"})

config = {
    "model_name": "sentence-transformers/all-mpnet-base-v2",
    "model_kwargs": {"device": "cpu"},
    "encode_kwargs": {"normalize_embeddings": False},
}
embedding = LangchainEmbedding.from_kwargs(name="HuggingFaceEmbeddings", fields=config)

vectordb = ChromaDB.from_kwargs(index_name="Testing")

    or

vectordb = Weaviate.from_kwargs(
    url="http://localhost:8080/", index_name="Testing", text_key="test"
)

memory = VectorDBMemory.from_kwargs(index_name = "Conversation", k=2)

Stack(
    model=model,
    embedding=embedding,
    vectordb=vectordb,
    memory=memory
)

# Storing few conversation
memory.add_text(user_text="Hi my name is Jhon",model_text="Hello, Jhon! How can I assist you today?")
memory.add_text(user_text="Which is the smallest month of the year?",model_text="The smallest month of the year is February")
memory.add_text(user_text="What is my name?",model_text="Your name is Jhon.")

memory.get_chat_history()
```

**Important Note**:Once the total number of conversations are 40, the first 20 conversations are removed from vectordb memory. This is because to make sure the context length doesn't exceeds.
