#!/usr/bin/env python3
"""
The unit test for utils.access_nested_map
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map  # Adjust the import as necessary
from unittest.mock import patch, Mock, MagicMock
from utils import get_json  # Adjust the import as necessary
from utils import memoize


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


class TestMemoize(unittest.TestCase):

    def test_memoize(self):

        # Define TestClass with the method and memoized property
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        # Use patch directly on the class definition
        with patch.object(TestClass, 'a_method', return_value=42) \
                as mock_a_method:
            obj = TestClass()

            # Access the memoized property twice
            result1 = obj.a_property
            result2 = obj.a_property

            # Verify that the result is correct
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            # Verify that a_method was called only once
            mock_a_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
