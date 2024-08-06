#!/usr/bin/env python3
"""A coroutine that takes no arguments, collects 10 random numbers
and returns those 10 random numbers."""

import asyncio


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> float:
    # result = asyncio.run(async_generator())
    result = [i async for i in async_generator()]
    return result
