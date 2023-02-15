def NQueens(n):
    def checkBoard(rowIndex):
        for i in range(rowIndex):
            if cols[i] == cols[rowIndex]:
                return False
            if abs(cols[i] - cols[rowIndex]) == rowIndex - i:
                return False
        return True

    def helper(rowIndex):
        if rowIndex == n:
            board = [[0 for _ in range(n)] for _ in range(n)]
            for i in range(n):
                board[i][cols[i]] = 1
            res.append(board)
            return
        for i in range(n):
            cols[rowIndex] = i
            if checkBoard(rowIndex):
                helper(rowIndex+1)
    cols = [0 for _ in range(n)]
    res = []
    helper(0)
    return res

n = 4
print(NQueens(n))