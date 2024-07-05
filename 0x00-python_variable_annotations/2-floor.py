#!/usr/bin/env python3
"""
Implements a type-annotated function which takes a float as argument and
returns the floor of the float.
"""
import math


def floor(n: float) -> int:
    """
    Takes a float as argument and returns the floor of the float

    Args:
        n (float): The float

    Returns:
        int: The floor of the float
    """
    return math.floor(n)
