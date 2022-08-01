"""
Classic Computer Science Problems in Python
Chapter 1: Small Problems
Section 1: The Fibonacci Sequence
"""
from functools import lru_cache
from typing import Dict
from typing import Generator


memo: Dict[int, int] = {0: 0, 1: 1}


def fib1(n: int) -> int:
    return fib1(n - 1) + fib1(n - 2)


def fib2(n: int) -> int:
    print("fib2 called")
    if n < 2:
        return n
    return fib2(n - 1) + fib2(n - 2)


def fib3(n: int) -> int:
    print("fib3 called")
    if n not in memo:
        memo[n] = fib3(n - 1) + fib3(n - 2)
    return memo[n]


@lru_cache(maxsize=None)
def fib4(n: int) -> int:
    print("fib4 called")
    if n < 2:
        return n
    return fib4(n - 2) + fib4(n - 1)


def fib5(n: int) -> int:
    print("fib5 called")
    if n == 0:
        return n
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
    return next


def fib6(n: int) -> Generator[int, None, None]:
    yield 0
    if n > 0:
        yield 1
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
        yield next


if __name__ == "__main__":
    import sys
    import time

    val = int(sys.argv[1])
    tic = time.perf_counter()
    for i in fib6(val):
        print(i)
    print(f"Time: {time.perf_counter() - tic:.2f}")
