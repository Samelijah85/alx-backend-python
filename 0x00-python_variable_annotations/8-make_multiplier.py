#!/usr/bin/env python3
"""A module to demonstrate the make_multiplier function."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Takes a float multiplier as an argument and returns a function
    that multiplies a float by the multiplier.

    Args:
        multiplier (float): The multiplier to use

    Returns:
        Callable[[float], float]: A function that multiplies a float by the
        multiplier
    """
    def multiply(n: float) -> float:
        """
        Multiply a float by the multiplier.

        Args:
            n (float): The float to multiply

        Returns:
            float: The result of multiplying x by the multiplier
        """
        return n * multiplier

    return multiply
