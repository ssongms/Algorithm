import sys

N = int(sys.stdin.readline())
fGraph = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
resultGraph = [[0 for _ in range(N)]for _ in range(N)]

def floyd(graph, N):
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if j == k:
                    continue
                if (graph[j][i] == 'Y' and graph[i][k] == 'Y') or graph[j][k] == 'Y':
                    resultGraph[j][k] = 1
    result = 0
    for row in resultGraph:
        result = max(result, sum(row))
    return result

print(floyd(fGraph, N))