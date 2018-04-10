"""
This solves Problem 2 of Project Euler.  It finds the sum of all even
Fibonacci numbers below a specified upper bound (4,000,000)

Refer to http://blog.jeffshaul.com/euler-2-even-fibonacci-numbers/ for a
discussion of the solution.

Usage: python p2solution.py upper_bound
       python p2solution.py 4000000
"""
import math
import sys
PHI = (1 + math.sqrt(5))/2


def even_fib_sum(upper_bound):
	"""Calculates the sum of all even Fibonacci numbers below the
	upper bound.  The equation is very cumbersome so I've broken it up.
	"""
	index = find_index_even_fib(upper_bound)
	return (geo_series_sum(index/3, PHI, 3) - geo_series_sum(index/3, -PHI, -3)) / math.sqrt(5)


def find_index_even_fib(upper_bound):
	"""This finds the index number of the largest even Fibonacci number below
	upper_bound"""
	index = math.floor((math.log(upper_bound) + math.log(5)/2) / math.log(PHI))
	#print("The estimated index is " + str(index))

	# Check if it's divisible by 3 (i.e. the corresponding Fib. number is even)
	if index % 3 == 0:
		return index
	else:
		return index - 1


def geo_series_sum(upper_bound, base, constant):
	"""Calculates the sum of the generic geometric series:
	sum_{k=1}^{upper_bound} base^(constant * k)
	"""
	return (base**constant * (base**(constant * upper_bound) - 1)) / (base**constant - 1)


def main():
	"""Handle user input via command-line arguments."""
	try:
		upper_bound = int(sys.argv[1])
		print(math.floor(even_fib_sum(upper_bound)))
	except IndexError:
		print("Usage: python p2solution.py upper_bound")


if __name__ == "__main__":
	main()