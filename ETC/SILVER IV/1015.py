# https://www.acmicpc.net/problem/1015

size = int(input())
originArr = list(map(int, input().split()))
sortedArr = sorted(originArr) # O(NlogN)

copyArr = originArr[:]

count = 0
for elem in sortedArr:
    idx = originArr.index(elem)
    originArr[idx] = int(1e9)
    copyArr[idx] = count
    count += 1
        

print(" ".join(map(str, copyArr)))