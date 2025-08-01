#!/usr/bin/env python3
"""
Module: 3-tasks

Defines a function `task_wait_random` that creates and returns
an asyncio Task from the `wait_random` coroutine.
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create and return an asyncio.Task that wraps `wait_random`.

    Args:
        max_delay (int): Maximum number of seconds to delay.

    Returns:
        asyncio.Task: A Task object representing the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
