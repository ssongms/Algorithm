# N과 M(11)

N, M = map(int, input().split())
inputArr = list(map(int, input().split()))
arr = sorted(list(set(inputArr)))

branch = []
res = []

def backtracking():
    if len(branch) == M:
        res.append(' '.join(map(str, branch)))
        return
    
    for elem in arr:
        branch.append(elem)
        backtracking()
        branch.pop()

backtracking()
for i in res:
    print(i)