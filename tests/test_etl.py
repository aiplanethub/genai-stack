#!/usr/bin/env python

"""Tests for `llaim` package."""


import unittest

from llaim.etl.lang_loader import list_langchain_loaders, LangLoaderEtl


class TestEtl(unittest.TestCase):
    def test_list_langchain_loaders(self):
        langchain_loaders = list_langchain_loaders()
        assert isinstance(langchain_loaders, list)
        assert "CSVLoader" in langchain_loaders

    def test_langloader_etl(self):
        langhub_etl = LangLoaderEtl(config="assets/config.json")
        langhub_etl.run()

    def test_langloader_etl_custom_embedding(self):
        langhub_etl = LangLoaderEtl(config="assets/config_custom_embedding.json")
        langhub_etl.run()
