#!/usr/bin/env python3
"""
    Parameterizing a unit test
"""

from utils import access_nested_map
from unittest import TestCase
from parameterized import parameterized, parameterized_class
from typing import (
    Any,
    Mapping,
    Sequence
)

class TestAccessNestedMap(TestCase):
    """
        simple test class
    """
    @parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({'a': {'a': 2}}, ('a',), {'a': 2}),
        ({'a': {'b': 2}}, ('a', 'b'), 2),
        ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence, expected: Any) -> None:
        """
            Tests access_nested_map to ensure
            that the method returns what it is supposed to
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)


