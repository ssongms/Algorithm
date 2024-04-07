import sys
sys.setrecursionlimit(10000)
N, r, c = list(map(int, sys.stdin.readline().split(" ")))
count = 0

def calcVisit(row, col, n):
    global count
    if n == 2:
        for i in range(2):
            for j in range(2):
                if row+i == r and col+j == c:
                    print(count)    
                    exit()
                count+=1
                
    else:
        if r < row + n//2 and c < col + n//2:
            calcVisit(row, col, n//2)

        elif r < row + n//2 and c >= col + n//2:
            count += 1 * ((n//2) ** 2)
            calcVisit(row, col+n//2, n//2)

        elif r >= row + n//2 and c < col + n//2:
            count += 2 * ((n//2) ** 2)
            calcVisit(row+n//2, col, n//2)

        else:
            count += 3 * ((n//2) ** 2)
            calcVisit(row+n//2, col+n//2, n//2)

calcVisit(0, 0, 2**N) # matrix, 8, 8 