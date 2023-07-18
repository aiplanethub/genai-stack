#!/usr/bin/env python

"""Tests for `llaim` package."""


import unittest
from click.testing import CliRunner

from llaim.etl.lang_loader import list_langchain_loaders, LangHubEtl
from llaim import cli


class TestEtl(unittest.TestCase):

    def test_list_langchain_loaders(self):
        langchain_loaders = list_langchain_loaders()
        assert isinstance(langchain_loaders, list)
        assert "CSVLoader" in langchain_loaders

    def test_langhub_etl(self):
        langhub_etl = LangHubEtl(config="assets/config.json")
        langhub_etl.run()

    def test_langhub_etl_custom_embedding(self):
        langhub_etl = LangHubEtl(config="assets/config_custom_embedding.json")
        langhub_etl.run()
