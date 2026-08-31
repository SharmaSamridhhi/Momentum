def insert(intervals, newInterval):
    result = []

    for interval in intervals:
        #if left is alright
        if interval[1] < newInterval[0]:
            result.append(interval)

        #if right is alright
        elif interval[0] > newInterval[1]:
            result.append(newInterval)
            newInterval = interval

        #overlapping found
        else:
            newInterval[0] = min(newInterval[0], interval[0])
            newInterval[1] = max(newInterval[1], interval[1])

    result.append(newInterval)
    return result