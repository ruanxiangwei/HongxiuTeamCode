def MergeSort(num):
    if len(num) <= 1:
        return num
    mid = int(len(num)/2)
    llist, rlist = MergeSort(num[:mid]), MergeSort(num[mid:])
    result = []
    i, j = 0, 0
    while i < len(llist) and j < len(rlist):
        if rlist[j] < llist[i]:
            result.append(rlist[j])
            j += 1
        else:
            result.append(llist[i])
            i += 1
        result += llist[i:] + rlist[j:]
        return result

nums = [5, 3, 6, 4, 1, 2, 8, 7]
print(MergeSort(nums))