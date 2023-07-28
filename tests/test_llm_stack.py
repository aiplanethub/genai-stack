#!/usr/bin/env python

"""Tests for `llm_stack` package."""


import unittest
from click.testing import CliRunner

from llm_stack import cli


class Testllm_stack(unittest.TestCase):
    """Tests for `llm_stack` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        help_result = runner.invoke(cli.main, ["--help"])
        assert help_result.exit_code == 0
        assert "--help  Show this message and exit." in help_result.output
