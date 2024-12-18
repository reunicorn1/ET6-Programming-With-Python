#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for sum_even_and_odd function.

Test categories:
    - Standard cases: typical number lists and strings
    - Edge cases: empty lists, strings found in both lists
    - Defensive tests: invalid inputs, assertions

Created on 2024-12-12
Author: Reem Osama
"""
import unittest
from ..sum_evens_and_odds import sum_even_and_odd


class TestSumEvenAndOdd(unittest.TestCase):
    """Test suite for the is_in function"""
    # Standard test cases
    def test_default_list(self):
        """A list full of positive integers"""
        expected = {'even': 6, 'odd': 4}
        self.assertEqual(sum_even_and_odd([1, 2, 3, 4]), expected)

    def test_all_even(self):
        """A list full of all even numbers"""
        expected = {'even': 20, 'odd': 0}
        self.assertEqual(sum_even_and_odd([2, 4, 6, 8]), expected)

    def test_all_odd(self):
        """A list full of all odd numbers"""
        expected = {'even': 0, 'odd': 16}
        self.assertEqual(sum_even_and_odd([1, 3, 5, 7]), expected)

    def test_mixed_int(self):
        """A list of a mix of odd and even numbers"""
        expected = {'even': 2, 'odd': -2}
        self.assertEqual(sum_even_and_odd([-3, -2, 1, 4]), expected)

    # Edga Cases
    def test_empty_list(self):
        """It sould work with empty lists"""
        self.assertEqual(sum_even_and_odd([]), {'even': 0, 'odd': 0})

    def test_negative_ints(self):
        """testing the function with summing negative numbers"""
        expected = {'even': -6, 'odd': -4}
        self.assertEqual(sum_even_and_odd([-1, -2, -3, -4]), expected)

    def test_large_nums(self):
        """testing large numbers to be handled by the function"""
        expected = {'even': 1000000000, 'odd': 1000000001}
        self.assertEqual(sum_even_and_odd([10**9, 10**9+1]), expected)

    def test_zero_in_list(self):
        """testing a list with zero as an element"""
        expected = {'even': 6, 'odd': 0}
        self.assertEqual(sum_even_and_odd([0, 2, 4]), expected)

    def test_single_num(self):
        """testing a list with only one element"""
        expected = {'even': 2, 'odd': 0}
        self.assertEqual(sum_even_and_odd([2]), expected)

    # Defensive Tests
    def test_invalid_list(self):
        """It should raise AssertionError if nums isn't a list"""
        with self.assertRaises(AssertionError):
            sum_even_and_odd('error')

    def test_invalid_elements(self):
        """It should raise AssertionError if list don't contain integers"""
        with self.assertRaises(AssertionError):
            sum_even_and_odd(['1', '2', '3'])

    def test_float_numbers(self):
        """It should fail with any type of numbers other than int"""
        with self.assertRaises(AssertionError):
            sum_even_and_odd([1.44, 42.13, 5.21, 1.33])
