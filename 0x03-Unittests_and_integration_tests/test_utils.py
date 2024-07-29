#!/usr/bin/env python3
"""
The unit test for utils.access_nested_map
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map  # Adjust the import as necessary


class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand([
        ({}, ["a"], "'a'"),
        ({"a": 1}, ["a", "b"], "'b'"),
    ])
    def test_access_nested_map_exception(self, nested_map, \
            path, expected_message):
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


if __name__ == "__main__":
    unittest.main()
