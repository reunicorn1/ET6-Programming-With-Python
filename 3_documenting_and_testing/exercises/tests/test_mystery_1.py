#!/usr/bin/env python3
"""
testing mystery_1

@author: Reem Osama
"""

import unittest
from ..mystery_1 import mystery_1

class TestMystery1(unittest.TestCase):
    """ Test the mystery_1 function"""
    def test_0(self):
        """it should evaluate 1, 2 to 3"""
        self.assertEqual(mystery_1(1, 2), 3)

    def test_1(self):
        """it should evaluate 5, -6 to -1"""
        self.assertEqual(mystery_1(5, -6), -1)

    def test_3(self):
        """It should evaluate my, self to myself"""
        self.assertEqual(mystery_1('my', 'self'), 'myself')

    def test_4(self):
        """it should evaluate [1, 2], [3] to [1, 2, 3]"""
        self.assertEqual(mystery_1([1, 2], [3]), [1, 2, 3])

