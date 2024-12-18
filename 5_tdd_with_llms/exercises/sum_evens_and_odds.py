#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Sum Evens and Odds

Write a function that takes a list of numbers
and returns a dictionary with sums of the even and odd numbers in the list.

"""

def sum_even_and_odd(num_list: list) -> dict:
    """Takes a list of numbers and returns a dictonary with two elements
    even and odd, each one correspond to the sum of all even numbers, and
    the sum of all odd numbers that are available in the list.

    Parameters:
        num_list: list, a list of integers (not floats)

    Returns -> a dict: The dictionary has two keys, even and odd, with
    the value of the sum of each category of numbers

    Raises:
        AssertionError: if the num_list isn't a list or containing non-integers

    Examples:
        >>> sum_even_and_odd([1, 2, 3, 4])
        {'even': 6, 'odd': 4}
        >>> sum_even_and_odd([5,2,6,-1])
        {'even': 8, 'odd': 4}
        >>> sum_even_and_odd([7,1,1,1])
        {'even': 0, 'odd': 10}

    """
    # Checking the type
    assert isinstance(num_list, list), "The num_list must be a list"
    assert all(isinstance(num, int) for num in num_list)

    dictionary = {'even': 0, 'odd': 0}
    for num in num_list:
        if num % 2 == 0:
            dictionary['even'] += num
        else:
            dictionary['odd'] += num
    return dictionary
