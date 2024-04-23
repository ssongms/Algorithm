import math #math.gcd(,) 사용 

n = int(input())
tmpList = list(map(int, input().split()))
numList = tmpList[::-1] # 계산 용이성을 위해 뒤집음

bunmo = numList[0] * numList[1] + 1
bunza = numList[0]

for i in range(2, n):
    bunza, bunmo = bunmo, bunza # 분모, 분자 swap
    bunmo = bunza * numList[i] + bunmo

gcdNum = math.gcd(bunmo, bunza)

if gcdNum != 1: # 기약 분수가 아니면
    bunmo //= gcdNum
    bunza //= gcdNum # 두 분모 분자의 최대 공약수로 나눔

print(bunmo-bunza, bunmo)