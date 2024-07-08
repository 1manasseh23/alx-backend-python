#!/usr/bin/env python3
"""
Import wait_random from the previous python file that
you’ve written and write an async routine called wait_n
that takes in 2 int arguments (in this order)
"""


import asyncio
from typing import List
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """Returns a sorted list of delays"""

    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Returns a sorted list of delays"""

    tasks = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return sorted(results)
