import sys

listLen, minSum = map(int, sys.stdin.readline().split())
permutation = list(map(int, sys.stdin.readline().split()))

front = 0
rear = 0
partSum = 0
count = 0
result = []

while(front != listLen):
    while partSum < minSum and rear < listLen:
        partSum += permutation[rear]
        rear += 1
    if partSum >= minSum:
        count += 1
        result.append(len(permutation[front:rear]))
    partSum -= permutation[front]
    front += 1

if not result: print(0)
# else: print(min(result))