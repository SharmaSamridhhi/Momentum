def minPlatform(self, arr: list[int], dep: list[int]) -> int:
    dep.sort()
    arr.sort()
        
    platform_needed, max_platform = 0,0
    i,j = 0,0
        
    while i < len(arr):
        if arr[i] <= dep[j]:
            platform_needed += 1
            max_platform = max(max_platform,platform_needed)
            i+=1
        else:
            platform_needed -= 1
            j+=1
                
    return max_platform