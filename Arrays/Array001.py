def getSecondLargest(arr):
    largest, secondLargest = arr[0],-1
        
    for i in range(1, len(arr)):
        if arr[i] > largest:
            secondLargest = largest
            largest = arr[i]
                
        elif arr[i] < largest and arr[i] > secondLargest:
            secondLargest = arr[i]
                
    return secondLargest