#!/usr/bin/env python3
"""This is a type-annoted function that
takes a string k and an int OR float v as
arguments and returns a tuple. The first
element of the tuple is the string k.
The second element is the square of the
int/float v and should be annotated as a float."""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """This is a type-annoted function that
    takes a string k and an int OR float v as
    arguments and returns a tuple. The first
    element of the tuple is the string k.
    The second element is the square of the
    int/float v and should be annotated as a float.
    Args:
        k: a string object.
        v: either an integer or a float object.
    Returns:
        A tuple."""
    return (k, (v ** 2))
