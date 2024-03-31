#https://www.acmicpc.net/problem/1189

import sys
sys.setrecursionlimit(10**6)

result = 0

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

def dfs(x, y, row, col, board, visited, move):
    global result
    if x == 0 and y == col - 1 : # Arrived
        if move == distance: 
            result += 1
        return
    
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if(0 <= nx < row and 0 <= ny < col and not visited[nx][ny] and board[nx][ny] == '.'):
            dfs(nx, ny, row, col, board, visited, move + 1)
            visited[nx][ny] = False

row, col, distance = map(int, input().split(" "))
visited = [[False for _ in range(col)] for _ in range(row)]
board = [list(input()) for _ in range(row)]
for i in range(row):
    for j in range(col):
        if board[i][j] == 'T':
            visited[i][j] = True
# 장애물이 있는 곳(T)에 접근하지 못하도록 visited 배열을 True로 설정

dfs(row-1, 0, row, col, board, visited, 1)

print(result)
