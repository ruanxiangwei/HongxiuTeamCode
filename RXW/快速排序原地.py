nums = [5, 3, 6, 4, 1, 2, 8, 7]
def QSort(left, right):
    if left >= right:
        return
    l, r, key = left, right, nums[left]
    while l < r:
        while l < r and nums[r] >= key:
            r -= l
        nums[l] = nums[r]
        while l < r and nums[l] < key:
            l += 1
            nums[r] = nums[l]
        nums[l] = key
        QSort(left, l-1)
        QSort(l+1, right)
QSort(0, len(nums)-1)
print(nums)