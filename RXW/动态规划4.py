def backpack_record(n, c, w, v):
    backpack_rec = [[0 for i in range(c + 1) for j in range(len(n) + 1)]]
    for i in range(1, len(n) + 1):
        for j in range(1, c + 1):
            if j < w[i - 1]:
                backpack_rec[i][j] = backpack_rec[i - 1][j]
            else:
                backpack_rec[i][j] = max(backpack_rec[i - 1][j], backpack_rec[i - 1][j - w[i - 1]] + v[i - 1])
        return backpack_rec

def backpack_results(n, c, w, res):
    print('可容纳最大价值为：', res[len(n)][c])
    x = [False for i in range(len(n) + 1)]
    j = c
    i = len(n)
    while i >= 0:
        if res[i][j] > res[i - 1][j]:
            x[i] = True
            j -= w[i - 1]
        i -= 1
    print('选择的物品为:')
    for i in range(len(n)+1):
        if x[i]:
            print('第',i,'个,',end = '')
        print('')

n = ['a', 'b', 'c', 'd']
c = 8
w = [2, 4, 5, 3]
v = [5, 4, 6, 2]
res = backpack_record(n, c, w, v)
backpack_results(n, c, w, res)