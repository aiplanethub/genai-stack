#!/usr/bin/env python

"""Tests for `genai_stack` package."""


import unittest

from genai_stack.etl.langchain import list_langchain_loaders, LangchainETL
from genai_stack.etl.llamahub_loader import LLamaHubEtl


class TestEtl(unittest.TestCase):
    def test_list_langchain_loaders(self):
        langchain_loaders = list_langchain_loaders()
        assert isinstance(langchain_loaders, list)
        assert "CSVLoader" in langchain_loaders

    def test_langloader_etl(self):
        etl = LangchainETL.from_kwargs(
            name="PyPDFLoader", fields={"file_path": "/path/to/pdf"}
        )
        etl.extract()
        # Need to write testcases after integrating the vectordb component
