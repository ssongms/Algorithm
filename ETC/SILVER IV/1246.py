N, M = map(int, input().split())

P = []

for i in range(M):
    Pi = int(input())
    P.append(Pi)

P.sort() # 오름차순 정렬

profits = []
if N <= M :
    for i in range(N):
        price = P[M-i-1]
        profit = price * (i+1)
        profits.append([profit, price])
    profit, price = max(profits)
    print(price, profit)
else:
    for i in range(M):
        price = P[i]
        profit = P[i] * (M-i)
        profits.append([profit, price])

    profit, price = max(profits)
    print(price, profit)