from collections import defaultdict
# n = 30
# is_prime = [True for i in range(n+1)]
# is_prime[0], is_prime[1] = False, False
# for i in range(2, int(n**1/2 + 1)):
#     if is_prime[i]:
#         for j in range(i*i, n+1, i):
#             is_prime[j] = False

# for i, v in enumerate(is_prime):
#     if v == True:
#         print(i)

global is_prime
is_prime = defaultdict(lambda: True)
is_prime[0] = False
is_prime[1] = False

max_calculated = [2]


def solve(n):
    ans = []
    for i in range(max_calculated[0], int(n**1/2 + 1)):
        if is_prime[i]:
            # print(i)
            for j in range(i*i, n+1, i):
                is_prime[j] = False

    max_calculated[0] = max(max_calculated[0], n)
    print(is_prime)

    for i in range(n+1):
        if is_prime[i]:
            ans.append(i)
    return " ".join(map(str, ans))


t = int(input())

res = []
for _ in range(t):
    n = int(input())
    res.append(solve(n))

for x in res:
    print(x)
