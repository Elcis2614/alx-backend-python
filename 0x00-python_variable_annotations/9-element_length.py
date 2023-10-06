#!/usr/bin/env python3
"""
   Just annotating
"""

from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
       Annotated function
    """
    return [(i, len(i)) for i in lst]
