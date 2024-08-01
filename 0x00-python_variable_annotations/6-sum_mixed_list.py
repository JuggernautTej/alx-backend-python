#!/usr/bin/env python3
"""This is a type-annoted function that
takes a list mxd_lst of integers and floats
as an argument and returns their sum as a float."""

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """This is a type-annoted function that
    takes a list mxd_lst of integers and floats
    as an argument and returns their sum as a float.
    Args:
        mxd_list: a list of integers and floats.
    Returns:
        The sum of the elements as a float."""
    sum: float = 0
    for values in mxd_list:
        sum += values
    return float(sum)
