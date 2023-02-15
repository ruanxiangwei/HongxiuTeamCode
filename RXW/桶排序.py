countn = [0] * 51
nums, result = [1, 1, 3, 19, 35, 49, 50, 5, 10, 16], []
for i in nums:
    countn[i] += 1
for i in range(1, len(countn)):
    if countn[i]:
        result += [i] * countn[i]
print(result)