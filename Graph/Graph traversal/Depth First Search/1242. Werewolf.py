# [2, 7]
# [[2], [], [5], [4, 5], [], [1], [], [0]]
# TODO: Search Ancestors and descendants of victim nodes
# 
def dfs(N, graph, start=1):
    dp = [0] * (N + 1)
    visited, finished = [False] * (N + 1), [False] * (N + 1)
    stack = [start]
    while stack:
        start = stack[-1]
        # push unvisited children into stack
        if not visited[start]:
            visited[start] = True
            for child in graph[start]:
                if not visited[child]:
                    # print(f"stack....{stack}")
                    stack.append(child)
        else:
            print(f"stack...{stack}")
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
graph = [[] for _ in range(N + 1)]
victims = []
while True:
    try:
        line = input()
        child, parent = map(int, line.split())
        graph[child].append(parent)
    except:
        while True:
            try:
                victim = int(input())
                victims.append(victim)
            except:
                break
        break
print(graph)
print(solve(N, graph, victims))
