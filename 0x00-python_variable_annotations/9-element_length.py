#!/usr/bin/env python3
""" Annotate the below """
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Computes the length """
    return [(i, len(i)) for i in lst]
