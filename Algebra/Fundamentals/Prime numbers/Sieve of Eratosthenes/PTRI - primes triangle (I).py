from collections import defaultdict


def sieve(n):
    is_prime = defaultdict(lambda: True)
    is_prime[0] = True
    is_prime[1] = True
    for i in range(2, int(n**1/2 + 1)):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False


res = []
T = int(input())
for _ in range(T):
    n = int(input())
    res.append(sieve(n))
