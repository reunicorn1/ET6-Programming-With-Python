#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Is in

Write a function that takes in a string and two lists of strings.
It will return true if the item is in _at least one_ of the lists.

"""

def is_in(word: str, first_list: list, second_list: list) -> bool:
    """Identifies if a string is found in one of the two lists given

    This function takes a string and two lists of words, and returns a bool of
    whether the word is found in either of the lists or not.

    Parameters:
        text: str, the word to look for
        first_list: the first list to look for the word in
        second_list: the second list to for the word in

    Returns -> bool: True if the word is found in either of the lists, and
    False if not found in neither.

    Raises:
        AssertionError: if the word isn't a string, if any of the lists isn't
        a list, or if they don't contain all strings.

    Examples:
        >>> is_in('hello', ['hi', 'hola'], ['hey', 'haya'])
        False
        >>> is_in('reem', ['lina', 'raghed', 'omer'], ['reem'])
        True
        >>> is_in('jasmine', ['sunflowers', 'jasmine'], ['jasmine', 'rose'])
        True
    """
    assert isinstance(word, str), "The word to look for must be a string"
    assert isinstance(first_list, list), "First list must be a 'list'"
    assert isinstance(first_list, list), "First list must be a 'list'"
    assert all(isinstance(word, string) for word in first_list + second_list)

