import copy
def sudoku(board):
    def checkBoard(i, j, num):
        for t in range(9):
            if t != j and board[i][t] == num:
                return False
            if t != i and board[t][j] == num:
                return False
        for t in range(i - i % 3, 3 + i - i % 3):
            for s in range(j - j % 3, 3 + j - j % 3):
                if t != i and s != j and board[t][s] == num:
                    return False
        return True

    def helper(index):
        if index == 81:
            solution = copy.deepcopy(board)
            res.append(solution)
            return
        i = index // 9
        j = index % 9
        if board[i][j] == 0:
            for num in range(1, 10):
                board[i][j] = num
                if checkBoard(i, j, num):
                    helper(index + 1)
                board[i][j] = 0
            else:
                helper(index + 1)

    res = []
    helper(0)
    return res
