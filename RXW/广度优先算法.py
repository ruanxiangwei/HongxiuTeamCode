from queue import Queue
Q = Queue()
class grid:

    def __init__(self, row, col):
        self.row = row
        self.col = col

    def bfs(self, val, startrow, startcol):
        row = len(val)
        col = len(val[0])
        arrived = [[False for j in range(int(col))] for i in range(int(row))]
        moverow = [0, 1, 0, -1]
        movecol = [1, 0, -1, 0]
        ans = 1
        Q.put(grid(int(startrow), int(startcol)))
        arrived[int(startrow) - 1][int(startcol) - 1] = True
        while not Q.empty():
            cur = Q.get()
            for i in range(4):
                newrow = cur.row + moverow[i]
                newcol = cur.col + movecol[i]
                if newrow > row or newrow <= 0 or newcol > col or newcol <= 0:
                    continue
                if not arrived[newrow - 1][newcol - 1] and val[newrow - 1][newcol - 1] != val[cur.row - 1][cur.col - 1]:
                    Q.put(grid(newrow, newcol))
                    arrived[newrow - 1][newcol - 1] = True
                    ans += 1
        return ans