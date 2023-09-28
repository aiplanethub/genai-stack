#!/usr/bin/env python

"""Tests for `genai_server`."""

import unittest
import requests


class TestSessionServerAPIs(unittest.TestCase):

    def setUp(self) -> None:
        self.base_url = "http://127.0.0.1:8080/api/session"

    def fetch(self, url, method="GET", data=None):
        if method == "GET":
            return requests.get(url=url)
        elif method == "POST":
            return requests.post(url=url, data=data)
        elif method == "DELETE":
            return requests.delete(url=url)

    def test_create_session(self):
        response = self.fetch(url=self.base_url, method="POST")
        assert response.status_code == 200
        assert response.json().get("id") == 1

    def test_sessions_list(self):
        response = self.fetch(url=self.base_url, method="GET")
        assert response.status_code == 200

    def test_get_session(self):
        response = self.fetch(url=self.base_url + "/1", method="GET")
        assert response.status_code == 200

    def test_delete_session(self):
        response = self.fetch(url=self.base_url + "/1", method="DELETE")
        assert response.status_code == 200
