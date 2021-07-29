def computeHash(s):
    hash = 0
    p = 53
    mod = 1e9 + 9
    pPow = 1
    for c in s:
        hash = (hash + (ord(c) * pPow)) % mod
        pPow = (pPow * p) % mod
    return hash


def solve(S, P):
    StrLen = len(S)
    count = 0
    start, end, latter = (
        P, StrLen, True) if P > StrLen // 2 else (0, P, False)
    for i in range(start, end):
        if latter:
            if computeHash(S[i]) == computeHash(S[i - P]):
                count += 1
            else:
                break
        else:
            if computeHash(S[i]) == computeHash(S[i + P]):
                count += 1
            else:
                break
    return count


S = input()
Q = int(input())
P = []
for _ in range(Q):
    P.append(int(input()))
for x in P:
    print(solve(S, x))
