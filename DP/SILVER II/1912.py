n = int(input())
arr = list(map(int, input().split()))

dp = [0] * n
dp[0] = arr[0]
for i in range(1, n):
    dp[i] = max(arr[i], dp[i-1] + arr[i]) # 현재 인덱스 i에서 자기 자신(arr[i])과 이전의 누적 합에 자기 자신을 더했을 때(dp[i-1]+arr[i]) 중 더 큰 값을 기록

print(max(dp))