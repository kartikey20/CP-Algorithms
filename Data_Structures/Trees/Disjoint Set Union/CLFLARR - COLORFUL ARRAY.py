from collections import defaultdict

n, q = list(map(int, input().split()))
graph = defaultdict(list)

for i in range(1, n+1):
    graph[i] = [i, 0]


def find(v):
    if v == graph[v][0]:
        return v
    return find(graph[v][0])


def union(a, b, c):
    a = find(a)
    b = find(b)
    if b != a:
        graph[b] = [a, c]


for _ in range(q):
    l, r, c = map(int, input().split())
    union(l, r, c)


print(graph)
