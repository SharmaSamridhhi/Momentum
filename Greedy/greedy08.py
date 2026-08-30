def eraseOverlapIntervals(intervals):
    intervals.sort(key=lambda x:x[1])
    count, last_end = 0, float('-inf')

    for st,et in intervals:
        if st >= last_end:
            count+=1
            last_end = et

    return len(intervals) - count