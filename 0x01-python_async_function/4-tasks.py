#!/usr/bin/env python3
"""
This a code from wait_n and alter it into a new
function task_wait_n. The code is nearly identical
to wait_n except task_wait_random is being called.
"""


import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Takes two integer arguments (n and max_delay).
    Creates n tasks with task_wait_random(max_delay),
    and returns the list of all the delays (float values).
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
