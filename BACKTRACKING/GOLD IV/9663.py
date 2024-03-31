# N - Queens 문제
# https://www.acmicpc.net/problem/9663

import sys

n = int(sys.stdin.readline())
result = 0
col = [0] * n

def isPromissing(x):
    for i in range(x):
        if col[x] == col[i] or abs(col[x] - col[i]) == abs(x - i):
            return False
    
    return True

def nQueens(x):
    global result
    if x == n:
        result += 1
        return

    else:
        for i in range(n):
            col[x] = i #퀸을 놓음
            if isPromissing(x):
                nQueens(x+1)

nQueens(0)
print(result)