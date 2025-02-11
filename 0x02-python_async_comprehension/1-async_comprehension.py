#!/usr/bin/env python3
"""
This a function that import async_generator from the previous
task and then write a coroutine called async_comprehension
that takes no arguments the coroutine will collect 10 random
numbers using an async comprehensing over async_generator,
then return the 10 random numbers
"""

import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """
    A coroutine that collects 10 random numbers
    using an async comprehension over async_generator
    then returns the 10 random numbers
    """

    return [i async for i in async_generator()]
