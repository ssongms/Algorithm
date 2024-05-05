R, C = map(int, input().split())
image = [list(map(int, input().split())) for _ in range(R)]
Threshold = int(input())
result = 0

# filtering function
def imgFilter(r, c):
    global result
    partNum = []
    for i in range(r, r+3):
        for j in range(c, c+3):
            partNum.append(image[i][j])
    partNum.sort()
    if Threshold <= partNum[4]:
        result += 1

for i in range(R-2):
    for j in range(C-2):
        imgFilter(i, j)

print(result)