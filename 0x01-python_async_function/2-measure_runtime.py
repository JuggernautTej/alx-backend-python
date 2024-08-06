#!/usr/bin/env python3
"""A function that measures the execution time for
the wait_n function."""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """A function that measures the average time for
    the wait_n function to execute.
        Args:
            n: The number of times to spawn wait_random.
            max_delay: The maximum delay for wait_random.
    Returns:
        The average time for the function to execute as a float
    """
    start_t = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_t = time.perf_counter()
    total_time = (end_t - start_t)
    result = total_time / n

    return result
