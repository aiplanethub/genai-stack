#!/usr/bin/env python

"""Tests for `genai_server`."""
import json
import unittest
import requests


class TestVectorDBServerAPIs(unittest.TestCase):

    def setUp(self) -> None:
        self.base_url = "http://127.0.0.1:5000/api/vectordb"

    def test_add_document(self):
        response = requests.post(
            url=self.base_url + "/add-documents",
            data=json.dumps({"session_id": 2, "documents": [{"page_content": "Sunil lives in Hyderabad", "metadata": {"source": "/path", "page": 1}}]}),
        )
        assert response.status_code == 200

    def test_search(self):
        response = requests.get(
            url=self.base_url + "/search",
            data=json.dumps({"session_id": 2, "query": "Where is Sunil from ?"}),
        )
        print(response.json())
        assert response.status_code == 200
