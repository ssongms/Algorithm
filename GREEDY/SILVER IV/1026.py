# https://www.acmicpc.net/problem/1026

len = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(reverse=False)
B.sort(reverse=True)

result = 0
for i in range(len):
    result += A[i] * B[i]
print(result)