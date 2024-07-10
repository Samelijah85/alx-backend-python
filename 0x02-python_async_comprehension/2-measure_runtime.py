#!/usr/bin/env python3
"""
Module: 2-measure_runtime

This module provides an asynchronous coroutine that measures the total runtime
of executing async_comprehension four times in parallel using asyncio.gather.
"""
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Asynchronous coroutine that executes async_comprehension four times in
    parallel using asyncio.gather.
    Measures the total runtime and returns it.

    Returns:
    - float: Total runtime in seconds.
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
