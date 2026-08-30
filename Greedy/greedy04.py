def canJump(nums):
    maxIndx = 0

    for i in range(len(nums)):
        if i > maxIndx:
            return False

        maxIndx = max(maxIndx, i+nums[i])

    return True