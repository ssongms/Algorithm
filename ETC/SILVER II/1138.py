N = int(input())
info = list(map(int, input().split()))
line = [0] * N

line[info[0]] = 1
num = 2

for i in range(1, N):
    target = info[i]
    count = 0
    loc = 0
    for j in range(N):
        if count == target:
            loc = j
            break
        if line[j] == 0:
            count += 1
    
    if line[loc] == 0:
        line[loc] = num
        num += 1
        continue
    else:
        for j in range(loc, N):
            if line[j] == 0:
                line[j] = num
                num += 1
                break

print(' '.join(map(str, line)))