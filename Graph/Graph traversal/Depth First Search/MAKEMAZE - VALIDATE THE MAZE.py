def validate(matrix, m, n):
    visited = [[False for _ in range(n)] for _ in range(m)]
    points = []
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == '.':
                if j == 0 or j == n - 1:
                    points.append([i, j])
                if i == 0 or i == m - 1:
                    points.append([i, j])

    points = list(set(map(tuple, points)))

    if len(points) == 2:
        def valid(x, y):
            if x >= 0 and x < m and y >= 0 and y < n:
                return True
            return False

        def dfs(x, y):
            visited[x][y] = True
            if valid(x + 1, y) and visited[x + 1][y] == False and matrix[x + 1][y] != '#':
                dfs(x + 1, y)
            if valid(x - 1, y) and visited[x - 1][y] == False and matrix[x - 1][y] != '#':
                dfs(x - 1, y)
            if valid(x, y - 1) and visited[x][y - 1] == False and matrix[x][y - 1] != '#':
                dfs(x, y - 1)
            if valid(x, y + 1) and visited[x][y + 1] == False and matrix[x][y + 1] != "#":
                dfs(x, y + 1)

        dfs(points[0][0], points[0][1])

        if any(visited[i[0]][i[1]] for i in points[1:]):
            return "valid"

        return "invalid"
    else:
        return "invalid"


T = int(input())
res = []
for _ in range(T):
    m, n = map(int, input().split())
    matrix = [input() for i in range(m)]
    res.append(validate(matrix, m, n))

for x in res:
    print(x)
