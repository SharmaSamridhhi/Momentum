def jobSequencing(self, deadline, profit):
    n = len(deadline)
        
    jobs = []
    for i in range(n):
        jobs.append((profit[i], deadline[i]))
            
    jobs.sort(key = lambda x: x[0], reverse = True)
        
    slots = [-1] * (n+1)
    count, totalProfit = 0,0
        
    for p,d in jobs:
            
        for slot in range(d,0,-1):
            if slots[slot] == -1:
                slots[slot] = p
                    
                count += 1
                totalProfit += p
                break
                
    return [count, totalProfit]