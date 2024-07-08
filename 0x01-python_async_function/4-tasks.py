#!/usr/bin/env python3
""" tasks """
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ run an async function n times with max_delay """
    w_tasks = [task_wait_random(max_delay) for _ in range(n)]
    m_delays = await asyncio.gather(*w_tasks)
    return sorted(m_delays)
