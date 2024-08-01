#!/usr/bin/env python3
"""This is a type-annoted function that
takes a float multiplier as an argument
and returns a function that multiplies
a float by multiplier."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """This is a type-annoted function that
    takes a float multiplier as an argument
    and returns a function that multiplies
    a float by multiplier.
    Args:
        multiplier: a float object.
    Returns:
        A function."""
    def multiplier_function(value: float) -> float:
        """A function that multiplies
        a float by the multiplier."""
        return value * multiplier

    return multiplier_function
