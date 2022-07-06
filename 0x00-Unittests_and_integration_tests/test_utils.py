#!/usr/bin/env python3
"""Module for test_utils.py"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """ Defines the TestAccessNestedMap Class """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test that utils.access_nested_map returns the expected result"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test that an exception is raised"""
        with self.assertRaises(KeyError) as exception_context_manager:
            access_nested_map(nested_map, path)


class TestMemoize(unittest.TestCase):
    """ Defines the TestMemoize Class """
    def test_memoize(self):
        """ Tests that `memoize` method works as expected """
        class TestClass:
            """ Defines the TestClass Class """
            def a_method(self):
                """ Method that returns a numbers """
                return 42

            @memoize
            def a_property(self):
                """ Method that returns the `a_method` func """
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_method:
            test = TestClass()
            test.a_property()
            test.a_property()
            mock_method.assert_called_once()
