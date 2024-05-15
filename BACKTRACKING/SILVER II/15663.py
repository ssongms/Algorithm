# N과 M(9)
import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

branch = []
result = []
visited = [False] * N

def backtracking():
    if len(branch) == M:
        res = ' '.join(map(str, branch))
        if res not in result:
            result.append(res)
        return
    
    for i, elem in enumerate(arr):
        if not visited[i]:
            branch.append(elem)
            visited[i] = True
            backtracking()
            branch.pop()
            visited[i] = False

backtracking()
for res in result:
    print(res)