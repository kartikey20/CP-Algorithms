# https://codeforces.com/problemset/problem/126/B
# TODO: error on tc 4

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
    s = input()
    n = len(s)
    matches = []
    for i in range(2, n):
        prefixHash = computeHash(s[:i])
        suffixHash = computeHash(s[n - i:])
        prefixLen = len(s[:i])
        if prefixHash == suffixHash:
            for j in range(i, n - i + 1):
                if prefixHash == computeHash(s[j:j + prefixLen]):
                    matches.append(s[:i])
    return max(matches) if len(matches) > 0 else "Just a legend"


print(solve())
