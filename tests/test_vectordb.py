#!/usr/bin/env python

"""Tests for `genai_stack` package."""


import unittest

from langchain.docstore.document import Document as LangDocument

from genai_stack.vectordb.chromadb import ChromaDB
from genai_stack.vectordb.weaviate_db import Weaviate
from genai_stack.embedding.langchain import LangchainEmbedding
from genai_stack.stack.stack import Stack


class TestVectordb(unittest.TestCase):
    def setUp(self) -> None:
        config = {
            "model_name": "sentence-transformers/all-mpnet-base-v2",
            "model_kwargs": {"device": "cpu"},
            "encode_kwargs": {"normalize_embeddings": False},
        }
        self.embedding = LangchainEmbedding.from_kwargs(name="HuggingFaceEmbeddings", fields=config)
        self.chromadb = ChromaDB.from_kwargs()
        self.weaviatedb = Weaviate.from_kwargs(url="http://localhost:8080/", index_name="Testing", text_key="test")

        self.chroma_stack = Stack(model=None, embedding=self.embedding, vectordb=self.chromadb)
        self.weaviate_stack = Stack(model=None, embedding=self.embedding, vectordb=self.weaviatedb)

    def test_chromadb(self):
        self.chroma_stack.vectordb.add_documents(
            documents=[
                LangDocument(
                    page_content="Some page content explaining something", metadata={"some_metadata": "some_metadata"}
                )
            ]
        )
        result = self.chroma_stack.vectordb.search("page")
        print(result)

    def test_weaviatedb(self):
        self.weaviate_stack.vectordb.add_documents(
            documents=[
                LangDocument(
                    page_content="Some page content explaining something", metadata={"some_metadata": "some_metadata"}
                )
            ]
        )
        result = self.weaviate_stack.vectordb.search("page")
        print(result)


if __name__ == "__main__":
    unittest.main()
