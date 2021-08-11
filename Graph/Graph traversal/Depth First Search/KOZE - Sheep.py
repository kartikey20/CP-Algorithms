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


k, v = [-1], [-1]


def dfs(x, y, visited, matrix):
    visited[x][y] = True
    if matrix[x][y] == 'k':
        k[0] += 1
    if matrix[x][y] == 'v':
        v[0] += 1
    if valid(x + 1, y, N, M) and visited[x + 1][y] == False and matrix[x + 1][y] != '#':
        dfs(x + 1, y, visited, matrix)
    if valid(x - 1, y, N, M) and visited[x - 1][y] == False and matrix[x - 1][y] != '#':
        dfs(x - 1, y, visited, matrix)
    if valid(x, y + 1, N, M) and visited[x][y + 1] == False and matrix[x][y + 1] != '#':
        dfs(x, y + 1, visited, matrix)
    if valid(x, y - 1, N, M) and visited[x][y - 1] == False and matrix[x][y - 1] != '#':
        dfs(x, y - 1, visited, matrix)


def solve(N, M, matrix, sheep, wolves):
    visited = [[False for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 'k' and visited[i][j] == False:
                k[0] = 0
                v[0] = 0
                dfs(i, j, visited, matrix)
                if k[0] > v[0]:
                    wolves -= v[0]
                else:
                    sheep -= k[0]
    return " ".join(map(str, (sheep, wolves)))


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
