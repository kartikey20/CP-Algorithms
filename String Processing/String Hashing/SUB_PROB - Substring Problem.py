def computeHash(s, dic={}):
    if s in dic:
        return dic[s]
    p = 53
    pPow = 1
    mod = 1e9 + 9
    hash = 0
    for c in s:
        hash = (hash + (ord(c) * pPow)) % mod
        pPow = (pPow * p) % mod
    dic[s] = hash
    return hash


hayStack = input()
hayStackLen = len(hayStack)
n = int(input())
needles = []
for i in range(n):
    needles.append(input())
res = []
for needle in needles:
    def solve():
        needleLen = len(needle)
        for i in range(hayStackLen - needleLen):
            if computeHash(hayStack[i:i + needleLen]) == computeHash(needle):
                return 'Y'
        else:
            return 'N'
    res.append(solve())

for r in res:
    print(r)
