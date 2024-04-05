import sys

small, big = list(map(int, sys.stdin.readline().split()))
primeLen = []
result = 0

def initializaList(n):
    sieve = [True] * n # sieve : 체
    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True: # i가 소수인 경우
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 리스트 리턴
    return [i for i in range(2, n) if sieve[i] == True]

primeList = initializaList(1000000)

def calcPrime(num):
    count = 0
    idx = 0
    prime = primeList[idx] # 초기값 2
    global result

    while prime <= num:
        if num % prime == 0:
            count += 1
            num /= prime
        else:
            idx += 1
            prime = primeList[idx]
    if count in primeList:
        result += 1

for num in range(small, big+1):
    calcPrime(num)

print(result)