def missingNumber(nums):
    n = len(nums) + 1
    summation = (n*(n-1))//2


    missing_number = summation - sum(nums)

    return missing_number