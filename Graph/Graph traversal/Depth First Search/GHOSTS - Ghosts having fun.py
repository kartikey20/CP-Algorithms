# WA, idk why
def solve(graph, n):
    visited = [False for _ in range(n)]
    res = []

    def dfs(node):
        visited[node] = True
        for child in graph[node].copy():
            if not visited[child]:
                dfs(child)
            else:
                res.append([node, child])
                graph[node].discard(child)
    dfs(0)
    return res


amount_of_rooms = int(input())
teleports = int(input())
graph = [set() for _ in range(amount_of_rooms)]
for _ in range(teleports):
    u, v = map(int, input().split())
    graph[u-1].add(v-1)

for i in solve(graph, amount_of_rooms):
    print(i[0]+1, i[1]+1)
print(0, 0)
