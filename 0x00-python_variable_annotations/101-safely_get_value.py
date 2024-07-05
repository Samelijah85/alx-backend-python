#!/usr/bin/env python3
"""
Module to demonstrate safe retrieval of values from a dictionary.
"""
from typing import Any, Mapping, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) \
      -> Union[Any, T]:
    """
    Safely retrieves a value from a dictionary based on a key.

    If the key exists in the dictionary, returns the corresponding value.
    Otherwise, returns the provided default value.

    Args:
        dct (Mapping): The dictionary to retrieve the value from.
        key (Any): The key to look up in the dictionary.
        default (Union[T, None], optional): The default value to return if the
        key is not found. Defaults to None.

    Returns:
        Union[Any, T]: The value corresponding to the key in the dictionary
        or the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
