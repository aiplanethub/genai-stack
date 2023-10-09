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
        memory.add_text(user_text="hello my name is Ali,what’s your name?",model_text="my name is Mona ,nice to meet you ,Al")
        memory.add_text(user_text="nice to meet you,whats your last name",model_text="it’s Mohamed,and you")
        memory.add_text(user_text="it’s Nader",model_text="what are you doing for living?")

        # Chat history
        print(memory.get_chat_history())

        # User query
        assert memory.get_user_text() == "it’s Nader"
        print(memory.get_user_text())

         # Model response
        assert memory.get_model_text() == "what are you doing for living?"
        print(memory.get_model_text())

class TestVectordbMemory(unittest.TestCase):
    def setup_stack(self):
        config = {
            "model_name": "sentence-transformers/all-mpnet-base-v2",
            "model_kwargs": {"device": "cpu"},
            "encode_kwargs": {"normalize_embeddings": False},
        }
        self.embedding = LangchainEmbedding.from_kwargs(name="HuggingFaceEmbeddings", fields=config)

        # VectorDB
        self.chromadb = ChromaDB.from_kwargs()
        self.weaviatedb = Weaviate.from_kwargs(url="http://localhost:8080/", index_name="Testing", text_key="test")

        # VectorDB Memory
        retrieve_parameters = {
                'search_type':'similarity',
                'search_kwargs':{'k':1}
        }
        self.chromadb_memory = VectorDBMemory.from_kwargs(
            chromadb={"index_name":"test_chromadb_memory"},
            retrieve_parameters=retrieve_parameters
        )
        self.weaviatedb_memory = VectorDBMemory.from_kwargs(
            weaviate={
            "index_name":"test_weaviate_memory", 
            "text_key":"chat_history"
            },
            retrieve_parameters=retrieve_parameters
        )

        # Stack for each VectorDB
        self.chroma_stack = Stack(model=None, embedding=self.embedding, vectordb=self.chromadb, memory=self.chromadb_memory)
        self.weaviate_stack = Stack(model=None, embedding=self.embedding, vectordb=self.weaviatedb, memory=self.weaviatedb_memory)

    
    def store_random_conversation_to_test(self):
        self.chromadb_memory.add_text(user_text="My favorite food is pizza",model_text="that's good to know")
        self.chromadb_memory.add_text(user_text="My favorite sport is soccer",model_text="that's good to know")
        self.chromadb_memory.add_text(user_text="My favorite car is lamborgini",model_text="that's good to know")
        self.chromadb_memory.add_text(user_text="My favorite movie is kushi",model_text="that's good to know")

        self.weaviatedb_memory.add_text(user_text="My favorite food is pasta",model_text="that's good to know")
        self.weaviatedb_memory.add_text(user_text="My favorite sport is cricket",model_text="that's good to know")
        self.weaviatedb_memory.add_text(user_text="My favorite car is supra",model_text="that's good to know")
        self.weaviatedb_memory.add_text(user_text="My favorite movie is The Walking Dead",model_text="that's good to know")
        print("Completed adding random conversation")
    
    def test_chromadb_memory(self, query:str = "what is my favourite car?"):
        print(self.chromadb_memory.get_chat_history(query=query))

    def test_weaviatedb_memory(self, query:str = "what is my favourite sport?"):
        print(self.weaviatedb_memory.get_chat_history(query=query))
