from typing import List

from langchain.schema import Document

from genai_stack.llm_cache.base import BaseLLMCache, BaseLLMCacheConfigModel, BaseLLMCacheConfig


class LLMCacheConfigModel(BaseLLMCacheConfigModel):
    """
    Data Model for the configs
    """
    index_name: str = "Cache"
    text_key: str = "cache"
    attributes: List[str] = ["response"]


class LLMCacheConfig(BaseLLMCacheConfig):
    data_model = LLMCacheConfigModel


class LLMCache(BaseLLMCache):
    config_class = LLMCacheConfig

    def _get_kwargs_map(self):
        return {
            "ChromaDB": {"index_name": self.config.config_data.index_name},
            "Weaviate": {
                "index_name": self.config.config_data.index_name,
                "text_key": self.config.config_data.text_key,
                "attributes": self.config.config_data.attributes,
            },
        }

    def _post_init(self, *args, **kwargs):
        self.client = self.mediator.create_index(self._get_kwargs_map())

    def get_cache(
        self,
        query: str,
        metadata: dict = None,
    ):
        """
        This method is for getting the cached response from the cache vectordb. This method performs similarity search on the
        query and scalar search using the metadata.
        """
        response = self.mediator.hybrid_search(query, metadata, self._get_kwargs_map())
        if response and response[0].isSimilar:
            output = response[0].metadata.get("response") if response[0].metadata else None
            return output
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
                page_content=query
            )]
        )
        return True
