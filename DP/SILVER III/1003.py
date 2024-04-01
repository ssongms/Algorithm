#https://www.acmicpc.net/problem/1003

def DP_Fibonacci(num):
    zeroFibonacciArr = [0] * (num+1)
    oneFibonacciArr = [0] * (num+1)
    for i in range(num+1):
        if i == 0 :
            zeroFibonacciArr[i] = 1
            oneFibonacciArr[i] = 0
        elif i == 1:
            zeroFibonacciArr[i] = 0
            oneFibonacciArr[i] = 1
        else:
            zeroFibonacciArr[i] = zeroFibonacciArr[i-1] + zeroFibonacciArr[i-2]
            oneFibonacciArr[i] = oneFibonacciArr[i-1] + oneFibonacciArr[i-2]
    resultList.append(zeroFibonacciArr[num])
    resultList.append(oneFibonacciArr[num])

resultList = []
case = int(input())

for i in range(case):
    inputNum = int(input())
    DP_Fibonacci(inputNum)

for i in range(case):
    print(resultList[2*i], resultList[2*i+1])
    
