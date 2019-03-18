import sys
import math
from isprime import is_prime

# def is_prime(potential_prime):
#     limit = math.sqrt(potential_prime)

#     for num in range(2, int(limit) + 1):
#         if potential_prime % num == 0:
#             return False
#     return potential_prime > 1


# implements the Sieve of Erathosthenes algorithm using the is_prime() function

def sieve(from_number, to_number):
    prime_numbers = [number
                     for number in range(int(from_number), int(to_number) + 1)
                     if is_prime(number)]
    return print(prime_numbers)


sieve(sys.argv[1], sys.argv[2])
