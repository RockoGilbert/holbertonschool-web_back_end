#!/usr/bin/env python3
"""
Will wait_random n times the
with the specified max delay
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """[Summary]

    Args:
        n (int): [description]
        max_delay (int): [description]

    Returns:
        List[float]: [Return the list of all the delays]

    """
    lst = [await wait_random(max_delay) for i in range(n)]
    return sorted(lst)
