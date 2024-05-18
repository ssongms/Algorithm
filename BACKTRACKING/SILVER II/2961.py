# 도영이가 만든 맛있는 음식 : https://www.acmicpc.net/problem/2961

# 신 맛 : 곱 / 쓴 맛 : 합
import sys
from itertools import combinations
input = sys.stdin.readline

N = int(input())

taste = [list(map(int, input().split())) for _ in range(N)]
result = int(1e9)
for i in range(1, N+1):
    for case in combinations(taste, i):
        sin = 1
        ssun = 0
        for elem in case:
            sin *= elem[0]
            ssun += elem[1]
        gap = abs(sin - ssun)
        if gap < result:
            result = gap
print(result)
