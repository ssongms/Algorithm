import sys

N = int(sys.stdin.readline())
prefixSet = []
for _ in range(N):
    prefixSet.append(input())
prefixSet.sort(key=len)
resultList = []
for i in range(N-1):
    for j in range(i+1, N):
        if str(prefixSet[j]).startswith(str(prefixSet[i])):
            resultList.append(prefixSet[i])
            break
    
print(len(prefixSet)-len(resultList))