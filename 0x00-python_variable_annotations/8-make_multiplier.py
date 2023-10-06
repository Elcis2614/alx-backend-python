#!/usr/bin/env python3
"""
   annotation with callable
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
       takes a float multiplier as argument and returns a
       function that multiplies a float by multiplier.
    """
    return lambda factor: factor * multiplier
