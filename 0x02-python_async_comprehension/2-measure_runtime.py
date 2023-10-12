#!/usr/bin/env python3
"""
   calculating runtime
"""


import asyncio
import time
async_generator = __import__('0-async_generator').async_generator


async def measure_runtime() -> float:
    """
       execute async_comprehension four times in
       parallel using asyncio.gather
    """
    start = time.perf_counter()
    await asyncio.gather(async_generator(), async_generator(), async_generator(), async_generator())
    elapsed = time.perf_counter() - start
    return (elapsed)
