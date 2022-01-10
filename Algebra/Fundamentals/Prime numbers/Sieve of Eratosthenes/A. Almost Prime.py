def trail_divison(n):
    fact = [1]
    for i in range(2, int(n**1/2+1)):
        while n % i == 0:
            fact.append(i)
            n /= i
    if n > 1:
        fact.append(n)
    return fact


print(trail_divison(28))
