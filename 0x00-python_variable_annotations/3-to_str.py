#!/usr/bin/env python3
"""
Implements a type-annotated function that takes a float as argument and
returns the string representation of the float.
"""


def to_str(n: float) -> str:
    """
    Takes a float as argument and returns the string representation
    of the float.

    Args:
        n (float): The float

    Returns:
        str: The string representation
    """
    return str(n)
