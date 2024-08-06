#!/usr/bin/env python3
"""A coroutine that takes no arguments, collects 10 random numbers
and returns those 10 random numbers."""

import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """A coroutine that takes no arguments, collects 10 random numbers
    from the async_generator function and returns those 10 random
    numbers.
    Args:
        none.
    Returns:
        List[float]: An asynchronous generator
        that yields random floats."""
    # result = asyncio.run(async_generator())
    result = [i async for i in async_generator()]
    return result
