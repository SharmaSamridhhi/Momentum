import sys


def solver(triangle):
	n = len(triangle)
	dp = [[-1] * len(row) for row in triangle]
	
	def inner(r,c):
		if r == n-1:
			return triangle[n-1][c]
			
		if dp[r][c] != -1:
			return dp[r][c]
			
		down = triangle[r][c] + inner(r+1,c)
		diagonal = triangle[r][c] + inner(r+1,c+1)
		
		dp[r][c] = min(down,diagonal)
		return dp[r][c]
		
	return inner(0,0)
	
	
def main():
	data = sys.stdin.read().split()
	indx = 0
	
	rows = int(data[indx]); indx+=1
	
	mat = []
	for i in range(rows):
		row_len = i+1
		row = list(map(int, data[indx:indx+row_len]))
		indx+=row_len
		mat.append(row)
		
	print(solver(mat))
		
if __name__ == "__main__":
	main()