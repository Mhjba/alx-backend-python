#!/usr/bin/env python3
""" multiplies a float by multiplier """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function"""

    def f(v: float):
        """ multiplies a float by multiplier """
        return v * multiplier
    return f
