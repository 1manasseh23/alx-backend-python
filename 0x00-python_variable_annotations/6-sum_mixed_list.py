#!/usr/bin/env python3
"""
This a type-annotated function sum_mixed_list which takes a list
mxd_lst of integers and floats
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns their sum as a float"""

    return sum(mxd_lst)
