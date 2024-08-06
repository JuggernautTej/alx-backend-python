#!/usr/bin/env python3
"""A function that tasks an integer max_delay and returns a
asyncio.Task."""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """This is a function that returns asyncio.Task.
    Args:
        max_delay: The maximum delay for wait_random..
    Returns:
        asyncio.Task.
    """
    t = asyncio.create_task(wait_random(max_delay))
    return t
