#!/usr/bin/env python3

import asyncio
import random


async def wait_random(max_delay: int = 10):
    """
    Waits for a random delay between 0 and max_delay seconds,
    then returns the delay.
    Args:
        max_delay (float, optional): The maximum delay
        in seconds. Defaults to 10.
    Returns:
        float: The actual delay in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
