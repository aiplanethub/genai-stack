#!/usr/bin/env python

"""Tests for `genai_server`."""

import unittest
import requests


class TestVectorDBServerAPIs(unittest.TestCase):

    def setUp(self) -> None:
        self.base_url = "http://127.0.0.1:8080/api/vectordb"

    def fetch(self, url, method="GET", data=None, **kwargs):
        if method == "GET":
            return requests.get(url=url, **kwargs)
        elif method == "POST":
            return requests.post(url=url, data=data, **kwargs)

    def test_add_document(self):
        response = self.fetch(
            url=self.base_url + "/add-documents",
            method="POST",
            data={"session_id": 1, "data": {"page_content": "Hello World", "metadata": {"title": "Hello World"}}},
        )
        assert response.status_code == 200
        assert response.json().get("id") == 1

    def test_search(self):
        response = self.fetch(
            url=self.base_url + "/search",
            params={"session_id": 1, "query": "Hello World"},
        )
        assert response.status_code == 200
        assert response.json().get("id") == 1
