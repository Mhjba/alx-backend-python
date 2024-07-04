#!/usr/bin/env python3

""" Annotated sum_mixed_list """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """  returns sum as a float. """
    return float(sum(mxd_lst))
