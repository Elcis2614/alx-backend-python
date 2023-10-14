#!/usr/bin/env python3
"""
    Measuring the total of execution of async function
    wait_n (see 1-concurrent_coroutines.py)
"""

import asyncio
from time import perf_counter

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
       Mearuses the total time of execution and return total_time / n
    """
    start = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = perf_counter() - start
    return total_time / n
