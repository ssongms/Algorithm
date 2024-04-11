weight = []
value = []

N, K = map(int, input().split())
# K : 버틸 수 있는 무게

dp = [[0 for _ in range(100001)] for _ in range(101)]
# dp[물건 수 N][버틸 수 있는 무게 K]

def knapsack(idx, curWeight):

    if dp[idx][curWeight] > 0:
        return dp[idx][curWeight]
    
    if idx == N: 
        return 0
    
    val1 = 0
    if K >= curWeight + weight[idx]:
        val1 = value[idx] + knapsack(idx+1, curWeight + weight[idx]) # 포함 -> 현재 가치 + 이번 인덱스 아이템의 가치
    
    val2 = knapsack(idx+1, curWeight) # 미포함
    dp[idx][curWeight] = max(val1, val2)
    return dp[idx][curWeight]

for _ in range(N):
    w, v = map(int, input().split())
    weight.append(w)
    value.append(v)

print(knapsack(0, 0))