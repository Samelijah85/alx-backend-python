#!/usr/bin/env python3
"""
Module 0-basic_async_syntax

Provides an asynchronous coroutine for generating a random delay.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously waits for a random duration between 0 and `max_delay`
    seconds, then returns the delay.

    :param max_delay: The maximum delay in seconds. Defaults to 10.
    :type max_delay: int
    :return: The delay in seconds.
    :rtype: float
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
