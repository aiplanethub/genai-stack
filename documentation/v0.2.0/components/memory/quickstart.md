# 🔥 Quickstart

Currently we have support only for **Conversation Buffer Memory**.

A Conversation Buffer Memory component temporarily stores recent messages and interactions in a conversation. It acts as a short-term memory buffer, holding onto messages for a brief period to facilitate real-time conversations. This component help in maintaining a sense of continuity and context within the conversation.

Conversation Buffer Memory doesn't require any specific configuration from the user.

```py
from genai_stack.memory import ConversationBufferMemory

memory = ConversationBufferMemory.from_kwargs()

# Storing few conversation
memory.add_text(user_text="Hi my name is Jhon",model_text="Hello, Jhon! How can I assist you today?")
memory.add_text(user_text="Which is the smallest month of the year?",model_text="The smallest month of the year is February")
memory.add_text(user_text="What is my name?",model_text="Your name is Jhon.")

memory.get_chat_history()
```

**Important Note**: The ConversationBufferMemory uses the main memory of the system to store the conversations and it will be lost once the process gets terminated.
