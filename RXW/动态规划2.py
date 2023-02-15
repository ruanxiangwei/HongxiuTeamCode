def goldMine(n, m, g, L):
    results = [0 for _ in range(m+1)]
    t_results = [0 for _ in range(m+1)]
    for i in range(1, m+1):
        if i < L[0]:#如果小于0，就什么砖石都得不到
            t_results[i] = 0
        else:
            t_results[i] = g[0]

    for i in range(1, n):
        results = [0 for _ in range(m+1)]
        for j in range(1, m+1):
            if j < L[i]:
                results[j] = t_results[j]
            else:
                results[j] = max(t_results[j], t_results[j-L[i]] + g[i])
        t_results = results
    return results[-1]
print(goldMine(5, 10, [400,500,200,300,350], [5,5,3,4,3]))