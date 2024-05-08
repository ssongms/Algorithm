# Not using DP
N = int(input())
knapsack = [-1] * 5001
knapsack[3] = 1
knapsack[5] = 1
for i in range(6, N+1):
    if knapsack[i-5] != -1:
        knapsack[i] = knapsack[i-5] + 1
    elif knapsack[i-3] != -1:
        knapsack[i] = knapsack[i-3] + 1

print(knapsack[N])