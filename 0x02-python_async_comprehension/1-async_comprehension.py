#!/usr/bin/env python3
"""This coroutine will collect 10 random numbers
using async_comprehension over async_generator
then returns 10 random numbers.
"""


from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Return a list of random numbers"""
    numbers = [i async for i in async_generator()]
    return numbers
