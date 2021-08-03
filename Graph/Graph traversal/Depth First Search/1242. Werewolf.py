# [2, 7]
# [[2], [], [5], [4, 5], [], [1], [], [0]]
def dfs(N, graph, start=0):
    dp = [0] * N
    visited, finished = [False] * N, [False] * N
    stack = [start]
    while stack:
        start = stack[-1]
        # push unvisited children into stack
        if not visited[start]:
            visited[start] = True
            for child in graph[start]:
                if not visited[child]:
                    stack.append(child)
        else:
            stack.pop()
            # base case
            dp[start] += 1
            # update finished children
            for child in graph[start]:
                if finished[child]:
                    dp[start] += dp[child]

            finished[start] = True
    return dp


def solve(N, graph, victims):
    return dfs(N, graph)


N = int(input())
graph = [[] for _ in range(N)]
victims = []
while True:
    try:
        line = input()
        child, parent = map(int, line.split())
        graph[parent - 1].append(child - 1)
    except:
        while True:
            try:
                victim = int(input())
                victims.append(victim - 1)
            except:
                break
        break
print(graph)
# print(solve(N, graph, victims))
