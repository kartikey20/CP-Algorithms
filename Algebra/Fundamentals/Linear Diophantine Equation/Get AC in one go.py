def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def solve(a, b):
    if gcd(a, b) == 1:
        return a*b-a-b+1
    else:
        return -1


try:
    res = []
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        res.append(solve(a, b))

    for x in res:
        print(x)
except:
    print(end="")
