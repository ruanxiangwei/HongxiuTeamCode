nums = [5, 3, 6, 4, 1, 2, 8, 7]
res = []
while len(nums):
    minInd = 0
    for i in range(1, len(nums)):
        if nums[i] < nums[minInd]:
            minInd = i
    temp = nums[minInd]
    nums.pop(minInd)
    res.append(temp)
print(res)