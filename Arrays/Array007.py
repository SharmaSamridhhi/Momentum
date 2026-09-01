def findMaxConsecutiveOnes(arr):
    currCount, maxCount = 0,float('-inf')

    l,r = 0,0

    while r < len(arr):
        if arr[r] == 1:
            currCount = r-l+1
            maxCount = max(maxCount, currCount)

        else:
            currCount = 0
            l = r+1
        r+=1

        maxCount = max(maxCount, currCount)

    return maxCount