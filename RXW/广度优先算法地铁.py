from queue import Queue
move = []
Q = Queue()
start, end, num = input().split()
move = input().split()
station = [-1 for i in range(0, int(num) + 1)]
Q.put(int(start))
station[int(start)] = 0
while not Q.empty():
    cur = Q.get()
    left = cur - int(move[cur - 1])
    right = cur + int(move[cur - 1])
    if left >= 1 and station[left] == -1:
        Q.put(left)
        station[left] = station[cur] + 1
    if right <= int(num) and station[right] == -1:
        Q.put(right)
        station[right] = station[cur] + 1

print(station[int(end)])