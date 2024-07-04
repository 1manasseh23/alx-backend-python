#!/usr/bin/env python3
""""
This The code with the correct duck-typed annotations
"""


from typing import Sequence, Any, Union, Optional


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """To check by index"""

    if lst:
        return lst[0]
    else:
        return None
