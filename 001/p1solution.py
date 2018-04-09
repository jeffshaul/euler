"""
This program solves Problem 1 of Project Euler.  Later on, it will be expanded
to support more than 2 multiples.  Instead of using (slow) iteration, we use
properties of sums and Gauss's discovery

Usage: python p1solution.py bound a b [...]
       python p1solution.py 1000 3 5
"""
import sys
import math


def sum_first_n_numbers(n):
    """Discovered by Gauss, helper function for sum_multiples_below_bound"""
    return n*(n+1)/2


def sum_multiples_below_bound(m1, m2, u):
    """Solution to Project Euler Problem #1"""
    return m1 * sum_first_n_numbers(math.ceil(u/m1 - 1)) + m2 * sum_first_n_numbers(math.ceil(u/m2 - 1)) - m1 * m2 * sum_first_n_numbers(math.ceil(u/(m1*m2) - 1))


if __name__ == "__main__":
    try:
        print(sum_multiples_below_bound(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[1])))
    except:
        print("Usage: python p1solution.py bound a b [...]")