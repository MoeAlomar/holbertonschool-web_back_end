#!/usr/bin/env python3
"""
Module: 1-concurrent_coroutines

Provides a coroutine `wait_n` that concurrently runs `wait_random`
n times and returns the list of delays in ascending order,
based on natural task completion timing.
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Run `wait_random` concurrently n times with max_delay.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay for each coroutine.

    Returns:
        List[float]: List of delays in ascending order (by completion time).
    """
    delays = []

    # Create and schedule n wait_random coroutines
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    # As tasks complete, collect their results in order of completion
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
