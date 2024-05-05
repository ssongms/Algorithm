node = int(input())
graph = [list(map(int, input().split())) for _ in range(node)]
visited = [[0 for _ in range(node)] for _ in range(node)]
# visited = [0] * node

for k in range(node):
    for a in range(node):
        for b in range(node):
            if graph[a][b] == 1 or graph[a][k] == 1 or graph[k][b] == 1:
                graph[a][b] = 1
        

print(graph)