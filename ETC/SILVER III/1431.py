import re

N = int(input())

def sumFunc(serial):
    nums = re.findall(r'\d', serial)
    return sum(map(int, nums))

serialList = []
for i in range(N):
    serialInput = input()
    serialList.append(serialInput)

serialList.sort(key=lambda k:(len(k), sumFunc(k), k))
for serial in serialList:
    print(serial)