def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b, gcd):
    return a * b // gcd


def solve(x, y):

    _gcd = gcd(x, y)

    _lcm = lcm(x, y, _gcd)

    return " ".join(map(str, (_gcd, _lcm)))


try:
    T = int(input())
    res = []
    for _ in range(T):
        a, b = map(int, input().split())
        res.append(solve(a, b))

    for x in res:
        print(x)

except EOFError as e:
    print(end="")
