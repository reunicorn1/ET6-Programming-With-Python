#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for is_in function.

Test categories:
    - Standard cases: typical number lists and strings
    - Edge cases: empty lists, strings found in both lists
    - Defensive tests: invalid inputs, assertions

Created on 2024-12-11
Author: Reem Osama
"""
import unittest
from ..is_in import is_in


class TestIsIn(unittest.TestCase):
    """Test suite for the is_in function"""
    # Standard test cases

    # Edga Cases
    def test_empty_list(self):
        """It sould work with empty lists"""
        self.assertEqual(count_between([1, 2, 3, 4, 5], 2, 4), 3)
    # Defensive Tests
    def test_invalid_word(self):
        """It should raise AssertionError if word isn't a string"""
        with self.assertRaises(AssertionError):
            is_in(1, ['1', '2'], ['3', '4'])

    def test_invalid_list(self):
        """It should raise AssertionError if any list isn't a list"""
        with self.assertRaises(AssertionError):
            is_in('h', 'hello', 'reem')

    def test_invalid_string(self):
        """It should raise AssertionError if list have non-string element"""
        with self.assertRaises(AssertionError):
            is_in('1', ['1', '2', 3], [])
