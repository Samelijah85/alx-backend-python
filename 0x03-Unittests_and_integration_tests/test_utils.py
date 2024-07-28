#!/usr/bin/env python3
"""
Parameterize a unit test
"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    class that inherits from unittest.TestCase
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test the access_nested_map function with various nested maps and paths.

        Parameters:
            nested_map (dict): The nested dictionary to access.
            path (tuple): The path to the desired value in the nested
            dictionary.
            expected (Any): The expected result of accessing the nested map at
            the given path.

        Returns:
            None
        """

        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Test that access_nested_map raises a KeyError when the path does not
        exist.

        This test checks that access_nested_map raises a KeyError when the path
        does not exist in the nested map. This is a case that is not handled by
        the function, and it is important to test that the function behaves
        correctly in this case.

        Parameters:
            nested_map (dict): The nested dictionary to access.
            path (tuple): The path to the desired value in the nested
            dictionary.

        Returns:
            None
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
     implement the TestGetJson.test_get_json
     method to test that utils.get_json returns the expected result.
    """
    @parameterized.expand([
        (
            "http://example.com",
            {"payload": True},
            "Test that get_json returns the expected result for a valid URL.",
        ),
        (
            "http://holberton.io",
            {"payload": False},
            "Test that get_json returns the expected result for a valid URL.",
        ),
    ])
    def test_get_json(self, url, payload, description):
        """
        Test that get_json returns the expected result for a valid URL.

        Parameters:
            url (str): The URL to test.
            payload (dict): The expected result of get_json(url).

        Returns:
            None
        """
        # Replace the requests.get function with a mock that returns a
        # Mocked object that returns the payload.
        class Mocked(Mock):
            """
            Class that inherits from Mock.
            """

            def json(self):
                """
                json returning a payload
                """
                return payload

        with patch("requests.get") as MockClass:
            # Set the return value of the patched requests.get to a Mocked
            # object.
            MockClass.return_value = Mocked()
            # Call get_json(url) and assert that the result is equal to the
            # expected payload.
            self.assertEqual(get_json(url), payload)


class TestMemoize(unittest.TestCase):
    ''' memoize unittest '''

    def test_memoize(self):
        ''' memoize test '''

        class TestClass:
            ''' self descriptive'''

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mocked:
            spec = TestClass()
            spec.a_property
            spec.a_property
            mocked.asset_called_once()
