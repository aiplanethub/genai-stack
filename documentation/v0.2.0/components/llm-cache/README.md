# 🗃️ LLM Cache

The LLM Cache component is responsible for managing the cache of the language model (LLM). It is responsible for storing
and retrieving the cache. It can be used to store the cache in a preferred vector database (weaviate or chromadb). This
component is optional and can be used to improve the performance of the stack. It reduces the number of queries to the
LLM and is cost-effective.

**Setting the cache** : The LLM Cache component is responsible for setting the cache of the language model (LLM). It can
store the query and response along with their metadata in the cache.

**Getting the cache** : The LLM Cache component is responsible for getting the cache of the language model (LLM). It does
a hybrid search based on the query and metadata to retrieve the cache. The returned cache will contain the expected
response for the query.

The stack can be used without the LLM Cache component. In this case, the stack will directly interact with the LLM to
generate the response.
