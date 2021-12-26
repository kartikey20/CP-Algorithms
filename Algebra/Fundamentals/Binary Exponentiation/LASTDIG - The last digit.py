n = int(input())
res = []

for i in range(n):
    a, b = map(int, input().split())
    lastDigit = str(pow(a, b))[-1]
    res.append(int(lastDigit))

for x in res:
    print(x)
