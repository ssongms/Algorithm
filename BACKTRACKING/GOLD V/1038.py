import sys

n = int(sys.stdin.readline())

# Brute Force 알고리즘
# 모든 경우의 수를 탐색
"""
bruteForce = []
for i in range(0, 10):
    bruteForce.append(i)

def isDecrease(num) :
    numToStr = str(num)
    for i in range(len(numToStr) - 1):
        if(numToStr[i] <= numToStr[i+1]):
            return False
    return True

for i in range (10, 9876543211):
    if isDecrease(i):
        bruteForce.append(i)

if(n > len(bruteForce)):
    print(-1)
else:
    print(bruteForce[n])
"""
# 시간 초과
    

solutionArr = []

def solution(num):
    solutionArr.append(int(num))

    for i in range(int(num[0])+1, 10):
        nextNum = str(i) + num
        solution(nextNum)



for digit in range(0, 10):
    charDigit = str(digit)
    solution(charDigit)
# solution('0) ~ solution('9')

solutionArr.sort()

if(n > len(solutionArr)-1):
    print(-1)
else:
    print(solutionArr[n])