# 📚 Introduction

### What is GenAI Stack?

GenAI Stack is an end-to-end framework designed to integrate large language models (LLMs) into applications seamlessly. The purpose is to bridge the gap between raw data and actionable insights or responses that applications can utilize, leveraging the power of LLMs.

### How does it work?

There are 4 main components involved in GenAI Stack.

1. Data extraction & loading
2. Vector databases
3. Prompt engine
4. Retrieval
5. Memory
6. Model

The operation of GenAI Stack can be understood through its various components:

**Data extraction & loading:**

Supports data extraction from various sources including structured (sql, postgress etc), unstructured (pdf, webpages etc) and semi-structured (mongoDB, documentDB etc) data sources. GenAI Stack supports airbyte and llamahub for this purpose.

**Vector databases:**

Data that has been extracted is then converted into vector embeddings. These embeddings are representations of the data in a format that can be quickly and accurately searched. Embeddings are stored in vector databases. GenAI Stack supports databases like weaviate and chromadb for this purpose.

**Prompt engine:**

The prompt engine is responsible for generating prompt templates based on the user query and the type of prompt required. The prompt templates are then passed to the retriever, which uses them to retrieve relevant data from the source database. The prompt engine also performs validation on the user query to ensure that it is safe to be sent to the retriever.

**Retrieval:**&#x20;

A Retriever component is responsible for managing various retrieval-related tasks. Its primary purpose is to retrieve the necessary information or resources required, such as querying and retrieving the relevant documents from vectordb component, performing post processing tasks on it, retrieving the prompt template from the prompt engine component and formatting it to ensure it aligns with expected format. retrieving the chat history, and finally querying the llm and storing the query and response in memory.

**Memory:**

Memory is a vital component within a chat system responsible for storing and managing chat conversations. Its primary function is to retain a record of past interactions between users and llms. This stored information serves multiple purposes, including improving the llm's ability to provide contextually relevant responses, tracking user preferences, and facilitating seamless, coherent conversations. Storing user inputs, and system responses, creating a valuable resource for enhancing user experiences and enabling personalized interactions within the chat environment.

**LLMs:**

Large Language Models leverage the vector embeddings to generate responses or insights based on user queries. We've pre-configured ChatGPT and gpt4all, however, you can configure your own custom models. With gpt4all and any other open source LLMs, it offers developers to host the entire stack and model on their own servers, providing them required privacy and security.

In conclusion, GenAI Stack is a comprehensive framework that offers a structured approach to harness the capabilities of large language models for various applications. Its well-defined components ensure a smooth integration process, making it easier for developers to build applications powered by advanced LLMs.
