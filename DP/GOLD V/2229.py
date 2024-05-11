import sys
N = int(sys.stdin.readline())
score = list(map(int, sys.stdin.readline().split()))
dp = [0] * 1001

for i in range(1, N+1):
    for j in range(i, 0, -1):
        maxN = max(score[i-1], score[j-1])
        minN = min(score[i-1], score[j-1])
        dp[i] = max(dp[i], dp[j-1] + maxN - minN)

print(dp[N])