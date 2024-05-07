def floyd(node, graph):
    for i in range(node):
        for j in range(node):
            for k in range(node):
                if graph[j][i] == 1 and graph[i][k] == 1: # j에서 i까지 연결돼있고, i에서 k까지 연결돼있다면
                    graph[j][k] = 1 # j와 k도 연결돼있음 (여기서 i는 중간 노드의 역할)

# main 
node = int(input()) # 노드의 개수 입력
adjacentGraph = [list(map(int, input().split())) for _ in range(node)] # 인접 그래프 입력
floyd(node, adjacentGraph) # 플로이드 워셜 함수 호출
        
for line in adjacentGraph: # 출력문
    print(*line)