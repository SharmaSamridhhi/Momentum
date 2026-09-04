import sys

def solver(triangle):
	return triangle

def main():
	data = sys.stdin.read().split()
	indx = 0
	
	rows = int(data[indx]); indx+=1
	
	triangle = []
	for i in range(rows):
		row_len = i+1
		row = list(map(int, data[indx:indx+row_len]))
		indx += row_len
		triangle.append(row)
		
	print(solver(triangle))
	
if __name__ == "__main__":
	main()