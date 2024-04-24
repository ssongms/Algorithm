N, M = map(int, input().split())

if N < M:
    factorial = [1] * (M+1)
    result = 1
    for i in range(2, N+1):
        factorial[i] = (factorial[i-1] * i) % M

    print(factorial[N])
else:
    print(0)