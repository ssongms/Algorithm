# 크면서 작은 수 : https://www.acmicpc.net/problem/2992
import sys
from itertools import permutations
X = list(sys.stdin.readline().rstrip())
numX = int(''.join(X))
numL = []
for case in permutations(X, len(X)):
    num = int(''.join(case))
    if numX < num and num not in numL:
        numL.append(num)
if len(numL) == 0:
    print(0)
else:
    print(min(numL))