paper = [[0 for _ in range(100)]for _ in range(100)]

n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    for j in range(10):
        for k in range(10):
            paper[99-(10+y)+j][x+k] = 1

result = 0
for i in range(100):
    result += paper[i].count(1)
print(result)