#!/usr/bin/env python3
""" All unittests for utils.py module """
import unittest
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """Class testing utils.access_nest_map from utils.py"""

    @parameterized.expand([({"a": 1}, ("a",), 1),
                           ({"a": {"b": 2}}, ("a",), {"b": 2}),
                           ({"a": {"b": 2}}, ("a", "b"), 2)
                           ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Tests function with three different situations"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([({}, ("a",)),
                           ({"a": 1}, ("a", "b"))
                           ])
    