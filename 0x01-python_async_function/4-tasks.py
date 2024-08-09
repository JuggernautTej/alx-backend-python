#!/usr/bin/env python3
"""An asynchronous routine that takes 2 int arguments
Spawns the wait_random n times with the specified max
delay and returns the list of all delays."""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """This is an asynchronous routine that
    takes spawns task_wait_random n times with the specified max_delay.
    Args:
        n: The number of times to spawn wait_random.
        max_delay: The maximum delay for wait_random..
    Returns:
        A list of all the delays in ascending order."""
    tasks = []
    delayed = []

    for _ in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)

    for task in asyncio.as_completed(tasks):
        delay = await task
        delayed.append(delay)

    return delayed
