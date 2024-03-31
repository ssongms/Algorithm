#https://www.acmicpc.net/problem/1012
import sys
sys.setrecursionlimit(10**6)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(x, y, row, col, mat, visited):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < row and 0 <= ny < col and mat[nx][ny] == 1 and not visited[nx][ny]):
            dfs(nx, ny, row, col, mat, visited)
        
case = int(input())
result = []

for _ in range(case):
    col, row, num = map(int, input().split(" "))
    mat = [[0 for _ in range(col)] for _ in range(row)]
    visited = [[False for _ in range(col)] for _ in range(row)]
    worms = 0

    for j in range(num):
        x, y = map(int, input().split(" "))
        mat[y][x] = 1

    for i in range(row):
        for j in range(col):
            if(mat[i][j] == 1 and not visited[i][j]):
               worms += 1
               dfs(i, j, row, col, mat, visited)
               
    result.append(worms)

for worm in result:
    print(worm)