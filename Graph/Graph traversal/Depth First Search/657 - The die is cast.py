def solve(col, row, board):
    visited = [[False for _ in range(col)] for _ in range(row)]
    visited[0][0] = True

    def dfs(endCol, endRow, board, col, row, previousIsX, count, arr):
        if col == endCol and endRow == row:
            return count
        else:
            for i in range(row - 1, row + 2):
                for j in range(col - 1, col + 2):
                    if visited[i][j] == False and i >= 0 and j >= 0 and i < endRow and j < endCol:
                        visited[i][j] = True
                        if board[i][j] == 'X':
                            if not previousIsX:
                                count += 1
                            previousIsX = True
                        else:
                            previousIsX = False
                        dfs(endCol, endRow, board, i,
                            j, previousIsX, count, arr)
    return dfs(col, row, board, 0, 0, False, 0, [])


col, row = map(int, input().split())
matrix = []
for i in range(row):
    matrix.append(list(input()))
_ = map(int, input().split())
print(solve(col, row, matrix))
