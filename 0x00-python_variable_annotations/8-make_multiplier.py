#!/usr/bin/env python3

"""
Module with type-annotated function 'make_multiplier'
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Function that takes a float multiplier as argument and returns
    a function that multiplies a float by multiplier.
    """
    def multiplier_func(x: float) -> float:
        return x * multiplier
    return multiplier_func
