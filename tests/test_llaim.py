#!/usr/bin/env python

"""Tests for `llaim` package."""


import unittest
from click.testing import CliRunner

from llaim import llaim
from llaim import cli


class TestLlaim(unittest.TestCase):
    """Tests for `llaim` package."""

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
