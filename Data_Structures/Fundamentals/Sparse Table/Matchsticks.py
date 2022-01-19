from math import floor, log2
from turtle import right


N = int(input())
arr = list(map(int, input().split()))
Q = int(input())

queries = []
for _ in range(Q):
    queries.append(list(map(int, input().split())))


def solve(arr, queries):
    N = len(arr)
    P = floor(log2(N))
    dp_min = [[0 for _ in range(N)] for _ in range(P+1)]
    dp_max = [[0 for _ in range(N)] for _ in range(P+1)]

    for i in range(N):
        dp_min[0][i] = arr[i]
        dp_max[0][i] = arr[i]

    for p in range(1, N+1):
        for i in range(N+1 - 2**p):
            left = dp_max[p-1][i]
            right = dp_min[p-1][i+2**(p-1)]
            dp_max[p][i] = max(left, right)
            dp_min[p][i] = min(left, right)

    def lookup(queries):
        res = []
        _M = max(arr)
        for query in queries:
            l, r = query
            _range = r - l+1
            p = floor(log2(_range))
            l_max = dp_max[p][l]
            r_max = dp_max[p][r-(2**p) + 1]
            M = max(l_max, r_max)
            print(M, arr[l], arr[r])
            l_min = dp_min[p][l]
            r_min = dp_min[p][r-(2**p) + 1]
            m = min(l_min, r_min)
            print(m)
            res.append(m + max((M-m)/2, _M))
        return res
    return lookup(queries)


ans = solve(arr, queries)
for x in ans:
    print(ans)
