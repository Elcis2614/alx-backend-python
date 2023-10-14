#!/usr/bin/env python3
"""
   Function wait_n executes multiple coroutines
   by importing wait_random ( in 0-basic_async_syntax.py)
"""


import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


def insertElement(element: float, lst: List[float]) -> None:
    """
       Insert a element at on the corresponding posision in
       a sorted list
    """
    for i in range(len(lst)):
        if element < lst[i]:
            lst.insert(i, element)
            break
    else:
        lst.append(element)


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
       takes in 2 int arguments (in this order): n and max_delay.
       Spawns wait_random n times with the specified max_delay
       Returns the list of all the delays (float values) in ascending order
    """
    lst = list()
    for i in range(n):
        random = await asyncio.gather(wait_random(max_delay))
        insertElement(random[0], lst)
    return lst
