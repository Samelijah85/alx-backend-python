#!/usr/bin/env python3
"""
Module to demonstrate zooming in on an array by repeating each element
a specified number of times.
"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zooms in on an array by repeating each element a specified number of times

    Args:
        lst (Tuple): The input array.
        factor (int, optional): The zoom factor. Defaults to 2.

    Returns:
        List: The zoomed-in array.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array: Tuple = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
