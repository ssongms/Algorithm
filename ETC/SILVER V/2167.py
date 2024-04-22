N, M = map(int, input().split())
board = []

for i in range(N):
    row = list(map(int, input().split()))
    board.append(row)

M = int(input())
result = []

def calcSum(startR, startC, endR, endC):
    global board
    num = 0
    for i in range(startR, endR+1):
        for j in range(startC, endC+1):
            num += board[i][j]
    return num


for _ in range(M):
    i, j, x, y = map(int, input().split())
    result.append(calcSum(i-1, j-1, x-1, y-1))

for i in range(len(result)):
    print(result[i])