#!/bin/usr/env python3
"""An asynchronous routine that takes 2 int arguments
Spawns the wait_random n times with the specified max
delay and returns the list of all delays."""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """This is an asynchronous routine that
    takes spawns wait_random n times with the specified max_delay..
    Args:
        n: The number of times to spawn wait_random.
        max_delay: The maximum delay for wait_random..
    Returns:
        A list of all the delays in ascending order.."""
    d_list = []
    delay_time = []

    for _ in range(n):
        spawn = wait_random(max_delay)
        d_list.append(spawn)
    for a_list in asyncio.as_completed(d_list):
        delay = await a_list
        delay_time.append(delay)
    return delay_time
