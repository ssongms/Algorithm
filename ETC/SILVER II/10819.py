# https://www.acmicpc.net/problem/10819

import sys
from itertools import permutations
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
maxResult = 0

def calc(array, N):
    result = 0
    for i in range(N-1):
        result += abs(array[i]-array[i+1])
    return result

for case in permutations(arr, N):
    n = calc(case, N)
    if maxResult < n:
        maxResult = n

print(maxResult)