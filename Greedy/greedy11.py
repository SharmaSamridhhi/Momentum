def merge(intervals):
    intervals.sort()

    result = []
    newInterval = intervals[0]

    for interval in intervals[1:]:
        if interval[0] > newInterval[1]:
            result.append(newInterval)
            newInterval = interval
        else:
            newInterval[1] = max(newInterval[1], interval[1])

    result.append(newInterval)
    return result