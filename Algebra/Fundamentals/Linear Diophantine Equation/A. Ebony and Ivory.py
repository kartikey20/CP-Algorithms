a, b, c = map(int, input().split())


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


if c % gcd(a, b) == 0:
    print("Yes")
else:
    print("No")
