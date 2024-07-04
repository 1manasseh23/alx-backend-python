#!/usr/bin/env python3
"""
This a type-annotated function sum_list which takes a list
input_list of floats as argument
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """Returns their sum as a float"""

    return sum(input_list)
