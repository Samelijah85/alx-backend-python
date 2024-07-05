#!/usr/bin/env python3
"""
Implements a type-annotated function that takes a string and an int OR float
as arguments and returns a tuple.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string and an int OR float as arguments and returns a tuple.
    The first element of the tuple is the string k.
    The second element is the square of the int/float v, annotated as a float.

    Args:
        k (str): The string
        v (int/float): Integer or float

    Returns:
        tuple: The tuple of string and float
    """
    return k, v * v
