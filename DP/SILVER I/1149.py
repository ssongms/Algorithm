# https://www.acmicpc.net/problem/1149

import sys
R = 0
G = 1
B = 2
house = int(sys.stdin.readline())
board = [list(map(int, input().split())) for _ in range(house)]
dp = [[0] * 3 for _ in range(house)]
sum = 0


for i in range(house):
    if i == 0: # 처음
        for j in range(3):
            dp[0][j] = board[0][j]
    else:
        dp[i][R] = min(board[i][R] + dp[i-1][G], board[i][R] + dp[i-1][B]) 
        dp[i][G] = min(board[i][G] + dp[i-1][R], board[i][G] + dp[i-1][B])
        dp[i][B] = min(board[i][B] + dp[i-1][R], board[i][B] + dp[i-1][G])

result = min(dp[house-1][R], dp[house-1][G], dp[house-1][B])
print(result)