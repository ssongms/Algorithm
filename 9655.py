"""
상근이가 먼저 게임 시작, 돌은 1개 또는 3개 가져갈 수 있음

N=1) 상근1 -> 상근 win
N=2) 상근1 -> 창영1 -> 창영 win
N=3) 상근3 -> 상근 win
N=4) 상근3 -> 창영1 -> 창영 win
N=5) 상근3 -> 창영1 -> 상근1 -> 상근 win
N=6) 상근3 -> 창영3 -> 창영 win
...

"""

# 1) Not using DP
# N = int(input())
# if N % 2 == 1: # N이 홀수면 상근 승
#     print("SK")
# else: # N이 짝수면 창영 승
#     print("CY")


# 2) Using DP
N = int(input())
dp = [0] * 1001
# 1 : 상근 win
# 2 : 창영 win
dp[1] = 1
dp[2] = 2
for i in range(3, N+1):
    if dp[i-1] == 2 or dp[i-3] == 2: # 현재 돌 개수보다 1개 적을 때 혹은 3개 적을 때 창영이 이겼다면 현재 돌의 개수에선 상근이 승리
        dp[i] = 1
    elif dp[i-1] == 1 or dp[i-3] == 1: 
        dp[i] = 2

if dp[N] == 1:
    print("SK")
elif dp[N] == 2:
    print("CY")
