# fuck this
from math import log2, floor

N, M = map(int, input().split())
arr = list(map(int, input().split()))
queries = []
for _ in range(M):
    queries.append(list(map(int, input().split())))


def solve(arr, queries):
    N = len(arr)
    P = floor(log2(N))  # p is for power
    print('bigp', P)

    dp = [[0 for _ in range(N)] for _ in range(P+1)]

    for i in range(N):
        dp[0][i] = arr[i]

    # cell (i, j) = left interval (j, j + 2**(p-1)) + right interval (j + 2**(p-1), j + 2**p)
    for p in range(1, P+1):
        for i in range(N+1 - 2**p):
            left = dp[p-1][i]
            right = dp[p-1][i + 2**(p-1)]
            dp[p][0] = max(left, right)

    def lookup(queries):
        count = 0
        for query in queries:
            l, r = query
            l -= 1
            r -= 1

            if l+1 == r:
                count += 1
            else:
                _range = (r-1) - (l+1) + 1
                _l = l + 1
                _r = r - 1
                p = floor(log2(_range))
                print(p, l)
                left = dp[p][_l]
                # pr
                right = dp[p][_r-(2**p)+1]
                max_height = max(left, right)
                if max_height <= arr[l]:
                    count += 1
        return count

    return lookup(queries)


print(solve(arr, queries))
