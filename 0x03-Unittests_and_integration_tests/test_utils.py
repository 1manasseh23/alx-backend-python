#!/usr/bin/env python3
"""
The unit test for utils.access_nested_map
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map  # Adjust the import as necessary
from unittest.mock import patch, Mock
from utils import get_json  # Adjust the import as necessary


class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand([
        ({}, ["a"], "'a'"),
        ({"a": 1}, ["a", "b"], "'b'"),
    ])
    def test_access_nested_map_exception(
            self, nested_map, path, expected_message):
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), expected_message)

    @parameterized.expand([
        ({"a": 1}, ["a"], 1),
        ({"a": {"b": 2}}, ["a"], {"b": 2}),
        ({"a": {"b": 2}}, ["a", "b"], 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)


class TestGetJson(unittest.TestCase):

    @patch('requests.get')
    def test_get_json(self, mock_get):
        # Define test cases
        test_cases = [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]

        for test_url, test_payload in test_cases:
            # Set up the mock response
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            # Call the function
            result = get_json(test_url)

            # Check that the mock was called once with the correct URL
            mock_get.assert_called_once_with(test_url)

            # Check that the result is what we expect
            self.assertEqual(result, test_payload)

            # Reset the mock for the next iteration
            mock_get.reset_mock()


if __name__ == "__main__":
    unittest.main()
