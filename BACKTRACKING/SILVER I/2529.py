import sys
input = sys.stdin.readline

# Not Using Backtracking
from itertools import permutations

k = int(input())
operations = list(input().split())
numL = [i for i in range(10)]
res = []
for case in permutations(numL, k+1):
    for idx, oper in enumerate(operations):
        if oper == '<':
            if case[idx] > case[idx+1]: break
        else:
            if case[idx] < case[idx+1]: break
    else:
        res.append(''.join(map(str, case)))

print(max(res))
print(min(res))


# Using Backtracking

# branch = []
# res = []
# def backtracking(idx, s):
#     if len(branch) >= 2 and operation == '>':
#         if branch[idx-1] <= branch[idx]:
#             return
#     if len(branch) >= 2 and operation == '<':
#         if branch[idx-1] >= branch[idx]:
#             return

#     if idx == k+1:
#         res.append(''.join(map(str, branch)))

    
#     for i in range(0, 10):
#         if i not in branch:
#             if (idx == 0) or 
#             branch.append(i)
#             backtracking(i, operations[i])
#             branch.pop()

# backtracking(0, '')
# print(min(res))