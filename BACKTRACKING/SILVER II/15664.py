import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

branch = []
result = []
visited = [False] * N
arr.sort()

def isIndescending(): # branch 배열이 비오름차순인지 확인하는 함수 정의
    for i in range(1, len(branch)): # branch에 원소가 하나일 때는 검사하지 않도록 for문을 1부터 len(branch)-1 까지로 설정
        if branch[i-1] > branch[i]:
            return False # 비오름차순이 아니라면 여기서 return하고 함수 종료
    return True # 비오름차순이 맞다면 for문을 통과하고 여기에서 return


def backtracking():
    if len(branch) == M: # 재귀 탈출 조건
        tempStr = ' '.join(map(str, branch))
        if tempStr not in result: # 중복된 값을 저장하지 않기 위해 조건문 추가
            result.append(tempStr)
    
    for idx, element in enumerate(arr):
        if not visited[idx]: # 방문하지 않았다면
            branch.append(element)
            if isIndescending(): # 방금 element를 branch에 추가했을 때, branch 배열이 비오름차순을 지키는지 확인하는 함수
                visited[idx] = True # 해당 인덱스를 방문 마킹
                backtracking() # 백트래킹 재귀 호출
                branch.pop() # 재귀 함수가 끝나면 실행되는 포인트 -> 추가했던 element를 다시 pop해서 사용가능하게 만듦
                visited[idx] = False # 마찬가지로 다시 방문 가능하게 만듦
            else:
                branch.pop() # 비오름차순이 아니기 때문에 추가했던 element를 pop해서 아무일도 없던 것으로 만듦

backtracking()
for res in result: # 결과 출력
    print(res)