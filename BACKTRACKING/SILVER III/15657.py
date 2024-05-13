N, M = map(int, input().split())
arr = list(map(int, input().split()))
result = []
branch = []
arr.sort()

def check():
    isTrue = True
    for i in range(1, len(branch)):
        if branch[i-1] > branch[i]:
            isTrue = False
            break
    return isTrue


def backtracking():
    if len(branch) == M:
        result.append(' '.join(map(str, branch)))
        return
    
    for elem in arr:
        branch.append(elem)
        if check():
            backtracking()
            branch.pop()
        else:
            branch.pop()


backtracking()
for i in result:
    print(i)