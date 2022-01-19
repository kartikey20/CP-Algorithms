from math import log2, floor

N = int(input())
arr = list(map(int, input().split()))
Q = int(input())
queries = []

for _ in range(Q):
    i, j = map(int, input().split())
    queries.append([i, j])


def solve(arr, queries):
    N = len(arr)
    P = floor(log2(N))   # p for power

    dp = [[0 for _ in range(N)] for _ in range(P+1)]

    for i in range(N):
        dp[0][i] = arr[i]

    # range (i, j) = left interval (j, j + 2**(p-1)) + right interval (j+2**(p-1), j+2**p)
    for p in range(1, P+1):
        for i in range(N+1-2**p):
            left = dp[p-1][i]
            right = dp[p-1][i+2**(p-1)]
            dp[p][i] = min(left, right)

    def lookup(queries):
        res = []
        for query in queries:
            l, r = query
            if l == r:
                res.append(arr[l])
            else:
                # [l, r] = [l, l+k] + [r-k+1, r]
                # might overlap but we don't care because min is overlap friendly
                _range = r - l + 1
                p = floor(log2(_range))
                left = dp[p][l]
                right = dp[p][r-2**p+1]
                res.append(min(left, right))
        return res

    return lookup(queries)


res = solve(arr, queries)

for x in res:
    print(x)
