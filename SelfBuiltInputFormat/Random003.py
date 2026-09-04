import sys

def solver(row,col):
	dp = [[-1]*(col) for _ in range(row)]
	def inner(r,c):
		if r==0 and c==0:
			return 1
		if r < 0 or c < 0:
			return 0
			
		if dp[r][c] != -1:
			return dp[r][c]
			
		left = inner(r-1,c)
		up = inner(r,c-1)
		
		dp[r][c] = left+up
		
		return dp[r][c]
	return inner(row-1,col-1)
	
	
def main():
	data = sys.stdin.read().split()
	indx = 0
	
	row = int(data[indx]); indx+=1
	col = int(data[indx]); indx+=1
	
	print(solver(row,col))
	
	
if __name__ == "__main__":
	main()