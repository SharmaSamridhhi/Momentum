def check(nums):
    n = len(nums)
    count = 0

    for i in range(1, n):
        if nums[i-1] > nums[i]:
                count += 1

    if nums[0] < nums[-1]:
        count += 1

    return True if count <= 1 else False