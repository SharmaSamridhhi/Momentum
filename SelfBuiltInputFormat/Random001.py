import sys
 
def solver(n, arr):
    prefix_sum, max_len = 0, float('-inf')
    prefix_map = {}
    
    for i in range(len(arr)):
        prefix_sum += arr[i]
        
        if prefix_sum == n:
            max_len = max(max_len, i+1)
            
        rem = prefix_sum - n
        
        if rem in prefix_map:
            length = i-prefix_map[rem]
            max_len = max(max_len, length)
            
        if prefix_sum and prefix_sum not in prefix_map:
            prefix_map[prefix_sum] = i
            
        return max_len
    
 
def main():
    data = sys.stdin.read().split()
    indx = 0
    
    n = int(data[indx]); indx+=1
    a = int(data[indx]); indx+=1
    b = int(data[indx]); indx+=1
    c = int(data[indx]); indx+=1
    
    arr = [a,b,c]
    print(solver(n, arr))
    
if __name__ == '__main__':
    main()