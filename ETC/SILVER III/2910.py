import sys
N, C = map(int, sys.stdin.readline().split())

numList = list(map(int, sys.stdin.readline().split()))
dictNum = dict()
for i in range(len(numList)):
    if numList[i] not in dictNum:
        dictNum[numList[i]] = 1
    else:
        dictNum[numList[i]] += 1

x = sorted(dictNum.items(), key=lambda x:-x[1])
for key, freq in x:
    print((str(key) + " ") * freq, end="")
