from collections import Counter
import math


def factorize(n):
	"""Returns the non-unique prime factors of n as a list"""

	factors = []
	divisor = 2
	while divisor <= math.sqrt(n):
		if n % divisor == 0:
			factors.append(divisor)
			n = n // divisor
			divisor = 2
		elif divisor % 2 == 0:
			divisor += 1
		else:
			divisor += 2
	factors.append(n)
	return factors


def prime_factorization_with_exponents(n):
	"""Returns a dictionary of the prime factorization of n,
	keyed on prime factors, values their exponents"""

	prime_factors = factorize(n) # Returns something like [2, 2, 7]
	exponents = Counter(prime_factors) # Returns something like {2: 2, 7: 1}
	return exponents


def number_of_divisors(n):
	"""Calculates the number of divisors of n"""

	exponents = prime_factorization_with_exponents(n).values()
	return math.prod([exponent + 1 for exponent in exponents])


def find_triangle_number_with_over_n_divisors(n):
	"""Generates triangle numbers until a number is found
	such that it has over n divisors.  Return that number."""

	i = 2
	triangle_number = 1
	while number_of_divisors(triangle_number) <= n:
		triangle_number += i
		i += 1
	return triangle_number


print(find_triangle_number_with_over_n_divisors(500))