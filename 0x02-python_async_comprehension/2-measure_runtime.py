#!/usr/bin/env python3
"""
   calculating runtime
"""


import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
       execute async_comprehension four times in
       parallel using asyncio.gather
    """
    start = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    elapsed = time.perf_counter() - start
    return (elapsed)
