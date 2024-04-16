# https://www.acmicpc.net/problem/1748
N = int(input())

a = (N+1 - pow(10, len(str(N))-1)) * len(str(N))
sum = 0
for i in range(len(str(N))-1):
    sum += 9 * pow(10, i) * (i+1)
print(a+sum)