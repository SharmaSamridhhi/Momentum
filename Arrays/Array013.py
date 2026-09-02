def rearrangeArray(nums):
    newNums = [0] * len(nums)

    pos, neg = 0, 1

    for i in range(len(nums)):
        if nums[i] < 0:
            newNums[neg] = nums[i]
            neg += 2

        else:
            newNums[pos] = nums[i]
            pos += 2

    return newNums