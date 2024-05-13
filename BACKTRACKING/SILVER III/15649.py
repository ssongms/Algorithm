# Not using Backtracking

# from itertools import permutations
# N, M = map(int, input().split())
# arr = [i for i in range(1, N+1)]
# case = permutations(arr, M)

# for a in case:
#     print(' '.join(map(str, a)))

#==========================================================

# Using Backtracking
N, M = map(int, input().split())

branch = []
res = []
def backtracking():
    if len(branch) == M:
        print(' '.join(map(str, branch)))
        return

    for i in range(1, N+1):
        if i not in branch:
            branch.append(i)
            backtracking()
            branch.pop()

backtracking()