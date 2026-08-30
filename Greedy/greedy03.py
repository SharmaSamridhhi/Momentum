def solve(bt):
    bt.sort()
    total, endTime,n = 0,0,len(bt)
        
    for i in range(n-1):
        endTime += bt[i]
        total += endTime
            
    return total//n