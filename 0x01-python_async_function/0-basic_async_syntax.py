#!/usr/bin/env python3
""" Basics of async """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Waits for a random number of seconds. """
    m_delay = random.uniform(0, max_delay)
    await asyncio.sleep(m_delay)
    return m_delay
