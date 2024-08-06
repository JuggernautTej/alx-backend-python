#!/usr/bin/env python3
"""A coroutine that takes no arguments,
executes async_comprehension four times in
parallel, and returns the total runtime."""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """A coroutine that takes no arguments,
    executes async_comprehension four times in
    parallel, and returns the total runtime.
    Args:
        none.
    Returns:
        Float: the total runtime of the function in seconds."""
    start_t = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_t = time.perf_counter()
    result = end_t - start_t
    return result
