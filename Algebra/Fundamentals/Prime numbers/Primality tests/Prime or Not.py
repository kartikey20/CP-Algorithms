def solve(n):
    if n == 1:
        return False
    if n == 0:
        return False
    for i in range(2, int(n**1/2 + 1)):
        if n % i == 0:
            return False
    return True


T = int(input())
res = []
for i in range(T):
    n = int(input())
    res.append(solve(n))
print(res)
