#!/usr/bin/env python3
"""
Module: 0-basic_async_syntax

Provides a coroutine `wait_random` that asynchronously waits
for a random delay between 0 and `max_delay` seconds and returns
the delay as a float.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously wait for a random delay between 0 and max_delay.

    Args:
        max_delay (int): Maximum delay in seconds (default is 10).

    Returns:
        float: The actual delay time that was waited.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
