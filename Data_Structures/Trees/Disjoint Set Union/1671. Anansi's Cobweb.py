from collections import defaultdict
N, M = map(int, input().split())
graph = defaultdict(int)
components = [N]
for i in range(1, N+1):
    graph[i] = i


def find(v):
    if v == graph[v]:
        return v
    return find(graph[v])


def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        components[0] -= 1
        graph[b] = a


for _ in range(M):
    u, v = map(int, input().split())
    union(u, v)

Q = int(input())
threads = list(map(int, input().split()))
print(components)
