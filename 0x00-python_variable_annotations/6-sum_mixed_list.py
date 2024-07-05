#!/usr/bin/env python3
"""
Implements a type-annotated function which takes a list of integers and floats
and returns their sum as a float.
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Takes a list of integers and floats and returns their sum as a float.

    Args:
        mxd_lst (list[int/float]): A list of integers and floats

    Returns:
        float: The sum of elements in the list
    """
    return sum(mxd_lst)
