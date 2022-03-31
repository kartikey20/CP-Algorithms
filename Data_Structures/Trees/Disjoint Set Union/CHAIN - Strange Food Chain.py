from collections import defaultdict

T = int(input())
n, k = map(int, input().split())
count = 0
graph = defaultdict(int)

for i in range(1, n+1):
    graph[i] = i


def find(v):
    if v == graph[v]:
        return v
    return find(graph[v])


def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        graph[b] = a


for _ in range(k):
    p, x, y = map(int, input().split())

    if x > n or y > n:
        count += 1
    if p == 2:
        union(x, y)
    if p == 1:
        if x != y and graph[x] == graph[y]:
            print("...", x, y)
            count += 1
print(count)
