import sys

N, M = map(int, sys.stdin.readline().split())
adjGraph = [[int(1e9) for _ in range(N+1)] for _ in range(N+1)]

def kevinBacon(N, adj):
    for i in range(1, N+1):
        for j in range(1, N+1):
            for k in range(1, N+1):
                if j == k:
                    adj[j][k] = 0
                else:
                    adj[j][k] = min(adj[j][k], adj[j][i] + adj[i][k])
    newGraph = []
    for i in range(1, N+1):
        slicedLine = adj[i][1:]
        newGraph.append(slicedLine)

    answer = []
    for row in newGraph:
        answer.append(sum(row))
    
    result = answer.index(min(answer)) + 1
    return result

for i in range(M): # 인접 그래프 입력
    a, b = map(int, sys.stdin.readline().split())
    adjGraph[a][b] = 1
    adjGraph[b][a] = 1

print(kevinBacon(N, adjGraph))