from collections import Counter

def majorityElement(self, nums):
    freq = Counter(nums)

    for num, occurence in freq.items():
        if occurence > len(nums)//2:
            return num

    return -1