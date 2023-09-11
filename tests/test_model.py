#!/usr/bin/env python

"""Tests for `genai_stack` package."""


import unittest

from genai_stack.model import OpenAIGpt35Model


class TestModel(unittest.TestCase):
    def test_openai_gpt35_model(self):
        llm = OpenAIGpt35Model.from_kwargs(parameters={"openai_api_key": "<ADD_OPENAI_KEY>"})
        model_response = llm.predict("How many countries are there in the world?")
        print(model_response)
