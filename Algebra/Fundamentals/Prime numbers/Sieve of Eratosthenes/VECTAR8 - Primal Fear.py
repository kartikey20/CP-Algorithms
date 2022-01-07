from collections import defaultdict


def solve(n):
    count = 0
    is_prime = defaultdict(lambda: True)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**1/2 + 1)):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False

    for i in range(n+1):
        if is_prime[i]:
            str_n = str(i)
            if all([is_prime[int(str_n[i:])] for i in range(len(str_n))]):
                count += 1
    return count


try:
    T = int(input())
    res = []
    for _ in range(T):
        n = int(input())
        res.append(solve(n))
    for x in res:
        print(x)
except:
    print(end="")
