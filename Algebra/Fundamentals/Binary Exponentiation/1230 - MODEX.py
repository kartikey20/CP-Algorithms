def solve(x, y, n):
    return pow(x, y, n)


res = []
T = int(input())
for _ in range(T):
    x, y, n = map(int, input().split())
    res.append(solve(x, y, n))
input()
for i in res:
    print(i)
