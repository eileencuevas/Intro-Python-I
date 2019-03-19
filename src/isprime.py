import sys
import math


# def is_prime(potential_prime):
#     for num in range(2, int(potential_prime) + 1):
#         if potential_prime % num == 0:
#             return print(False)
#     return print(potential_prime > 1)

def is_prime(potential_prime):
    limit = math.sqrt(potential_prime)

    for num in range(2, int(limit) + 1):
        if potential_prime % num == 0:
            return False
    return potential_prime > 1


# with sys.argv, it will return [ 'name of file', argument1, ]
print(is_prime(int(sys.argv[1])))
