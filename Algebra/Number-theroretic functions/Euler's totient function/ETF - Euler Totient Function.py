def euler_tolient(n):
    res = n
    for i in range(2, int(n**1/2+1)):
        if n % i == 0:
            while n % i == 0:
                n /= i
            res -= res/i
    if n > 1:
        res -= res/n
    return res


# print(gcd(4, 5))
print(euler_tolient(12158598919))
