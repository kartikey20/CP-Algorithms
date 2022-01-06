def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def solve(a, b, d):
    if d % gcd(a, b) == 0:
        return "YES"
    else:
        return "NO"


try:
    T = int(input())
    res = []
    for _ in range(T):
        a, b, d = map(int, input().split())
        res.append(solve(a, b, d))
    for x in res:
        print(x)
except EOFError as e:
    print(end="")
