#!/usr/bin/env python3
"""A coroutine that takes no arguments and yields
random numbers."""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """A coroutine that takes no arguments and yields
    random numbers.
    Args:
        none.
    Returns:
        AsyncGenerator[float, none]: An asynchronous generator
        that yields random floats."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
