def candy(ratings):
    n = len(ratings)
    left = [0] * (n)
    right = [0] * (n)

    left[0],right[n-1] = 1,1

    for i in range(1, n):
        if ratings[i] > ratings[i-1]:
            left[i] = left[i-1] + 1
        else:
            left[i] = 1

    for i in range(n-2,-1,-1):
        if ratings[i] > ratings[i+1]:
            right[i] = right[i+1]+1
        else:
            right[i] = 1

    count = 0

    for i in range(n):
        count += max(left[i],right[i])

    return count