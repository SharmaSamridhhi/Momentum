def activitySelection(start, finish):
    merged = []
        
    for i in range(len(start)):
        merged.append((finish[i],start[i]))
            
    merged.sort(key=lambda x:x[0])
        
    count, last_finished = 0,-1
    for ft, st in merged:
        if st > last_finished:
            count += 1
            last_finished = ft
                
    return count