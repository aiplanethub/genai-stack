#!/usr/bin/env python

"""Tests for `genai_server`."""

import unittest
import requests


class TestRetrieverServerAPIs(unittest.TestCase):

    def setUp(self) -> None:
        self.base_url = "http://127.0.0.1:8080/api/retriever"

    def test_retrieve(self):
        response = requests.get(
            url=self.base_url + "/retrieve",
            params={"session_id": 1, "query": "Hello World"},
        )
        assert response.status_code == 200
        assert response.json()
        data = response.json()
        assert "output" in data.keys()
