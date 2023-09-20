# 📚 Introduction

### What is GenAI Stack?

GenAI Stack is an end-to-end framework designed to integrate large language models (LLMs) into applications seamlessly. The purpose is to bridge the gap between raw data and actionable insights or responses that applications can utilize, leveraging the power of LLMs.

### How does it work?

There are 7 main components involved in GenAI Stack.

1. Data extraction & loading
2. Embeddings
3. Vector databases
4. Prompt engine
5. Retrieval
6. Memory
7. Model

The operation of GenAI Stack can be understood through its various components:

**Data extraction & loading:**

Supports data extraction from various sources including structured (sql, postgress etc), unstructured (pdf, webpages etc) and semi-structured (mongoDB, documentDB etc) data sources. GenAI Stack supports airbyte and llamahub for this purpose.

**Embeddings:**

Embeddings are numerical representations of data, typically used to represent words, sentences, or other objects in a vector space. In natural language processing (NLP), word embeddings are widely used to convert words into dense vectors. Each word is represented by a unique vector in such a way that semantically similar words have similar vectors. Popular word embedding methods include Word2Vec, GloVe, and FastText. Word embeddings are essential in various NLP tasks such as sentiment analysis, machine translation, and named entity recognition. They capture semantic relationships between words, allowing models to understand context and meaning. In addition to words, entire sentences or paragraphs can be embedded into fixed-length vectors, preserving the semantic information of the text. Sentence embeddings are useful for tasks like text classification, document clustering, and information retrieval.

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
