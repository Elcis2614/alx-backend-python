#!/usr/bin/env python3
"""
   Adapting the code  to mypy
"""

from typing import Tuple, List, Any


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
       zoom in the array by a given factor
    """
    zoomed_in: List[Tuple] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
