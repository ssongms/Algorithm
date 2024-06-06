# https://www.acmicpc.net/problem/2630

import sys
N = int(sys.stdin.readline())
colorPaper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
BLUE, WHITE = 1, 0
blueCount, whiteCount = 0, 0

# 시작 x, y를 전달 & 크기(N)를 전달
def devide(x, y, N):
    global blueCount, whiteCount
    x1, y1 = x, y
    x2, y2 = x1+N, y1
    x3, y3 = x1, y1+N
    x4, y4 = x1+N, y1+N

    localBlueCount, localWhiteCount = 0, 0
    for i in range(N): # 1사분면
        for j in range(N):
            if colorPaper[x1+i][y1+j] == BLUE:
                localBlueCount += 1
            else:
                localWhiteCount += 1
    if localBlueCount == 0: # 전부 WHITE => 더이상 나눌 필요 없음
        whiteCount += 1
    elif localWhiteCount == 0:
        blueCount += 1
    else:
        devide(x1, y1, N//2)
    
    localBlueCount, localWhiteCount = 0, 0
    for i in range(N): # 1사분면
        for j in range(N):
            if colorPaper[x2+i][y2+j] == BLUE:
                localBlueCount += 1
            else:
                localWhiteCount += 1
    if localBlueCount == 0: # 전부 WHITE => 더이상 나눌 필요 없음
        whiteCount += 1
    elif localWhiteCount == 0:
        blueCount += 1
    else:
        devide(x2, y2, N//2)

    localBlueCount, localWhiteCount = 0, 0
    for i in range(N): # 1사분면
        for j in range(N):
            if colorPaper[x3+i][y3+j] == BLUE:
                localBlueCount += 1
            else:
                localWhiteCount += 1
    if localBlueCount == 0: # 전부 WHITE => 더이상 나눌 필요 없음
        whiteCount += 1
    elif localWhiteCount == 0:
        blueCount += 1
    else:
        devide(x3, y3, N//2)

    localBlueCount, localWhiteCount = 0, 0
    for i in range(N): # 1사분면
        for j in range(N):
            if colorPaper[x4+i][y4+j] == BLUE:
                localBlueCount += 1
            else:
                localWhiteCount += 1
    if localBlueCount == 0: # 전부 WHITE => 더이상 나눌 필요 없음
        whiteCount += 1
    elif localWhiteCount == 0:
        blueCount += 1
    else:
        devide(x4, y4, N//2)



if 0 not in (n for row in colorPaper for n in row): # 전부 1로 채워짐 -> 파란색 종이 한 장
    print(0)
    print(1)

elif 1 not in (n for row in colorPaper for n in row):
    print(1)
    print(0)

else:
    devide(0, 0, N//2)
    print(whiteCount)
    print(blueCount)