#!/usr/bin/env python3

from typing import Tuple, List


def zoom_array(lst: Tuple[int, ...],
               factor: int = 2) -> List[int]:
    """
    Zooms in on the elements of a tuple
    by repeating them based on the factor.
    Args:
        lst (Tuple[int, ...]): The input tuple of integers.
        factor (int): The zoom factor (default is 2).

    Returns:
        List[int]: A list containing zoomed-in elements.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
