# TLE, idk why, it's fast doubling method
N = int(input())


def fib(n):
    if n == 0:
        return (0, 1)
    else:
        a, b = fib(n // 2)
        c = a * (b * 2 - a)
        d = a * a + b * b
        if n % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)


Nth = fib(N)[0]
print(Nth % (pow(10, 9) + 7))
