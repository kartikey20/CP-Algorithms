from collections import defaultdict


def prime(n):
    ans = []
    is_prime = defaultdict(lambda: True)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**1/2 + 1)):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False

    for i in range(n+1):
        if is_prime[i]:
            ans.append(i)
    return " ".join(map(str, ans))


T = int(input())
res = []
for _ in range(T):
    n = int(input())
    res.append(prime(n))

for x in res:
    print(x)
