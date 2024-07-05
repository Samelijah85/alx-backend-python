#!/usr/bin/env python3
"""A module that demonstrate the element_length function."""
from typing import Iterable, Tuple, Sequence, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes a list of Sequence and return a list of tuples.
    The first element of the tuple is the Sequence.
    The second element of the tuple is the number of characters in the Sequence

    Args:
        lst (Iterable[Sequence]): A list of Sequences

    Returns:
        List[Tuple[Sequence, int]]: The list of tuples
    """
    return [(i, len(i)) for i in lst]
