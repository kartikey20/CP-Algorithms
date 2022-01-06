from math import gcd


def gcd1(a, b):
    x, y = 1, 0
    x1, y1 = 0, 1
    a1, b1 = a, b
    while b1:
        q = a1//b1
        x, x1 = x1, x-q*x1
        y, y1 = y1, y-q*y1
        a1, b1 = b1, a1 - q * b1
    return x, y


# print(gcd1(17, 17))


def gcd2(a, b):
    # x = 1
    # y = 0
    x1 = 0
    y1 = 1
    x = y1
    y = x1 - (a//b) * y1
    return x, y


print(gcd1(4, 6), gcd2(4, 6))
