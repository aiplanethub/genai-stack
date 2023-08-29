#!/usr/bin/env python

"""Tests for `genai_stack` package."""


import unittest

from genai_stack.model.gpt4all import GPT4AllModel
from genai_stack.etl.llamahub_loader import LLamaHubEtl


class TestEtl(unittest.TestCase):
    def test_gpt4all(self):
        model = GPT4AllModel.from_kwargs(model_path="/tmp")
        model.predict("how many countries are there in the world")
