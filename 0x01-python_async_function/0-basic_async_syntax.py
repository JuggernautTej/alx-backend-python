#!/bin/usr/env python3
"""An asynchronous coroutine that takes an
integer argument that waits for a random delay between
0 and the integer in seconds and eventually returns it"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """This is an asynchronous coroutine that
    takes an integer, max_delay, as an argument with
    a default value of 10, waits for a random delay between
    0 and max_delay and returns it.
    Args:
        max_delay: an integer.
    Returns:
        The argument."""
    i: float = random.uniform(0, max_delay)
    await asyncio.sleep(i)
    return i
