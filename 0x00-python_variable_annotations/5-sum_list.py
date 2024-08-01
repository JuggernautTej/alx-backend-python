#!/usr/bin/env python3
"""This is a type-annoted function that
takes a list input_list of floats as an argument
and returns their sum as a float."""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """This is a type-annoted function that
    takes a list input_list of floats as an argument
    and returns their sum as a float.
    Args:
        input_list: a list of floats.
    Returns:
        The sum of the elements as a float."""
    sum: float = 0
    for values in input_list:
        sum += values
    return float(sum)
