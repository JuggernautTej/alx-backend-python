#!/usr/bin/env python3
"""This is a type-annoted function that
takes a string str1 and a string str2 as arguments
and returns a concatenated string."""


def concat(str1: str, str2: str) -> str:
    """This is a type-annoted function that
    takes a string str1 and a string str2 as arguments
    and returns a concatenated string.
    Args:
        str1: a string object.
        str2: a string object.
    Returns:
        Concatenated string of the arguments."""
    return "{}{}".format(str1, str2)
