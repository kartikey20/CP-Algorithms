from itertools import combinations
from math import floor, log2


n, k = map(int, input().split())
arr = list(map(int, input().split()))


def solve(arr, k):
    N = len(arr)
    P = floor(log2(N))
    dp = [[0 for _ in range(N)] for _ in range(P+1)]

    for i in range(N):
        print(i)
        dp[0][i] = arr[i]

    for p in range(1, P+1):
        for i in range(N+1 - 2**p):
            left = dp[p-1][i]
            right = dp[p-1][i+2**(p-1)]
            dp[p][i] = min(left, right)

    def lookup(N, k):
        res = []
        lst = [i for i in range(N)]
        for x in combinations(lst, k):
            print(x)
            l, r = x[0], x[-1]
            _range = r - l + 1
            p = floor(log2(_range))
            left = dp[p][l]
            right = dp[p][r - 2**p + 1]
            res.append(min(left, right))
        return res
    ans = lookup(N, k)
    return max(ans)


print(solve(arr, k))
