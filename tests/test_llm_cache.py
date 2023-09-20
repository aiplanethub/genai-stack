#!/usr/bin/env python

"""Tests for `genai_stack` package."""

import unittest

from genai_stack.embedding.langchain import LangchainEmbedding
from genai_stack.stack.stack import Stack
from genai_stack.vectordb import ChromaDB, Weaviate
from genai_stack.llm_cache import LLMCache


class TestLLLMCache(unittest.TestCase):
    embedding = LangchainEmbedding.from_kwargs(
        name="HuggingFaceEmbeddings",
        fields={
            "model_name": "sentence-transformers/all-mpnet-base-v2",
            "model_kwargs": {"device": "cpu"},
            "encode_kwargs": {"normalize_embeddings": False},
        }
    )
    chromadb = ChromaDB.from_kwargs(search_method="max_marginal_relevance_search")
    weaviatedb = Weaviate.from_kwargs(
        url="http://localhost:8080/",
        index_name="Testing",
        text_key="test",
        attributes=["source", "page"]
    )
    llm_cache = LLMCache.from_kwargs()

    def test_llm_cache_with_chromadb(self):
        stack = Stack(
            model=None,
            embedding=self.embedding,
            vectordb=self.chromadb,
            llm_cache=self.llm_cache,
        )

        query = "How many countries are there in the world?"
        response = "There are 195 countries in the world."
        stack.llm_cache.set_cache(
            query=query,
            response=response
        )
        assert stack.llm_cache.get_cache(query=query) == response

        query = "How many states are there in the USA?"
        response = "There are 50 states in the USA."
        stack.llm_cache.set_cache(
            query=query,
            response=response,
            metadata={"source": "Wikipedia", "page": 1}
        )
        assert response == stack.llm_cache.get_cache(
            query=query,
            metadata={"source": "Wikipedia", "page": 1}
        )
        assert response != stack.llm_cache.get_cache(
            query=query,
            metadata={"source": "Wikipdfedia", "page": 1}
        )

    def test_llm_cache_with_weaviatedb(self):
        stack = Stack(
            model=None,
            embedding=self.embedding,
            vectordb=self.weaviatedb,
            llm_cache=self.llm_cache,
        )

        query = "How many countries are there in the world?"
        response = "There are 195 countries in the world."
        stack.llm_cache.set_cache(
            query=query,
            response=response
        )
        assert stack.llm_cache.get_cache(query=query) == response

        query = "How many states are there in the USA?"
        response = "There are 50 states in the USA."
        stack.llm_cache.set_cache(
            query=query,
            response=response,
            metadata={"source": "Wikipedia", "page": 1}
        )
        assert response == stack.llm_cache.get_cache(
            query=query,
            metadata={"source": "Wikipedia", "page": 1}
        )
        assert response != stack.llm_cache.get_cache(
            query=query,
            metadata={"source": "Wikipedia", "page": 3}
        )
        assert response != stack.llm_cache.get_cache(
            query=query,
            metadata={"source": "Wikipdfedia", "page": 1}
        )


