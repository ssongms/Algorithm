# Using combinations
# import sys
# from itertools import combinations

# input = sys.stdin.readline

# N, S = map(int, input().split())
# arr = list(map(int, input().split()))
# cnt = 0

# for i in range(1, N+1):
#     caseTup = combinations(arr, i)
#     for case in caseTup:
#         if sum(case) == S:
#             cnt += 1
# print(cnt)

# Using backtracking
import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

def subsetSum(idx, tempSum):
    global cnt

    if idx >= N: # 재귀 탈출 조건
        return
    
    tempSum += arr[idx] # 현재 배열의 수를 더해봄
    if tempSum == S: # 원하는 합과 같으면 cnt++
        cnt += 1
    
    subsetSum(idx+1, tempSum) # 현재 배열의 수를 선택한 것
    subsetSum(idx+1, tempSum-arr[idx]) # 현재 배열의 수를 선택하지 않은 것

subsetSum(0, 0)
print(cnt)