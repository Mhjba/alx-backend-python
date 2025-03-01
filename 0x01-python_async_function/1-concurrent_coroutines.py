#!/usr/bin/env python3
"""execute multiple coroutines at the same time with async"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """run an async function n times with max_delay """
    m_delays = await asyncio.gather(
     *(wait_random(max_delay) for _ in range(n)))
    return sorted(m_delays)
