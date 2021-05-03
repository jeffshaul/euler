import itertools, math


def generate_sorted_products_of_two_n_digit_numbers(n):
    """Runs a Cartesian product between all n digit numbers, then sorts them in decreasing order.

    Args:
        n (int): number of digits in the number

    Returns:
        list: a sorted list, in descending order, of the Cartesian product between all n-digit numbers
    """

    pairs = itertools.combinations_with_replacement(range(10**(n-1),10**n), 2)
    return sorted([pair[0] * pair[1] for pair in pairs], reverse = True)


def is_palindromic(n):
    """Non-string method of checking whether a number is palindromic or not
    
    Args:
        n (int): number to check for palindromicity
        
    Returns:
        bool: true if the number is palindromic, false otherwise    
    """
    
    digits = []
    while math.ceil(math.log(n, 10)) > 1:
        rightmost_digit_of_n = 10 * round(n / 10 - math.floor(n / 10), 1)
        n = math.floor(n / 10)
        digits.append(int(rightmost_digit_of_n))
    digits.append(n)
    reversed_digits = digits[::-1]
    return digits == reversed_digits


# Putting it together
products = generate_sorted_products_of_two_n_digit_numbers(3)
for product in products:
    if is_palindromic(product):
        print(product)
        break # Since the list is sorted in descending order, the first palindrome we encounter will be the largest.