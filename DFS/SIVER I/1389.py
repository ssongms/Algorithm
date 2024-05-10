import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
adjGraph = [[0 for _ in range(N+1)] for _ in range(N+1)]


def kevinBacon(N, adj):
    kevin = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for i in range(N+1):
        for j in range(N+1):
            for k in range(N+1):
                if adj[j][i] == 1 and adj[i][k] == 1:
                    kevin[j][k] += 1
    for line in kevin:
        print(*line)


for i in range(M): # 인접 그래프 입력
    a, b = map(int, sys.stdin.readline().split())
    adjGraph[a][b] = 1
    adjGraph[b][a] = 1

kevinBacon(N, adjGraph)