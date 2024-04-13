size = int(input())
location = int(input())

board = [[0 for _ in range(size)]for _ in range(size)] # N by N 2차원 배열 생성
count = pow(size,2) # count는 size^2으로 시작
curX = 0
curY = 0
result = ""

while True:
    if count == 1:
        board[curX][curY] = count # 중간에 1 
        if location == 1:
                result = str(curX+1) + " " + str(curY+1)
        break
    else:
        # to bottom
        while curX < size and board[curX][curY] == 0:
            board[curX][curY] = count
            if count == location:
                result = str(curX+1) + " " + str(curY+1)
            curX+=1
            count-=1
        curX -= 1
        curY += 1
        # to right
        while curY < size and board[curX][curY] == 0:
            board[curX][curY] = count
            if count == location:
                result = str(curX+1) + " " + str(curY+1)
            curY+=1
            count-=1
        curX -= 1
        curY -= 1
        # to up
        while curX >= 0 and board[curX][curY] == 0:
            board[curX][curY] = count
            if count == location:
                result = str(curX+1) + " " + str(curY+1)
            curX-=1
            count-=1
        curX += 1
        curY -= 1
        # to left
        while curY >= 0 and board[curX][curY] == 0:
            board[curX][curY] = count
            if count == location:
                result = str(curX+1) + " " + str(curY+1)
            curY-=1
            count-=1
        curY += 1
        curX += 1
    
for i in range(size):
    for j in range(size):
        print(board[i][j], end=" ")
    print()
print(result)