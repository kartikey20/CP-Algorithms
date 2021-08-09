# [
# ['.######.'],
# ['#..k...#'],
# ['#.####.#'],
# ['#.#v.#.#'],
# ['#.#.k#k#'],
# ['#k.##..#'],
# ['#.v..v.#'],
# ['.######.']
# ]
def valid(x, y, N, M):
    if x >= 0 and x < N and y >= 0 and y < M:
        return True
    return False


def dfs(x, y, visited, matrix, k, v):
    visited[x][y] = True
    if matrix[x][y] == 'k':
        k += 1
    if matrix[x][y] == 'v':
        v += 1
    if valid(x + 1, y, N, M) and visited[x + 1][y] == False and matrix[x + 1][y] != '#':
        return dfs(x + 1, y, visited, matrix, k, v)
    if valid(x - 1, y, N, M) and visited[x - 1][y] == False and matrix[x - 1][y] != '#':
        return dfs(x - 1, y, visited, matrix, k, v)
    if valid(x, y + 1, N, M) and visited[x][y + 1] == False and matrix[x][y + 1] != '#':
        return dfs(x, y + 1, visited, matrix, k, v)
    if valid(x, y - 1, N, M) and visited[x][y - 1] == False and matrix[x][y - 1] != '#':
        return dfs(x, y - 1, visited, matrix, k, v)
    return k, v, visited


def solve(N, M, matrix, sheep, wolves):
    visited = [[False for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 'k' and visited[i][j] == False:
                k, v = 0, 0
                k, v, visited = dfs(i, j, visited, matrix, k, v)
                if k > v:
                    wolves -= v
                else:
                    sheep -= k
    return wolves, sheep


N, M = map(int, input().split())
matrix = []
wolves, sheep = 0, 0
for _ in range(N):
    temp = input()
    for i in temp:
        if i == 'k':
            sheep += 1
        if i == 'v':
            wolves += 1
    matrix.append(temp)
print(solve(N, M, matrix, sheep, wolves))
# print(sheep, wolves)
