from sympy import divisors
import math


def divisors2(n):
    divirs = [1]
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divirs.extend([i, n//i])
    divirs.extend([n])
    return list(set(divirs))

# def interger_factorization()


print(divisors2(87))
# print(divisors(87))
