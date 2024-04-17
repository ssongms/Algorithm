import math
N = int(input())

factorialN = math.factorial(N)
listFact = list(str(factorialN))
reverseList = listFact[::-1]

result = 0
for i in range(len(reverseList)):
    if reverseList[i] != '0':
        result = i
        break
print(result)