#!/usr/bin/env python3
"""
Implements a type-annotated function which takes a list of floats as argument
and returns their sum as a float.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Takes a list of floats as argument and returns their sum as a float.

    Args:
        input_list (list[float]): The list of floats

    Returns:
        float: The sum of all floats in the list
    """
    return sum(input_list)
