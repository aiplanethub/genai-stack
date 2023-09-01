#!/usr/bin/env python

"""Tests for `genai_stack` package."""


import unittest

from genai_stack.retriever import LangChain

class TestLangChainRetriever(unittest.TestCase):
    def test_retriever(self, query):

        retriever = LangChain.from_kwargs()

        response = retriever.retrieve(query)

        print(response)