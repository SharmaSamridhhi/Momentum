def moveZeroes(arr):
    non_zero = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[non_zero] = arr[non_zero], arr[i]

            non_zero+=1