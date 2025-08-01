#!/usr/bin/env python3
"""
Module: 8-make_multiplier

This module defines a function `make_multiplier` that returns
a multiplier function. The returned function takes a float and
returns the product of that float and a preset multiplier.

Example:
    >>> doubler = make_multiplier(2.0)
    >>> doubler(4.5)
    9.0
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a multiplier function.

    Args:
        multiplier (float): The constant multiplier value.

    Returns:
        Callable[[float], float]: A function that takes a float and
        returns it multiplied by `multiplier`.

    Example:
        >>> triple = make_multiplier(3.0)
        >>> triple(2.0)
        6.0
    """

    def multiply(x: float) -> float:
        """
        Multiply a float by the outer multiplier.

        Args:
            x (float): The value to multiply.

        Returns:
            float: The result of x multiplied by the outer `multiplier`.

        Example:
            >>> multiply(4.0)  # if multiplier = 3.0
            12.0
        """
        return x * multiplier

    return multiply
