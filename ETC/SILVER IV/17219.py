N, M = map(int, input().split())
memo = {}
result = []

for i in range(N):
    site, password = map(str, input().split())
    memo[site] = password

for i in range(M):
    site = input()
    result.append(memo[site])

for i in range(len(result)):
    print(result[i])