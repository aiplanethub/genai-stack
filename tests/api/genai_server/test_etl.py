#!/usr/bin/env python

"""Tests for `genai_server`."""

import unittest
import requests


class TestETLServerAPIs(unittest.TestCase):

    def setUp(self) -> None:
        self.base_url = "http://127.0.0.1:8080/api/etl"

    def test_submit_job(self):
        response = requests.get(
            url=self.base_url + "/submit-job",
            params={"session_id": 1, "data": {"page_content": "Hello World", "metadata": {}}},
        )
        assert response.status_code == 200
        assert response.json().get("id") == 1
