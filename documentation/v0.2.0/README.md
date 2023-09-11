# 📚 Introduction

### What is GenAI Stack?

GenAI Stack is an end-to-end framework designed to integrate large language models (LLMs) into applications seamlessly. The purpose is to bridge the gap between raw data and actionable insights or responses that applications can utilize, leveraging the power of LLMs.

### How does it work?

There are 4 main components involved in GenAI Stack.

1. Data extraction & loading
2. Vector databases
3. LLMs
4. Retrieval

The operation of GenAI Stack can be understood through its various components:

**Data extraction & loading:**

Supports data extraction from various sources including structured (sql, postgress etc), unstructured (pdf, webpages etc) and semi-structured (mongoDB, documentDB etc) data sources. GenAI Stack supports airbyte and llamahub for this purpose.

**Vector databases:**

Data that has been extracted is then converted into vector embeddings. These embeddings are representations of the data in a format that can be quickly and accurately searched. Embeddings are stored in vector databases. GenAI Stack supports databases like weaviate and chromadb for this purpose.

**LLMs:**

Large Language Models leverage the vector embeddings to generate responses or insights based on user queries. We've pre-configured ChatGPT and gpt4all, however, you can configure your own custom models. With gpt4all and any other open source LLMs, it offers developers to host the entire stack and model on their own servers, providing them required privacy and security.

**Retrieval:**&#x20;

LangChain is the default tool used for retrieving the best-suited embeddings based on the query. When a query is made, instead of searching through the raw data, GenAI Stack looks for the closest matching vector embedding. This ensures fast and accurate results. The overall mechanism ensures that the data is utilized in its entirety. When a query is made, the LLMs search through the closest embeddings, ensuring responses are generated without hallucination (i.e., without making things up or providing inaccurate information).

In conclusion, GenAI Stack is a comprehensive framework that offers a structured approach to harness the capabilities of large language models for various applications. Its well-defined components ensure a smooth integration process, making it easier for developers to build applications powered by advanced LLMs.
