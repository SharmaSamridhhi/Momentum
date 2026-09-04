import sys

def solver(n,arr):
	return arr

def main():
	data = sys.stdin.read().split()
	indx = 0
	
	n = int(data[indx]); indx+=1
	arr = []
	
	for i in range(n):
		arr.append(int(data[indx]));indx+=1
		
	print(solver(n,arr))
	
if __name__ == "__main__":
	main()