import re # 정규표현식 모듈

N = int(input())

def sumFunc(serial):
    nums = re.findall(r'\d', serial) # 1-9가 문자열 내에 매칭되면 각각 리스트의 원소로 저장
    return sum(map(int, nums)) # 정수형으로 바꿔주고 리스트의 합을 리턴

serialList = []
for i in range(N):
    serialInput = input()
    serialList.append(serialInput)

serialList.sort(key=lambda k:(len(k), sumFunc(k), k)) # 세 가지의 정렬 기준으로 정렬
# 1. 문자의 길이가 짧은 순
# 2. 문자열 내의 숫자의 합이 작은 순
# 3. 문자열 그 자체를 비교 (기본값으로 사전순)
for serial in serialList:
    print(serial)