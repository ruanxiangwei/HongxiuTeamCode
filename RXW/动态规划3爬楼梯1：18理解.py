def goUpStairs(n):#第n级楼梯
    if n < 1:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    a = 1
    b = 2
    sum = 0
    for i in range(2, n):
        sum = a + b
        a = b
        b = sum
    return sum
print(goUpStairs(10))