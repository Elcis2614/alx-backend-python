#!/usr/bin/env python3
"""
    Adding the appropriate annotation
"""


from typing import Mapping, Any, Union, TypeVar
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, type(None)] = None) -> Union[Any, T]:
    """
       simple funtion
    """
    if key in dct:
        return dct[key]
    else:
        return default
