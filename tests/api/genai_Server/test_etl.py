#!/usr/bin/env python

"""Tests for `genai_server`."""

import unittest
import requests


class TestETLServerAPIs(unittest.TestCase):

    def setUp(self) -> None:
        self.base_url = "http://127.0.0.1:8080/api"

    def create_session(self):
        response = requests.post(url=self.base_url + "/session")
        assert response.status_code == 200
        return response.json()

    def test_submit_job(self):
        session = self.create_session()
        response = requests.get(
            url=self.base_url + "/etl/submit-job",
            params={"session_id": session.get("id"), "data": {"page_content": "Hello World", "metadata": {}}},
        )
        assert response.status_code == 200
        assert response.json().get("id") == 1
