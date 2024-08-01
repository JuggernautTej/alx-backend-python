#!/usr/bin/env python3
"""This is a type-annoted function that
takes a list lst as an argument and
returns each item of the list along
with the lenght of each item."""

from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """This is a type-annoted function that
    takes a list lst as an argument and
    returns a each item of the list along
    with the lenght of each item.
    Args:
        lst: a list object.
    Returns:
        Each item of the list along with
        the lenght of each item."""

    return [(i, len(i)) for i in lst]
