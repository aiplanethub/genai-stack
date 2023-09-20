from typing import List

from langchain.schema import Document

from genai_stack.llm_cache.base import BaseLLMCache, BaseLLMCacheConfigModel, BaseLLMCacheConfig


class LLMCacheConfigModel(BaseLLMCacheConfigModel):
    """
    Data Model for the configs
    """

    pass


class LLMCacheConfig(BaseLLMCacheConfig):
    data_model = LLMCacheConfigModel


class LLMCache(BaseLLMCache):
    config_class = LLMCacheConfig
    kwarg_map = {
        "ChromaDB": {"index_name": "Cache"},
        "Weaviate": {
            "index_name": "Cache",
            "text_key": "cache",
            "attributes": ["response"],
        },
    }

    def _post_init(self, *args, **kwargs):
        self.client = self.mediator.create_index(self.kwarg_map)

    def get_cache(
        self,
        query: str,
        metadata: dict = None,
    ):
        """
        This method is for getting the cached response from the cache vectordb. This method performs similarity search on the
        query and scalar search using the metadata.
        """
        response = self.mediator.hybrid_search(query, metadata, self.kwarg_map)
        if response and response[0]["isSimilar"]:
            return response[0]["response"]
        return None

    def set_cache(
        self,
        query: str,
        response: str,
        metadata: dict = None,
    ):
        """
        This method is for setting the cached response in the cache vectordb. This method adds the response to the cache
        vectordb.
        """
        if not metadata:
            metadata = {}
        self.client.add_documents(
            [Document(
                metadata={
                    **metadata,
                    "response": response
                },
                page_content=query,
                vector=self.mediator.get_embedded_text(query),
            )]
        )
