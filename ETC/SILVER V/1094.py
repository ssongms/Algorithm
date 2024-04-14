# https://www.acmicpc.net/problem/1094

stick = int(input())
stickLen = [1, 2, 4, 8, 16, 32, 64] # 길이 : 7
mask = [0, 0, 0, 0, 0, 0, 0]
curLen = 0

while stick != 0:
    if stick == 64:
        mask[6] = 1
        break
    for i in range(len(stickLen)-1):
        if stickLen[i+1] > stick and mask[i] != 1:
            mask[i] = 1 # 비트 마스킹
            stick -= stickLen[i]
            break
print(mask.count(1))