#!/usr/bin/env python3
"""
Module 3-tasks
Provides a function to create an asyncio.Task for the wait_random
coroutine from 0-basic_async_syntax.
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio.Task for wait_random with a specified
    max_delay.

    Parameters:
    - max_delay (int): The maximum delay in seconds for wait_random.

    Returns:
    - asyncio.Task: The asyncio task for wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))
