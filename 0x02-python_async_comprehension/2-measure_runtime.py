#!/usr/bin/env python3
"""
This a function that import async_comprehension from the previous
file and write a measure_runtime coroutine that will execute
async_comprehension four times in parallel using asyncio.gather.
measure_runtime should measure the total runtime and return it.

Notice that the total runtime is roughly 10 seconds, explain it to yourself:)
"""

import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """
    A coroutine that measures the total runtime of executing
    async_comprehension four times in parallel
    """
    start_time = asyncio.get_running_loop().time()
    await asyncio.gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension()
    )
    end_time = asyncio.get_running_loop().time()
    return end_time - start_time
