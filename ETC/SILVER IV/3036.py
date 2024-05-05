import math
N = int(input())
radiusList = list(map(int, input().split()))
result = []

def frac(n):
    gcdN = math.gcd(n, radiusList[0])
    res = str(radiusList[0]//gcdN) + '/' + str(n//gcdN)
    result.append(res)
    
for i in range(1, len(radiusList)):
    frac(radiusList[i])

for i in range(len(result)):
    print(result[i])