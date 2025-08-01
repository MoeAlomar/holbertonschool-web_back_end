#!/usr/bin/env python3
"""
Module: 4-tasks

Provides a coroutine `task_wait_n` that runs `task_wait_random`
multiple times concurrently and returns their delays in ascending order.
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Run `task_wait_random` n times concurrently and collect the delays.

    Args:
        n (int): Number of concurrent tasks to run.
        max_delay (int): Maximum delay for each task.

    Returns:
        List[float]: List of delays in ascending order of completion.
    """
    delays = []

    # Create and schedule n tasks
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    # Collect results in the order they complete
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
