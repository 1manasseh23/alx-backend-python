#!/usr/bin/env python3
from typing import Tuple, List

def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> Tuple[int, ...]:
    """Return type of the function"""

    zoomed_in: Tuple[int, ...] = tuple(
            item
            for item in lst
            for _ in range(factor)
    )
    return zoomed_in
array = [12, 72, 91]

zoom_2x = zoom_array(tuple(array))

zoom_3x = zoom_array(tuple(array), 3)
