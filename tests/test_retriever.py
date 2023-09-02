#!/usr/bin/env python

"""Tests for `genai_stack` package."""


import unittest

from genai_stack.retriever import LangChainRetriever
from genai_stack.model import OpenAIGpt35Model
from genai_stack.memory import ConversationBufferMemory
from genai_stack.prompt_engine.engine import PromptEngine
from genai_stack.stack.stack import Stack

class TestLangChainRetriever(unittest.TestCase):
    def test_retriever(self, query):
        retriever = LangChainRetriever(config={})
        promptengine = PromptEngine.from_kwargs(should_validate = False)
        memory = ConversationBufferMemory(config={})
        model = OpenAIGpt35Model.from_kwargs(parameters={"openai_api_key": "your-key"})
        Stack(model=model, prompt_engine=promptengine, retriever=retriever, memory=memory)
        response = retriever.retrieve(query)

        print(response)