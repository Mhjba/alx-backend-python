#!/usr/bin/env python3
"""module for testing the utils module."""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import MagicMock, patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """Tests the `access_nested_map` function."""
    @parameterized.expand(
        [
            ({"a": 1}, "a", 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, nested_map, path, output) -> None:
        """test access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), output)

    @parameterized.expand(
        [
            ({}, ("a",), KeyError),
            ({"a": 1}, ("a", "b"), KeyError),
        ]
    )
    def test_access_nested_map_exception(self, nested_map, path, error):
        """Tests `access_nested_map`'s exception raising."""
        with self.assertRaises(error):
            self.assertEqual(access_nested_map(nested_map, path))


class TestGetJson(unittest.TestCase):
    """Tests `get_json`'s output."""

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    @patch("requests.get")
    def test_get_json(self, test_url, test_payload, mock_requests_get) -> None:
        """Tests `get_json`'s output."""
        mock = Mock(return_value=test_payload)
        mock_requests_get.return_value.json = mock
        test = get_json(test_url)
        self.assertEqual(test, test_payload)
        mock_requests_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Tests the `memoize` function."""

    def test_memoize(self):
        """Tests `memoize`'s output."""
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, "a_method") as a_method:
            a_method.return_value = 10

            test_class = TestClass()
            test = test_class.a_property
            self.assertEqual(test_class.a_property, test)
            a_method.assert_called_once()
