#!/usr/bin/env python3
"""
Module 2-measure_runtime

Provides a function to measure the average execution time for the wait_n
asynchronous routine from async_delay_manager.
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the average execution time for wait_n(n, max_delay).

    Parameters:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay in seconds for each wait_random call

    Returns:
        float: The average execution time per wait_random call.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start_time) / n
