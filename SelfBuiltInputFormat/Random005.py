import sys
def solver(mat):
    row,col = len(mat), len(mat[0])
    dp = [[-1]*(col) for _ in range(row)]

    def inner(r,c):
        if r == 0 and c == 0:
            return mat[r][c]

        if r < 0 or c < 0:
            return float('inf')

        if dp[r][c] != -1:
            return dp[r][c]

        up = mat[r][c] + inner(r-1,c)
        left = mat[r][c] + inner(r,c-1)

        dp[r][c] = min(left, up)
        return dp[r][c]

    return inner(row-1,col-1)
def main():
    data = sys.stdin.read().split()
    indx = 0

    rows = int(data[indx]); indx+=1
    cols = int(data[indx]); indx+=1

    mat = []
    for i in range(rows):
        row = list(map(int, data[indx:indx+cols]))
        indx += cols
        mat.append(row)

    print(solver(mat))

if __name__ == "__main__":
    main()