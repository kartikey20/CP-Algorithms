# TLE, Not Accepted

T = int(input())
res = []
for _ in range(T):
    n, p = map(int, input().split())
    res.append(str(pow(n, p)))
for i in res:
    print(f'{i[:3]}...{i[-3:]}')
