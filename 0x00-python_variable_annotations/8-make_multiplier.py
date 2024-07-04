from typing import Callable
""" multiplies a float by multiplier """

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function"""
    def f(value: float) -> float:
        """ multiplies a float by multiplier """
        return value * multiplier
    return f
