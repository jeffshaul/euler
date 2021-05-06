import sys, math
sys.path.insert(1, 'C:/Users/Jeff/Google Drive/Coding/Exercises/euler/algos/elliptical') # Sorry
from lattice_points import find_quadrant1_lattice_points_of_ellipse
from lattice_points import find_quadrant1_lattice_points_of_hyperbola


def sieve_of_atkins(limit):
	"""Returns all prime numbers up to limit.  The limit must be above 5."""
	
	results = [2, 3, 5]	
	sieve = {i: False for i in range(1, limit)}
	
	for number in sieve:
		remainder = number % 60
		
		# Step 3a
		if remainder in {1, 13, 17, 29, 37, 41, 49, 53}:
			number_of_integer_solutions = len(find_quadrant1_lattice_points_of_ellipse(number, 4, 1))
			for i in range(number_of_integer_solutions):
				sieve[number] = not sieve[number]

		# Step 3b
		if remainder in {7, 19, 31, 43}:
			number_of_integer_solutions = len(find_quadrant1_lattice_points_of_ellipse(number, 3, 1))
			for i in range(number_of_integer_solutions):
				sieve[number] = not sieve[number]

		# Step 3c
		if remainder in {11, 23, 47, 59}:
			number_of_integer_solutions = len(find_quadrant1_lattice_points_of_hyperbola(number, 3, -1)) 
			for i in range(number_of_integer_solutions):
				sieve[number] = not sieve[number]

	# Steps 4-7
	for number in sieve:
		if sieve[number] == False:
			continue
		else:
			results.append(number)
			square = number**2
			max_multiple = math.floor(limit / square)
			for multiple in range(1, max_multiple + 1):
				sieve[multiple * square] = False

	return results