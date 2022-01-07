from os import defpath


from collections import defaultdict


def sieve(n):
    is_prime = defaultdict(lambda: True)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**1/2+1)):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    res = []
    col = 0
    for i in range(1, n+1):
        temp = i
        ans = []
        while temp > 0:
            if is_prime[i]:
                ans.append(i)
                temp -= 1
            i += 1
        res.append(ans)
    print(res)


res = []
T = int(input())
for _ in range(T):
    n = int(input())
    res.append(sieve(n))
