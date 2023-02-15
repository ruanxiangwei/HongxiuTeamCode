print("输入q停止运行")
while True:
    a = input("请输入被除数")
    if a == 'q':
        break
    b = input('请输入除数')
    if b == 'q':
        break
    try:
        answer = int(a) / int(b)
    except ZeroDivisionError:
        print('除数不能为0')
    else:
        print(answer)
