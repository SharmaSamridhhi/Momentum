import sys

def solver(matrix):
    n = len(matrix)
    dp = [[-1] * 4 for _ in range(n)]
    
    def inner(indx, last):
        if indx == 0:
            maxi = 0
            for i in range(3):
                if i != last:
                    maxi = max(maxi, matrix[0][i])
            return maxi
        
        if dp[indx][last] != -1:
        	return dp[indx][last]
        maxi = 0
        for i in range(3):
            if i != last:
                points = matrix[indx][i] + inner(indx - 1, i)
                maxi = max(maxi, points)
                
        dp[indx][last] = maxi
        return dp[indx][last]
    
    return inner(n - 1, 3)


def main():
    data = sys.stdin.read().split()
    indx = 0
    
    rows = int(data[indx]); indx += 1
    cols = int(data[indx]); indx += 1
    
    matrix = []
    for i in range(rows):
        row = list(map(int, data[indx:indx + cols]))
        indx += cols
        matrix.append(row)
    
    print(solver(matrix))


if __name__ == "__main__":
    main()