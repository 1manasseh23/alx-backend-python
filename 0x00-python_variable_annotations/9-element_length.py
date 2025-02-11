#!/usr/bin/env python3
"""
This annotate the function’s parameters
def element_length(lst):
        return [(i, len(i)) for i in lst]
and return values with the appropriate types
"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ return values with the appropriate types"""

    return [(i, len(i)) for i in lst]
