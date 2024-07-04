#!/usr/bin/env python3
"""
This is a function that given the parameters and the
return values, add type annotations to the function
"""


from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(
        dct: Mapping[Any, T], key: Any, default: Union[T, None] = None
        ) -> Union[T, Any]:
    """Return values, add type annotations to the function"""

    if key in dct:
        return dct[key]
    else:
        return default
