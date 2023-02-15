nums = [5, 3, 6, 4, 1, 2, 8, 7]
def ShellSort(nums):
    step = len(nums) // 2
    while step > 0:
        for i in range(step, len(nums)):
            ind = i
            while ind >= step and nums[ind] < nums[ind-step]:
                nums[ind], nums[ind-step] = nums[ind-step], nums[ind]
                ind -= step
        step //= 2
    print(nums)
ShellSort(nums)
