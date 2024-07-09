#!/usr/bin/env python3
"""
Module 1-concurrent_coroutines

Provides an asynchronous routine for managing multiple random delays
concurrently.
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Asynchronous routine that spawns `wait_random` n times with a specified
    maximum delay.

    Args:
        n (int): The number of times to spawn `wait_random`.
        max_delay (int, optional): The maximum delay in seconds for each
        `wait_random` call. Defaults to 10.

    Returns:
        List[float]: List of delays in ascending order.
    """
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
