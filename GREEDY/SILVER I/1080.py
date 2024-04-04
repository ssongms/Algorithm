import sys

N, M = list(map(int, sys.stdin.readline().split()))
beforeBoard = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
afterBoard = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
count = 0
found = False

def reverse(before, row, col):
    if row+2 < N and col+2 < M:
        for r in range(3):
            for c in range(3):
                if before[row+r][col+c] == 1:
                    before[row+r][col+c] = 0
                else:
                    before[row+r][col+c] = 1

if beforeBoard == afterBoard:
    found = True
else:
    for row in range(N):
        if found:
            break
        for col in range(M):
            if beforeBoard[row][col] != afterBoard[row][col]:
                reverse(beforeBoard, row, col)
                count += 1
                if(beforeBoard == afterBoard):
                    found = True
                    break
    
if not found:
    print(-1)
else:
    print(count)