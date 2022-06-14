#!/usr/bin/python3
"""The function returns a tuple of size
2 containing a start index and end index"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Args:
        page (int): [description]
        page_size (int): [description]

    Returns:
        Tuple[int, int]
    """

    start_index = (page * page_size) - page_size
    end_index = page * page_size
    return (start_index, end_index)
