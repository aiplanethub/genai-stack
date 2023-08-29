#!/usr/bin/env python

"""Tests for `genai_stack` package."""


import unittest
from click.testing import CliRunner

from genai_stack import cli


class Testgenai_stack(unittest.TestCase):
    """Tests for `genai_stack` package."""

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
