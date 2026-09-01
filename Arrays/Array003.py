def removeDuplicates(nums):
    last_unique = 0

    for i in range(1, len(nums)):
        if nums[last_unique] != nums[i]:
            nums[last_unique+1] = nums[i]
            last_unique += 1
            
    return last_unique+1