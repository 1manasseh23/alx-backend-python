#!/usr/bin/env python3
"""
This a coroutine called async_generator that takes no
arguments the coroutine will loop 10 times, each time
asynchronously wait 1 second, then yield a random number
between 0 and 10. Use the random module
"""
import asyncio
import random


async def async_generator():
    """
    A coroutine that generates 10 random numbers between
    0 and 10, waiting 1 second between each yield.
    """

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
