"""
This implements the trial division algorithm.  It tries integers from 2 to sqrt(n).
"""
import math


def trial(n):
    factors = []
    i = 2
    while i <= math.floor(math.sqrt(n)):
        if n % i == 0:
            factors.append(i)
            n //= i
        else:
            i += 1
    return factors


def test():
    """Check if algo returns correct results:
         trial(4)  --> [2, 2]
         trial(6)  --> [2, 3]
         trial(7)  --> [7]
         trial(11) --> [11]
         trial(64) --> [2, 2, 2, 2, 2, 2]
    """
    print("Trying trial(4), expecting [2, 2]")
    print("Got: " + str(trial(4)))
    print("\nTrying trial(6), expecting [2, 3]")
    print("Got: " + str(trial(6)))
    print("\nTrying trial(100), expecting [2, 2, 5, 5]")
    print("Got: " + str(trial(100)))


if __name__ == "__main__":
    test()

