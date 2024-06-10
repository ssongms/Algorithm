# https://www.acmicpc.net/problem/1337

import sys
N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(N)]
arr.sort() # 오름차순 정렬
result = 0

if N == 1:
    print(4)
else:
    pointer = 0
    cntArr = []
    cnt = 0
    while pointer < len(arr):
        num1 = arr[pointer]+1
        num2 = arr[pointer]+2
        num3 = arr[pointer]+3
        num4 = arr[pointer]+4
        if num1 in arr[pointer+1:]:
            cnt += 1
        if num2 in arr[pointer+1:]:
            cnt += 1
        if num3 in arr[pointer+1:]:
            cnt += 1
        if num4 in arr[pointer+1:]:
            cnt += 1

        cntArr.append(cnt)
        if cnt >= 4:
            break
        
        cntArr.append(cnt)
        cnt = 0
        pointer += 1
        
    if max(cntArr) == 0:
        print(4)
    elif max(cntArr) >= 4:
        print(0)
    else:
        print(4-max(cntArr))