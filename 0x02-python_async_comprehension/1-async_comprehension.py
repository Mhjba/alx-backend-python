#!/usr/bin/env python3
"""async comprehension"""

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """The coroutine will collect 10 random numbers """
    num = [i async for i in async_generator()]
    return num
