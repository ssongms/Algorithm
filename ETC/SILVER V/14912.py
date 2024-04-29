n, d = map(int, input().split())
result = 0
for i in range(1, n+1):
    result += str(i).count(str(d))
print(result)