from math import fmod


def fib_generator(n):
    arr = [0, 1]
    for i in range(n):
        arr.append(arr[i-1] + arr[i-2])
    return arr


def solve(n):
    fibonacci_seq = fib_generator(n % 10**9+7)
    for i in range(len(fibonacci_seq)):
        print(i, fibonacci_seq[i])


try:
    t = int(input())
    res = []
    for _ in range(t):
        n = int(input())
        res.append(solve(n))
    for x in res:
        print(x)
except:
    print(end="")
