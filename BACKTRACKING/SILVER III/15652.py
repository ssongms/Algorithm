# N과 M(4)

N, M = map(int, input().split())
branch = []
res = []

def check():
    for i in range(1, len(branch)):
        if branch[i-1] > branch[i]:
            return False
    return True

def backtracking():
    if len(branch) == M:
        res.append(' '.join(map(str, branch)))
        return
    
    for i in range(1, N+1):
        branch.append(i)
        if check():
            backtracking()
            branch.pop()
        else:
            branch.pop()

backtracking()
for i in res:
    print(i)