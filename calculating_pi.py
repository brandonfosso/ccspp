"""
Classic Computer Science Problems in Python
Chapter 1: Small Problems
Section 4: Calculating Pi
"""


def calculate_pi(n_terms: int) -> float:
    numerator: float = 4.0
    denominator: float = 1.0
    operation: float = 1.0
    pi: float = 0.0
    for _ in range(n_terms):
        pi += operation * (numerator / denominator)
        denominator += 2.0
        operation *= -1.0
    return pi


if __name__ == "__main__":
    import random
    import sys
    import time

    N = int(float(sys.argv[1]))
    print(calculate_pi(N))
