is_prime = [True for i in range(1000)]
is_prime[0] = False
is_prime[1] = False
n = 10


def sieve(n):
    for i in range(2, int(n**1/2 + 1)):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    return is_prime[n]


count = 0
for i in range(1, int(n**1/2+1)):
    for j in range(1, int(n**1/4+1)):
        if sieve(i*i + j*j*j*j):
            count += 1


print(count)
