#!/usr/bin/env python3
"""Import async comprehenson and write a measure_runtime
coroutine that will execute async_comprehension
4  times in parallel using asyncio.gather
"""


import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Should measure the runtime"""
    start: float = time.time()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end: float = time.time()
    return end - start
