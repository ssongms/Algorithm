# 카드 놓기
import sys
from itertools import permutations

input = sys.stdin.readline
n = int(input())
k = int(input())
cards = [int(input()) for _ in range(n)]

"""
# Not using Backtracking
result = []
for case in permutations(cards, k): # itertools 모듈의 순열(Permutation) 이용
    card = ''.join(map(str, case)) # 투플 형태인 case의 원소를 문자열로 합침
    if card not in result: # result 배열에 없는 case라면 추가
        result.append(card) 
print(len(result)) # result 배열의 길이를 출력

# => 통과
"""

# Using Backtracking
branch = []
result = []
visited = [False] * n # cards 배열의 길이인 n과 동일하게 설정
def cardBack():
    if len(branch) == k: # 재귀의 depth(branch의 길이)가 k와 같다면 조합이 완료된 상태 
        result.append(''.join(map(str, branch))) # 리스트 형태인 branch의 원소를 문자열로 합쳐서 result 배열에 저장
        return
    
    for idx, card in enumerate(cards): # 인덱스(0...n)와 원소에 직접 접근 가능하도록 enumerate 사용
        if not visited[idx]: # 해당 인덱스의 cards를 방문하지 않았다면
            branch.append(card) # branch에 append를 한 상태로 재귀를 호출하기 위함
            visited[idx] = True # 해당 인덱스 방문 표기 -> 그 다음 재귀에서 동일한 cards 배열의 인덱스를 사용하지 않게 하기 위함(if문에 걸리지 않도록)
            cardBack() # 백트래킹 재귀 호출
            branch.pop() # 콜 스택에서 재귀가 끝나면 branch에서 추가했던 마지막 원소를 다시 제거함으로써 '사용 가능'하게 만듦
            visited[idx] = False # 마찬가지로 다시 '방문 가능'하게 만듦

cardBack()
print(len(set(result))) # 중복 제거를 위해 set으로 바꿔주고 길이를 출력
# => 통과. 최적화 가능하지만 실행시간에 유의미한 영향을 주지 않음