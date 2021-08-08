def solve(cols, rows, board):
    arr = []
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    def floodFill(row, col, count, previousIsX):
        visited[row][col] = True
        if board[row][col] == 'X':
            if not previousIsX:
                count += 1
            previousIsX = True
        if board[row - 1][col] != '.' and visited[row - 1][col] == False and row - 1 >= 0:
            floodFill(row - 1, col, count, previousIsX)
        if board[row + 1][col] != '.' and visited[row + 1][col] == False and row + 1 < rows:
            floodFill(row + 1, col, count, previousIsX)
        if board[row][col - 1] != '.' and visited[row][col - 1] == False and col - 1 >= 0:
            floodFill(row, col - 1, count, previousIsX)
        if board[row][col + 1] != '.' and visited[row][col + 1] == False and col + 1 < cols:
            floodFill(row, col + 1, count, previousIsX)
        return count

    for row in range(rows):
        for col in range(cols):
            if board[row][col] == '*' and visited[row][col] == False:
                arr.append(floodFill(row, col, 0, False))
            visited[row][col] = True

    return arr


cols, rows = map(int, input().split())
matrix = []
for _ in range(rows):
    matrix.append(list(input()))
_ = map(int, input().split())
print(solve(cols, rows, matrix))
