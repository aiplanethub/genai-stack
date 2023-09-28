#!/usr/bin/env python

"""Tests for `genai_server`."""

import unittest
import requests


class TestSessionServerAPIs(unittest.TestCase):

    def setUp(self) -> None:
        self.base_url = "http://127.0.0.1:5000/api/session"

    def test_create_session(self):
        response = requests.post(url=self.base_url)
        print(response.json())
        assert response.status_code == 200

    def test_sessions_list(self):
        response = requests.get(url=self.base_url)
        assert response.status_code == 200

    def test_get_session(self):
        response = requests.get(
            url=self.base_url + "/1",
            params={"session_id": 1},
        )
        assert response.status_code == 200

    def test_delete_session(self):
        response = requests.delete(
            url=self.base_url + "/1",
            params={"session_id": 1},
        )
        assert response.status_code == 200
