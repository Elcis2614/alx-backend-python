#!/usr/bin/env python3
"""
   DuckType Anotation
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, type(None)]:
    """
        Simple ducktyped function
    """
    if lst:
        return lst[0]
    else:
        return None
