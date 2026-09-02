def longestSubarray(self, arr, k):  
    prefix_sum, max_len = 0,0
    prefix_map = {}
        
    for i in range(len(arr)):
        prefix_sum+=arr[i]
            
        #if prefix_sum == k(target)
        if prefix_sum == k:
                max_len = max(max_len, i+1)
                
                
        #calculate remaining(rem)
        rem = prefix_sum - k
            
        #is remaining(rem) in map
        if rem in prefix_map:
            length = i - prefix_map[rem]
            max_len = max(max_len, length)
                
        #is prefix_sum in map if not add it with value as index i
        if prefix_sum and prefix_sum not in prefix_map:
            prefix_map[prefix_sum] = i
                
    return max_len