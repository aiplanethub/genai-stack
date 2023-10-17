#!/usr/bin/env python

"""Tests for `genai_stack` package."""


import unittest

from genai_stack.stack.stack import Stack
from genai_stack.vectordb import ChromaDB, Weaviate
from genai_stack.embedding.langchain import LangchainEmbedding
from genai_stack.memory import ConversationBufferMemory, VectorDBMemory

class TestConversationBufferMemory(unittest.TestCase):
    def test_conversation_buffer_memory(self):
        memory = ConversationBufferMemory(config={})

        # Storing few conversation
        memory.add_text(
            user_text="hello my name is Ali,what’s your name?",
            model_text="my name is Mona ,nice to meet you ,Al"
        )
        memory.add_text(
            user_text="nice to meet you,whats your last name",
            model_text="it’s Mohamed,and you"
        )
        memory.add_text(
            user_text="it’s Nader",
            model_text="what are you doing for living?"
        )

        # Chat history
        print(memory.get_chat_history())

        # User query
        assert memory.get_user_text() == "it’s Nader"
        print(memory.get_user_text())

         # Model response
        assert memory.get_model_text() == "what are you doing for living?"
        print(memory.get_model_text())

class TestVectordbMemory(unittest.TestCase):
    def chromadb_stack(self, index_name = "Chroma", k=4):
        config = {
            "model_name": "sentence-transformers/all-mpnet-base-v2",
            "model_kwargs": {"device": "cpu"},
            "encode_kwargs": {"normalize_embeddings": False},
        }
        self.embedding = LangchainEmbedding.from_kwargs(
            name="HuggingFaceEmbeddings", fields=config
        )

        # VectorDB
        self.chromadb = ChromaDB.from_kwargs()

        # VectorDB Memory
        self.memory = VectorDBMemory.from_kwargs(index_name = index_name,k=k)

        self.chromadb_memory_stack = Stack(
            model=None, 
            embedding=self.embedding, 
            vectordb=self.chromadb, 
            memory=self.memory
        )


    def weaviatedb_stack(self, index_name = "Weaviate", k=4):
        config = {
            "model_name": "sentence-transformers/all-mpnet-base-v2",
            "model_kwargs": {"device": "cpu"},
            "encode_kwargs": {"normalize_embeddings": False},
        }
        self.embedding = LangchainEmbedding.from_kwargs(
            name="HuggingFaceEmbeddings", fields=config
        )

        # VectorDB
        self.weaviatedb = Weaviate.from_kwargs(
            url="http://localhost:8080/", index_name="Testing", text_key="test"
        )

        # VectorDB Memory
        self.memory = VectorDBMemory.from_kwargs(index_name = index_name, k=k)

        self.weaviatedb_memory_stack = Stack(
            model=None, 
            embedding=self.embedding, 
            vectordb=self.weaviatedb, 
            memory=self.memory
        )  
    
    def store_conversation_to_chromadb_memory(self, user_text:str, model_text:str):
        self.chromadb_memory_stack.memory.add_text(
            user_text=user_text,model_text=model_text
        )
    
    def store_conversation_to_weaviate_memory(self, user_text:str, model_text:str):
        self.weaviatedb_memory_stack.memory.add_text(
            user_text=user_text,model_text=model_text
        )
    
    def test_chromadb_memory(self):
        print(self.chromadb_memory_stack.memory.get_chat_history())
    
    def test_weaviatedb_memory(self):
        print(self.weaviatedb_memory_stack.memory.get_chat_history())
