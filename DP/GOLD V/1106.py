customers, city = map(int, input().split())
inputArr = [list(map(int, input().split()))for _ in range(city)]
result = int(1e9)
dp = [int(1e9)] * (customers+100)
dp[0] = 0

for cost, customer in inputArr:
    for i in range(customer, len(dp)):
        dp[i] = min(dp[i-customer] + cost, dp[i])
       

print(min(dp[customers:]))
