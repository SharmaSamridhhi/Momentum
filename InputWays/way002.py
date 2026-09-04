import sys

def solver(matrix):
	return matrix

def main():
	data = sys.stdin.read().split()
	indx = 0
	
	rows = int(data[indx]); indx+=1
	cols = int(data[indx]); indx+=1
	
	matrix = []
	
	for i in range(rows):
		row = list(map(int, data[indx:indx+cols]))
		indx+=cols
		matrix.append(row)
	
	print(solver(matrix))
	

if __name__ == "__main__":
	main()