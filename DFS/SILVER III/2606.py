computer = int(input()) # 컴퓨터의 수 : 1~100
pair = int(input()) # 연결된 컴퓨터 쌍의 개수

topology = [[0 for _ in range(101)] for _ in range(101)] # 인접 그래프를 표시하기 위한 2차원 배열
visited = [False] * 101 # 방문한 적이 있는지 확인하기 위한 배열
birus = 0 # 결과 (감염된 컴퓨터의 수)

for i in range(pair):
    c1, c2 = map(int, input().split())
    topology[c1][c2] = 1
    topology[c2][c1] = 1 # 인접 그래프를 표시

def birusSpread(startPC):
    global birus
    visited[startPC] = True # 현재 컴퓨터를 방문 Mark
    for endPC in range(1, computer+1): # 1번 컴퓨터부터 마지막 컴퓨터까지 확인
        if topology[startPC][endPC] == 1 and not visited[endPC]: # 방문한 적이 없고,토폴로지 상 이어져 있다면
            birus += 1
            birusSpread(endPC) # 재귀 호출

birusSpread(1) # 1번 컴퓨터부터 DFS 시작
print(birus)