def sortColors(nums):
    n = len(nums)
    low, mid, high = 0,0, n-1

    while mid <= high:
        if nums[mid] == 0:
            nums[mid],nums[low] = nums[low],nums[mid]
            mid+=1
            low+=1

        elif nums[mid] == 1:
            mid+=1

        else:
            nums[mid],nums[high] = nums[high],nums[mid]
            high-=1