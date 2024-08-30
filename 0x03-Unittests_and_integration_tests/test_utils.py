#!/usr/bin/env python3
"""This script houses the TestAccessNestedMap class"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """Something"""
    @parameterized.expand([
        ({"a": 1}, ["a"], 1),
        ({"a": {"b": 2}}, ["a"], {"b": 2}),
        ({"a": {"b": 2}}, ["a", "b"], 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """This method tests that access_nested_map returns as expected"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ["a"]),
        ({"a": 1}, ["a", "b"]),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """This method tests that exceptions are raised """
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
        self.assertEqual(str(error.exception), repr(path[-1]))


class TestGetJson(unittest.TestCase):
    """This class implements the test_get_json method
    to test that utils.get_json returns the expected result.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """This method tests the utils.get_json method to
        return the expected result"""
        with patch('utils.requests.get') as mock_get:
            # Create the Mock object with the desired json method behavior
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response
            # Call the function to test
            url_data = get_json(test_url)
            # Assert that requests.get was called exactly once with
            # the correct URL
            mock_get.assert_called_once_with(test_url)
            # Assert that the result is as expected
            self.assertEqual(url_data, test_payload)


if __name__ == '__main__':
    unittest.main()
