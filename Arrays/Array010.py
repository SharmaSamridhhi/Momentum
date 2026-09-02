def twoSum(nums, target):
    hashmap = {}

    for i, num in enumerate(nums):
        rem = target-num

        if num in hashmap:
            return [hashmap[num], i]

        hashmap[rem] = i

    return []