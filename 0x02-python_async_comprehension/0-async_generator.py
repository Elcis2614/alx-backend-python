#!/usr/bin/env pythn3
"""
   async_generator : a coroutine that takes no argument
   and uses random module to generate integers
"""

import asyncio
import random


async def async_generator() -> None:
    """
       It loops 10 times, each time asynchronously wait 1 second,
       then yield a random number between 0 and 10
    """
    random.seed(220)
    for i in range(10):
        await asyncio.sleep(1)
        yield 10 * random.random()
