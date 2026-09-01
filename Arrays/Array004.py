def reverse(arr, start, end):
    while start < end:
        arr[start] , arr[end] = arr[end] , arr[start]
        start += 1
        end -= 1
def rotate(arr, k):
    n = len(arr)
    k %= n
    reverse(arr, 0, n-k-1)
    reverse(arr, n-k, n-1)
    reverse(arr, 0, n-1)
    return arr