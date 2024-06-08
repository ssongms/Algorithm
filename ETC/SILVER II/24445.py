
# 메모리 초과
# import sys
# from collections import deque

# Node, EdgeCnt, Start = map(int, sys.stdin.readline().split())

# adjGraph = [[0 for _ in range(Node+1)] for _ in range(Node+1)]
# visited = [False for _ in range(Node+1)]
# visitOrder = [0 for _ in range(Node)]
# cnt = 1

# for Edge in range(EdgeCnt):
#     start, end = map(int, sys.stdin.readline().split())
#     adjGraph[start][end]  = 1

# def bfs(mat, i, visited):
#     global cnt
#     queue = deque()
#     queue.append(i)
#     while queue:
#         val = queue.pop()
#         if not visited[val]:
#             visitOrder[val-1] = cnt
#             cnt += 1
#             visited[val] = True
#             for c in range(len(mat[val])):
#                 if mat[val][c] == 1 and not visited[c]:
#                     queue.append(c)

# bfs(adjGraph, Start, visited)
# for order in visitOrder:
#     print(order)

from collections import deque

n, m, k = map(int,input().split())
l = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int,input().split())
    l[a].append(b)
    l[b].append(a)

for i in range(n+1):
    l[i].sort(reverse=True)

q = deque()
q.append(k)
ans = [0]*(n+1)
ans[k] = 1
cnt = 2
while q:
    x=q.popleft()
    for i in l[x]:
        if ans[i] == 0:
            ans[i] = cnt
            cnt += 1
            q.append(i)

print(*ans[1:],sep='\n')