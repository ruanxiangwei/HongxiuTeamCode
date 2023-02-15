nums = [5, 3, 6, 4, 1, 2, 8, 7]
def QuickSort(num):
    if len(num) <= 1:
        return num
    key = num[0]
    llist, rlist, mlist = [], [], [key]
    for i in range(1, len(num)):
        if num[i] > key:
            rlist.append(num[i])
        elif num[i] < key:
            llist.append(num[i])
        else:
            mlist.append(num[i])
    return QuickSort(llist) + mlist + QuickSort(rlist)
print(QuickSort(nums))