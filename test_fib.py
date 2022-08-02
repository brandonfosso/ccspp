"""
Classic Computer Science Problems in Python
Chapter 1: Small Problems
Section 1: The Fibonacci Sequence

*** TESTING ***
"""

import fib
import pytest


@pytest.mark.parametrize("seed, result", [(1, 1), (4, 3), (5, 5)])
def test_fib2(seed, result):
    assert result == fib.fib2(seed)


@pytest.mark.parametrize("seed, result", [(1, 1), (4, 3), (5, 5)])
def test_fib3(seed, result):
    assert result == fib.fib3(seed)
