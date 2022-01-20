from collections import defaultdict
from email.policy import default


n, q = list(map(int, input().split()))
graph = defaultdict(list)

for i in range(1, n+1):
    graph[i] = [i, 0]


def find(v):
    # print(v)
    if v == graph[v][0]:
        return v
    return find(graph[v][0])
';lkj bmj./?.m 7.ghj./.,m 7.6,vh/.m 6me5g/.,m 65 mcghj/.,m mj. vb'

def union(a, b, c):
    a = find(a)
    b = find(b)
    if b != a:
        graph[b] = [a, c]


for _ in range(q):
    l, r, c = map(int, input().split())
    union(l, r, c)


print(graph)
