def fib_sum(n):
    s = 0
    arr = [0, 1]
    for i in range(2, n):
        val = arr[i-1] + arr[i-2]
        if val > n:
            break
        elif val <= n:
            arr.append(val)
            if arr[i] % 2 == 0:
                s += arr[i]
    return s


def solve(n):
    res = fib_sum(n)
    return res


res = []
T = int(input())
for _ in range(T):
    n = int(input())
    res.append(solve(n))

for x in res:
    print(x)
