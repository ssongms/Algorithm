# N과 M(12)

N, M = map(int, input().split())
inputArr = list(map(int, input().split()))
arr = sorted(list(set(inputArr)))

branch = []
res = []

def check():
    for i in range(1, len(branch)):
        if branch[i-1] > branch[i]:
            return False
    return True

def backtracking():
    if len(branch) == M:
        # print(' '.join(map(str, branch)))
        res.append(branch[:])
        return
    
    for elem in arr:
        branch.append(elem)
        if check():
            backtracking()
            branch.pop()
        else:
            branch.pop()

backtracking()
for i in res:
    print(' '.join(map(str, i)))