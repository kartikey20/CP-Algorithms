def computeHash(s, dic={}):
    if s in dic:
        return dic[s]
    hash = 0
    p = 53
    mod = 1e9 + 9
    pPow = 1
    for c in s:
        hash = (hash + (ord(c) * pPow)) % mod
        pPow = (pPow * p) % mod
    dic[s] = hash
    return hash


def solve():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        v, u = map(int, input().split())
        graph[v - 1].append(u - 1)
