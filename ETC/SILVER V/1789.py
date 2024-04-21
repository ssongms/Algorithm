N = int(input())
num = 1
sum = 0
while sum < N:
    sum += num
    num += 1
if sum == N:
    print(num-1)
else:
    print(num-2)