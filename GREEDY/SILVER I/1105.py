import sys

start, end = map(str, sys.stdin.readline().split())
result = 0
# 처음부터 start, end 둘 중에 하나라도 8이 안들어가 있다면 답은 0

if '8' in start and '8' in end:
    result = start.count('8')
    while int(start) <= int(end):
        if '8' not in start:
            result = 0
            break
        else:
            # start에 들어있는 8의 개수를 result에 저장
            # 단 이미 저장돼있는 result보다 작은 경우에만 업데이트
            if start.count('8') < result:
                result = start.count('8')
            start = str(int(start)+1)
print(result)