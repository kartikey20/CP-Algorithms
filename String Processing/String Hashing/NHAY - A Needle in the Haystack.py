# https://www.spoj.com/problems/NHAY/
def computeHash(s):
    hash = 0
    p = 53
    mod = 1e9 + 9
    pPow = 1
    for c in s:
        hash = (hash + (ord(c) - ord('a') + 1) * pPow) % mod
        pPow = (pPow * p) % mod
    return int(hash)

# Rabin-Karp Algorithm


def rabinKarp():
    n = int(input())
    needle = input()
    haystack = input()
    lenHaystack = len(haystack)
    needleHash = computeHash(needle)
    matches = []
    for i in range(lenHaystack):
        if needleHash == computeHash(haystack[i:i + n]):
            matches.append(i)
    return matches


print(rabinKarp())
