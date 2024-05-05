# DFS 구현 -> 시간 초과

# import sys
# sys.setrecursionlimit(10**6)

# row, col = map(int, input().split())
# campus = [list(input()) for _ in range(row)]
# visited = [[False for _ in range(col)] for _ in range(row)]

# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]
# result = 0
# def dfs(curX, curY):
#     global result
#     visited[curX][curY] = True
#     if campus[curX][curY] == 'P':
#         result += 1
#     for i in range(4):
#         nx = curX + dx[i]
#         ny = curY + dy[i]
#         if(0<=nx<row and 0<=ny<col and not visited[nx][ny] and (campus[nx][ny]=='O' or campus[nx][ny]=='P')):
#             dfs(nx, ny)

# startX = 0
# startY = 0
# found = False
# for i in range(row):
#     if found:
#         break
#     for j in range(col):
#         if campus[i][j] == 'I':
#             startX = i
#             startY = j
#             found = True
#             break

# dfs(startX, startY)

# if result == 0:
#     print("TT")
# else:
#     print(result)


# BFS 구현 -> 시간 초과 해결
from collections import deque # BFS 구현을 위해 큐 모듈

row, col = map(int, input().split())
campus = [list(input()) for _ in range(row)]

dx = [0, 1, 0, -1] # 동,서,남,북 이동을 위한 dx, dy 선언
dy = [1, 0, -1, 0]

def bfs(startX, startY): # bfs 함수 구현
    visited = [[False for _ in range(col)] for _ in range(row)]
    queue = deque([(startX, startY)]) # dequeue 한 번 하고 시작
    visited[startX][startY] = True
    result = 0
    while queue: # 큐가 빌 때까지 루프
        x, y = queue.popleft() # dequeue
        if campus[x][y] == 'P': # 현재 방문한 곳이 P라면 result++
            result += 1
        for i in range(4): # 동서남북 4방향으로 반복
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < row and 0 <= ny < col and not visited[nx][ny] and (campus[nx][ny] == 'O' or campus[nx][ny] == 'P'):
                queue.append((nx, ny))
                visited[nx][ny] = True
    return result

def findStart():
    for i in range(row):
        for j in range(col):
            if campus[i][j] == 'I':
                return i, j # 바로 리턴함으로써 시간 단축

startX, startY = findStart()
result = bfs(startX, startY) # 현재 'I' 위치에서 BFS 시작

if result == 0:
    print("TT")
else:
    print(result)