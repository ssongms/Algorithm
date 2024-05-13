# N과 M(3)
N, M = map(int, input().split())
branch = []
res = []

def backtracking():
    if len(branch) == M:
        res.append(' '.join(map(str, branch)))
        return
    
    for i in range(1, N+1):
        branch.append(i)
        backtracking()
        branch.pop()

backtracking()
for i in res:
    print(i)