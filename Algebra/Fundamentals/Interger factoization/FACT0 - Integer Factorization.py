from collections import Counter


def integer_fact(n):
    res = []
    for i in range(2, int(n**1/2 + 1)):
        while n % i == 0:
            res.append(i)
            n /= i
    if n > 1:
        res.append(n)
    count = Counter(res)
    s = []
    for k, v in count.items():
        s.append(f"{k}^{v}")
    return " ".join(s)


res = []
n = int(input())
print(integer_fact(n))

a = [1, 3, 2, 3, 1]


def cond()


def conditional_sort(ls, f):
    y = iter(sorted(w for w in ls if f(w)))
    return [w if not f(w) else next(y) for w in ls]


conditional_sort(a, lambda x: x != -1)
