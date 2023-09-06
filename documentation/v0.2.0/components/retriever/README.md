# 📤 Retrieval

<figure><img src="../../.gitbook/assets/Screenshot from 2023-08-09 17-01-52.png" alt=""><figcaption></figcaption></figure>

A "Retriever" component is responsible for managing various retrieval-related tasks. Its primary purpose is to retrieve the necessary information or resources required. Here's a breakdown of the responsibilities typically associated with a Retriever.

**Getting the Context**: The retriever is responsible for querying and retrieving data from the Vector database that stores the source data. This step will basically return the relevant documents based on the query.

**Post-processing**: After retrieving relevant documentation from vectordb, the Retriever will perform post-processing tasks on it. This will include parsing and may also include cleaning, formatting, or transforming the retrieved data to make it suitable for further use.

**Getting Prompt Templates**: Prompt templates are predefined and also can be user defined structures that guide the conversation or interaction with the user. The Retriever will retrieve these templates from the prompt engine component.

There are three different types of prompt template available, you can look more into how the prompt engine component decides which prompt template should be used.

**Formatting the Prompt Template**: Once the prompt template is retrieved, the Retriever will be responsible for formatting it to ensure it aligns with the expected format.

**Getting the Chat History**: The chat history includes a record of previous interactions and messages exchanged within the conversation. The Retriever will retrieve previous chat history for the prompt template.

**Querying the Language Model (LLM)**: To generate responses, the Retriever interacts with a language model (LLM). It sends a prompt template to the LLM, which could involve asking questions, requesting responses, or seeking information based on the retrieved context.

**Storing the Chat Conversation**: The latest chat conversation is stored in the memory to maintain a sense of continuity and context within the conversation.

## Without Retriever Component

**User Query Processing**: In the absence of the retriever component, the stack components still have their individual responsibilities. The prompt engine is used to define the structure of the prompt template, the memory component stores chat history, the vectordb component handles context and vector embeddings, and the model component generates answers to user queries.

**Resource Integration**: Without the retriever, the integration of these resources becomes more manual. The other stack components may need to work together to gather and structure the input for the model component. For example, the prompt engine, vectordb and memory component need to collaborate to assemble the necessary context and template.

**Interaction with Language Model**: The model component will directly receive the structured input or template from the prompt engine and It will generate a response.

**Conversation Memory Update**: In this scenario, it becomes the responsibility of the individual components to manage conversation history updates. For example, the memory component might need to be more proactive in storing and retrieving chat history to maintain context.

In summary, the retriever component acts as an orchestrator that streamlines the process of collecting and integrating resources from various stack components for interaction with the language model. Without the retriever, the stack components would need to work more closely together to achieve the same result, potentially requiring more manual coordination and integration of information.

## Supported Retriever

Currently we have support only for:

-   LangChain Retriever
