import sys
from collections import Counter

S = list(sys.stdin.readline().rstrip())
L = len(S)
counters = Counter(S)
result = 0

def backtracking(prev, cur):
    global result
    if len(cur) == L: # counters의 모든 문자를 사용해서 '행운의 문자열'이 된 경우
        result += 1 
        return # 재귀 탈출
    
    for letter in counters: # S = ['a', 'b', 'a']인 경우 letter은 a, b
        if (prev == letter) or (counters[letter] == 0) : # 이전 문자가 현재 추가하려는 letter와 같을 때, 혹은 0개라 더이상 사용할 수 있는 letter가 없을 때
            continue # 다음 반복문
        counters[letter] -= 1 # 재귀 호출에서 문자열을 만들 때 A를 사용했다면 해당 문자의 빈도를 1 감소시켜서 다음 재귀 호출에서 다시 A를 선택하지 못하도록 함
        backtracking(letter, cur+letter)
        counters[letter] += 1 # 그리고 재귀 호출이 완료되면 해당 문자의 빈도를 다시 1 증가시켜서 다음 재귀 호출에서 해당 문자를 사용할 수 있도록 복구함
    
backtracking('@', '') # 첫 비교를 위해 prev를 쓰레기값으로 설정하여 호출
print(result)