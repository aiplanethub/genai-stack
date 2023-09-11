#!/usr/bin/env python

"""Tests for `genai_stack` package."""


import unittest

from genai_stack.retriever import LangChainRetriever
from genai_stack.model import OpenAIGpt35Model
from genai_stack.memory import ConversationBufferMemory
from genai_stack.prompt_engine.engine import PromptEngine
from genai_stack.stack.stack import Stack

class TestLangChainRetriever(unittest.TestCase):

    def __init__(self, openai_api_key:str) -> None:
        self.retriever = LangChainRetriever(config={})
        self.promptengine = PromptEngine.from_kwargs(should_validate = False)
        self.memory = ConversationBufferMemory(config={})
        self.model = OpenAIGpt35Model.from_kwargs(parameters={"openai_api_key": openai_api_key})
        Stack(model=self.model, prompt_engine=self.promptengine, retriever=self.retriever, memory=self.memory)
        
    def test_retriever(self, query):
        response = self.retriever.retrieve(query)
        print(response)